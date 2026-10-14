"""Parity-correct odd sine diagnostic for the cutoff-free Archimedean block.

Basis psi_k(w)=sqrt(2) sin(2*pi*k*w), k>=1. The existing resolvent
convention uses K=2B; in this odd sector B(1)=-I, hence K(1)=-2I.

Diagnostic only: this is not a positivity theorem or an RH proof.
"""
from __future__ import annotations
import mpmath as mp

def _terms(i: int, j: int):
    ci={i:mp.sqrt(2)/(2j),-i:-mp.sqrt(2)/(2j)}
    cj={j:mp.sqrt(2)/(2j),-j:-mp.sqrt(2)/(2j)}
    out=[]
    for m,cm in ci.items():
        for n,cn in cj.items():
            base=cm*cn; d=m-n
            if d==0: out.append(("w",n,base))
            else:
                z=base/(2j*mp.pi*d)
                out.extend([("e",m,z),("e",n,-z)])
    return out

def bilinear_block_entry(i,j,w):
    value=mp.mpc(0)
    for kind,alpha,coeff in _terms(i,j):
        phase=mp.exp(2j*mp.pi*alpha*w)
        value += coeff*(w*phase if kind=="w" else phase)
    return mp.re(value)

def _exp_integral(A,alpha):
    nu=A+2j*mp.pi*alpha
    return (mp.e**(2j*mp.pi*alpha)-mp.e**(-A))/nu

def _w_exp_integral(A,alpha):
    nu=A+2j*mp.pi*alpha
    return (mp.e**(2j*mp.pi*alpha)*(nu-1)+mp.e**(-A))/(nu*nu)

def integrated_bilinear_entry(i,j,A):
    value=mp.mpc(0)
    for kind,alpha,coeff in _terms(i,j):
        value += coeff*(_w_exp_integral(A,alpha) if kind=="w" else _exp_integral(A,alpha))
    return mp.re(value)

def endpoint_check(N,dps=60):
    mp.mp.dps=dps
    return 2*max(abs(bilinear_block_entry(i,j,mp.mpf(1))-(-1 if i==j else 0))
                  for i in range(1,N+1) for j in range(1,N+1))

def archimedean_matrix(c,N,n_terms=1000,dps=60):
    if c<=1 or N<1 or n_terms<=0:
        raise ValueError("require c > 1, N >= 1, and n_terms > 0")
    mp.mp.dps=dps
    L=mp.log(c)
    h0=mp.re(mp.digamma(mp.mpf("0.25")))-mp.log(mp.pi)
    A=(-h0)*mp.eye(N)
    for n in range(n_terms):
        a=mp.mpf(n)+mp.mpf("0.25")
        decay=2*L*a
        for i in range(1,N+1):
            for j in range(1,N+1):
                K1=-2 if i==j else 0
                A[i-1,j-1] += K1/(2*a)-L*(2*integrated_bilinear_entry(i,j,decay))
    return (A+A.T)/2

if __name__=="__main__":
    c,N=20,6
    A=archimedean_matrix(c,N,n_terms=3000,dps=50)
    print("endpoint_K_error=",mp.nstr(endpoint_check(N,50),20))
    print("lambda_min=",mp.nstr(min(mp.eigsy(A,eigvals_only=True)),20))

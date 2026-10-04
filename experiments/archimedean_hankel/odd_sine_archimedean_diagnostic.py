"""Odd-sector Archimedean diagnostic.

This is derived from the same cutoff-free resolvent identity used by the
existing cosine implementation, but with the physical odd sine basis.

For psi_k(w)=sqrt(2) sin(2*pi*k*w), k>=1,
K_ij(1)=int_0^1 psi_i(t) psi_j(1-t) dt = -2 delta_ij.
Thus the anchor h_+(0)/2*K(1) becomes -h_+(0) I.

The script deliberately labels the result a candidate odd Archimedean
restriction until the physical normalization/pole derivation is closed.
"""

from __future__ import annotations
import math
from typing import Dict, List, Tuple
import mpmath as mp

def _terms(i: int, j: int):
    inv = 1 / mp.sqrt(2)
    ci = { -i: 1/(mp.sqrt(2)*1j), i: -1/(mp.sqrt(2)*1j) }
    cj = { -j: 1/(mp.sqrt(2)*1j), j: -1/(mp.sqrt(2)*1j) }
    out=[]
    for m,cm in ci.items():
        for n,cn in cj.items():
            base=cm*cn
            d=m-n
            if d==0:
                out.append(("w", n, base))
            else:
                factor=base/(2j*mp.pi*d)
                out.append(("e",m,factor))
                out.append(("e",n,-factor))
    return out

def K_entry(i:int,j:int,w:mp.mpf)->mp.mpf:
    v=mp.mpc(0)
    for kind,a,c in _terms(i,j):
        phase=mp.exp(2j*mp.pi*a*w)
        v += c*w*phase if kind=="w" else c*phase
    return mp.re(v)

def _exp_integral(A,alpha):
    nu=A+2j*mp.pi*alpha
    return (mp.exp(2j*mp.pi*alpha)-mp.exp(-A))/nu

def _w_exp_integral(A,alpha):
    nu=A+2j*mp.pi*alpha
    return (mp.exp(2j*mp.pi*alpha)*(nu-1)+mp.exp(-A))/(nu*nu)

def integrated_K(i,j,A):
    v=mp.mpc(0)
    for kind,a,c in _terms(i,j):
        I=_w_exp_integral(A,a) if kind=="w" else _exp_integral(A,a)
        v += c*I
    return mp.re(v)

def prime_powers(c):
    out=[]
    for p in range(2,c+1):
        if all(p%d for d in range(2,int(math.isqrt(p))+1)):
            q=p
            while q<=c:
                out.append((q,p))
                if q>c//p: break
                q*=p
    return sorted(out)

def prime_matrix(c,N):
    L=mp.log(c)
    P=mp.matrix(N,N)
    for q,p in prime_powers(c):
        w=1-mp.log(q)/L
        weight=-2*mp.log(p)/mp.sqrt(q)
        for i in range(1,N+1):
            for j in range(1,N+1):
                P[i-1,j-1]+=weight*K_entry(i,j,w)
    return (P+P.T)/2

def arch_matrix(c,N,n_terms=1000):
    L=mp.log(c)
    h0=mp.re(mp.digamma(mp.mpf("0.25")))-mp.log(mp.pi)
    A=-h0*mp.eye(N)
    for n in range(n_terms):
        a=mp.mpf(n)+mp.mpf("0.25")
        decay=2*L*a
        for i in range(1,N+1):
            for j in range(1,N+1):
                K1=-2 if i==j else 0
                A[i-1,j-1]+=K1/(2*a)-L*2*integrated_K(i,j,decay)
    return (A+A.T)/2

def combined(c=20,N=6,n_terms=1000,dps=50):
    mp.mp.dps=dps
    P=prime_matrix(c,N)
    A=arch_matrix(c,N,n_terms)
    C=(P+A+ (P+A).T)/2
    vals=mp.eigsy(C,eigvals_only=True)
    return P,A,vals

if __name__=="__main__":
    P,A,vals=combined()
    print("c=20 N=6 T=1000")
    print("prime_min =",mp.nstr(min(mp.eigsy(P,eigvals_only=True)),18))
    print("arch_min =",mp.nstr(min(mp.eigsy(A,eigvals_only=True)),18))
    print("combined_min =",mp.nstr(min(vals),18))
    k1_err = max(abs(K_entry(i, j, mp.mpf("1")) - (-2 if i == j else 0)) for i in range(1, N + 1) for j in range(1, N + 1))\n    print("K1_max_error =", mp.nstr(k1_err, 18))\n    if k1_err > mp.mpf("1e-40"):\n        raise AssertionError("odd convolution endpoint K(1) != -2 I")\n    print("classification = CANDIDATE ODD ARCHIMEDEAN + PRIME RESTRICTION")

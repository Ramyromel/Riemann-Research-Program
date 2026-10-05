"""Experimental autocorrelation-corrected odd Archimedean resolvent.

For a real odd test function f, the Fourier transform of |F|^2 is the
autocorrelation C(t)=∫f(y)f(y-t)dy = -(f*f)(t). The current odd diagnostic
uses the convolution itself. This experiment flips that sign at the kernel
level while leaving every other convention unchanged, and compares the result
with the direct spectral reference.
"""
from __future__ import annotations
import numpy as np
from direct_physical_spectral_archimedean_audit import spectral_archimedean_matrix
from archimedean_hankel.odd_sine_archimedean_diagnostic import integrated_K
import mpmath as mp


def corrected_matrix(c: int, n: int, n_terms: int = 3000):
    mp.mp.dps = 50
    L = mp.log(c)
    h0 = mp.re(mp.digamma(mp.mpf("0.25"))) - mp.log(mp.pi)
    A = h0 * mp.eye(n)
    for m in range(n_terms):
        aa = mp.mpf(m) + mp.mpf("0.25")
        decay = 2 * L * aa
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                raw = integrated_K(i, j, decay)
                K1 = 2 if i == j else 0
                A[i-1,j-1] += K1/(2*aa) + 2*L*raw
    return (A + A.T)/2


def run(c=20,n=6):
    a=.5*np.log(c)
    spectral=spectral_archimedean_matrix(a,n,R=500,nr=100001)
    candidate=np.asarray(corrected_matrix(c,n).tolist(),dtype=float)
    d=candidate-spectral
    print(f"c={c} n={n}")
    print("spectral_lambda_min=",np.linalg.eigvalsh(spectral)[0])
    print("corrected_lambda_min=",np.linalg.eigvalsh(candidate)[0])
    print("frobenius_difference=",np.linalg.norm(d))
    print("max_entry_difference=",np.max(np.abs(d)))
    print("candidate_matrix=")\n    print(candidate)\n    print("spectral_matrix=")\n    print(spectral)\n    print("difference_matrix=")\n    print(d)\n    print("classification=EXPERIMENTAL_AUTOCORRELATION_SIGN_TEST")


if __name__=="__main__":
    run()

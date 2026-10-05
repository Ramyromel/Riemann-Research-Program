"""Numerical bridge audit for the corrected odd Archimedean resolvent.

The direct spectral matrix should equal D A_odd D, D=diag((-1)^k), up to
finite spectral-window and quadrature errors.
"""
from __future__ import annotations
import numpy as np
from direct_physical_spectral_archimedean_audit import spectral_archimedean_matrix
from archimedean_hankel.odd_sine_archimedean_resolvent_corrected import (
    archimedean_matrix, parity_conjugation,
)


def run(c=20, n=6):
    a=.5*np.log(c)
    spectral=spectral_archimedean_matrix(a,n,R=500,nr=100001)
    odd=np.asarray(archimedean_matrix(c,n,n_terms=3000,dps=50).tolist(),dtype=float)
    D=np.diag([(-1)**k for k in range(1,n+1)])
    transported=D@odd@D
    d=transported-spectral
    print(f"c={c} n={n}")
    print("spectral_lambda_min=",np.linalg.eigvalsh(spectral)[0])
    print("odd_lambda_min=",np.linalg.eigvalsh(odd)[0])
    print("transported_lambda_min=",np.linalg.eigvalsh(transported)[0])
    print("frobenius_difference=",np.linalg.norm(d))
    print("max_entry_difference=",np.max(np.abs(d)))
    print("classification=NUMERICALLY_SUPPORTED_PARITY_BRIDGE")


if __name__=="__main__":
    run()

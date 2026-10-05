"""Analytic parity bridge for the odd sine sector.

With phi_k(2w-1)=(-1)^k sin(2*pi*k*w), the odd physical basis differs from
the repository w-basis only by D=diag((-1)^k). Hence an operator represented
in the sine basis is transported to the w convention by D A D.
"""
from __future__ import annotations
import numpy as np

def parity_sign(k: int) -> int:
    return -1 if k % 2 else 1

def parity_conjugation(A):
    A=np.asarray(A,dtype=float)
    n=A.shape[0]
    D=np.diag([parity_sign(k) for k in range(1,n+1)])
    return D@A@D

def basis_identity(k: int, w):
    return np.sin(k*np.pi*(2*w-1)) / (parity_sign(k)*np.sin(2*k*np.pi*w)) if abs(np.sin(2*k*np.pi*w))>1e-14 else np.nan

def verify_basis_identity(samples=(0.17,0.29,0.41,0.63,0.81), n=8):
    for k in range(1,n+1):
        for w in samples:
            lhs=np.sin(k*np.pi*(2*w-1))
            rhs=parity_sign(k)*np.sin(2*k*np.pi*w)
            if abs(lhs-rhs)>1e-13:
                return False
    return True

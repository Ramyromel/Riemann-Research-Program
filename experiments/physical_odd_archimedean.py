"""Standalone physical odd Archimedean operator assembly.

This module contains only the physical-coordinate kernel
H_Leg + c0 I + V - K_gamma. It deliberately has no dependency on the
repository resolvent diagnostic, so normalization audits cannot become
circular through imports.
"""
from __future__ import annotations
import math
import numpy as np
from numpy.polynomial.legendre import leggauss


def rho(z):
    z = np.asarray(z, dtype=float)
    out = np.empty_like(z)
    small = np.abs(z) < 1.0e-6
    zz = z[~small]
    out[~small] = np.exp(-zz / 2.0) / (-np.expm1(-2.0 * zz)) - 1.0 / (2.0 * zz)
    zs = z[small]
    out[small] = 0.25 - zs / 48.0 - zs * zs / 32.0 + 7.0 * zs**3 / 11520.0
    return out


def physical_archimedean_matrix(a: float, n: int, order: int = 400):
    nodes, weights = leggauss(order)
    x, w = nodes, weights
    F = np.array([[math.sin(k * math.pi * xx) for xx in x] for k in range(1, n + 1)])
    X, Y = x[:, None], x[None, :]
    D = X - Y
    W2 = w[:, None] * w[None, :]
    H = np.zeros((n, n))
    V = np.zeros((n, n))
    K = np.zeros((n, n))
    for i in range(n):
        fi = F[i]
        for j in range(n):
            fj = F[j]
            num = (fi[:, None] - fi[None, :]) * (fj[:, None] - fj[None, :])
            q = np.divide(num, np.abs(D), out=np.zeros_like(D), where=np.abs(D) > 1e-14)
            H[i, j] = 0.25 * np.sum(W2 * q)
            V[i, j] = np.sum(w * (-0.5 * np.log(1.0 - x * x)) * fi * fj)
            K[i, j] = a * np.sum(W2 * fi[:, None] * rho(a * np.abs(D)) * fj[None, :])
    c0 = -math.log(a) - math.log(2.0 * math.pi) - 0.5772156649015328606
    A = H + c0 * np.eye(n) + V - K
    return (A + A.T) / 2.0

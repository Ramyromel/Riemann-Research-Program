"""Direct physical odd Archimedean matrix audit.

This diagnostic independently discretizes the physical normalized form
H_Leg + c0(a) I + V - K_gamma,a on (-1,1) in the sine basis
phi_k(x)=sin(k*pi*x), and compares it with the repository's odd
resolvent representation.

The quadrature is deliberately diagnostic, not a certificate. A mismatch
is evidence that the normalization bridge is not yet established; it is
not a counterexample to Weil positivity or RH.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

sys.path.insert(0, str(Path(__file__).resolve().parent / "archimedean_hankel"))
from odd_sine_archimedean_diagnostic import archimedean_matrix


def rho(z):
    z = np.asarray(z, dtype=float)
    out = np.empty_like(z)
    small = np.abs(z) < 1.0e-6
    zz = z[~small]
    out[~small] = np.exp(-zz / 2.0) / (-np.expm1(-2.0 * zz)) - 1.0 / (2.0 * zz)
    # rho(z)=1/4-z/48-z^2/32+7z^3/11520+O(z^4)
    zs = z[small]
    out[small] = 0.25 - zs / 48.0 - zs * zs / 32.0 + 7.0 * zs**3 / 11520.0
    return out


def physical_archimedean_matrix(a: float, n: int, order: int = 400):
    nodes, weights = leggauss(order)
    x = nodes
    w = weights
    F = np.array([[math.sin(k * math.pi * xx) for xx in x] for k in range(1, n + 1)])

    X = x[:, None]
    Y = x[None, :]
    D = X - Y
    W2 = w[:, None] * w[None, :]

    H = np.zeros((n, n))
    V = np.zeros((n, n))
    K = np.zeros((n, n))

    for i in range(n):
        fi = F[i]
        dpi = (i + 1) * math.pi * np.cos((i + 1) * math.pi * x)
        for j in range(n):
            fj = F[j]
            dpj = (j + 1) * math.pi * np.cos((j + 1) * math.pi * x)

            num = (fi[:, None] - fi[None, :]) * (fj[:, None] - fj[None, :])
            q = np.zeros_like(D)
            mask = np.abs(D) > 1.0e-14
            q[mask] = num[mask] / np.abs(D[mask])
            # Gauss nodes are distinct, so diagonal entries have zero weight.
            H[i, j] = 0.25 * np.sum(W2 * q)

            V[i, j] = np.sum(
                w * (-0.5 * np.log(1.0 - x * x)) * fi * fj
            )

            K[i, j] = a * np.sum(
                W2 * fi[:, None] * rho(a * np.abs(D)) * fj[None, :]
            )

    c0 = -math.log(a) - math.log(2.0 * math.pi) - 0.5772156649015328606
    A = H + c0 * np.eye(n) + V - K
    return (A + A.T) / 2.0


def run(c=20, n=6):
    a = 0.5 * math.log(c)
    direct_prev = None
    for order in (160, 240, 320, 480):
        direct = physical_archimedean_matrix(a, n, order)
        if direct_prev is not None:
            conv = np.linalg.norm(direct - direct_prev, ord="fro")
        else:
            conv = float("nan")
        direct_prev = direct
        print(f"order={order} direct_lambda_min={np.linalg.eigvalsh(direct)[0]:.15g} convergence={conv:.3e}")

    resolvent = np.asarray(archimedean_matrix(c, n, n_terms=3000, dps=50).tolist(), dtype=float)
    diff = direct - resolvent
    print("frobenius_difference=", np.linalg.norm(diff, ord="fro"))
    print("max_entry_difference=", np.max(np.abs(diff)))
    print("resolvent_lambda_min=", np.linalg.eigvalsh(resolvent)[0])
    print("classification=NUMERICAL_NORMALIZATION_MISMATCH_OPEN")


if __name__ == "__main__":
    run()

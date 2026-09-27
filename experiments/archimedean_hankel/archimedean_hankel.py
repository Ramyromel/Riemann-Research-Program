"""Finite-basis matrix realization of the cutoff-free archimedean block.

The implementation evaluates the exact Volterra/resolvent identity from
docs/archimedean-resolvent-reduction.md.  The infinite resolvent series is
truncated at n_terms for numerical exploration; no RH-zero data are used.
"""

from __future__ import annotations

import math
from typing import Dict, List, Tuple

import mpmath as mp


def fourier_coefficients(N: int) -> List[Dict[int, mp.mpf]]:
    coeffs: List[Dict[int, mp.mpf]] = [{0: mp.mpf(1)}]
    inv_sqrt2 = 1 / mp.sqrt(2)
    for k in range(1, N + 1):
        coeffs.append({-k: inv_sqrt2, k: inv_sqrt2})
    return coeffs


def _terms(i: int, j: int) -> List[Tuple[str, int, mp.mpc]]:
    """Return exponential/w-exponential terms for B_ij(w)."""
    ci = {0: mp.mpf(1)} if i == 0 else {
        -i: 1 / mp.sqrt(2),
        i: 1 / mp.sqrt(2),
    }
    cj = {0: mp.mpf(1)} if j == 0 else {
        -j: 1 / mp.sqrt(2),
        j: 1 / mp.sqrt(2),
    }
    out: List[Tuple[str, int, mp.mpc]] = []
    for m, cm in ci.items():
        for n, cn in cj.items():
            base = cm * cn
            d = m - n
            if d == 0:
                out.append(("w", n, base))
            else:
                factor = base / (2j * mp.pi * d)
                out.append(("e", m, factor))
                out.append(("e", n, -factor))
    return out


def bilinear_block_entry(i: int, j: int, w: mp.mpf) -> mp.mpf:
    """Exact finite Fourier evaluation of B_ij(w)."""
    value = mp.mpc(0)
    for kind, alpha, coeff in _terms(i, j):
        phase = mp.exp(2j * mp.pi * alpha * w)
        if kind == "w":
            value += coeff * w * phase
        else:
            value += coeff * phase
    return mp.re(value)


def bilinear_block(N: int, w: mp.mpf) -> mp.matrix:
    B = mp.matrix(N + 1, N + 1)
    for i in range(N + 1):
        for j in range(N + 1):
            B[i, j] = bilinear_block_entry(i, j, w)
    return (B + B.T) / 2


def _exp_integral(A: mp.mpf, alpha: int) -> mp.mpc:
    """Integral of exp(-A(1-w)) exp(2 pi i alpha w) on [0,1]."""
    nu = A + 2j * mp.pi * alpha
    if nu == 0:
        return mp.mpf(1)
    return (mp.e ** (2j * mp.pi * alpha) - mp.e ** (-A)) / nu


def _w_exp_integral(A: mp.mpf, alpha: int) -> mp.mpc:
    """Integral of w exp(-A(1-w)) exp(2 pi i alpha w) on [0,1]."""
    nu = A + 2j * mp.pi * alpha
    if nu == 0:
        return mp.mpf("0.5")
    return (
        mp.e ** (2j * mp.pi * alpha) * (nu - 1) + mp.e ** (-A)
    ) / (nu * nu)


def integrated_bilinear_entry(i: int, j: int, A: mp.mpf) -> mp.mpf:
    """Exact finite Fourier evaluation of int exp(-A(1-w)) B_ij(w) dw."""
    value = mp.mpc(0)
    for kind, alpha, coeff in _terms(i, j):
        integral = (
            _w_exp_integral(A, alpha)
            if kind == "w"
            else _exp_integral(A, alpha)
        )
        value += coeff * integral
    return mp.re(value)


def archimedean_matrix(
    c: int, N: int, n_terms: int = 1000, dps: int = 60
) -> mp.matrix:
    """Numerically evaluate the exact archimedean series through n_terms."""
    if c <= 1 or N < 0 or n_terms <= 0:
        raise ValueError("require c > 1, N >= 0, and n_terms > 0")

    mp.mp.dps = dps
    L = mp.log(c)
    h0 = mp.re(mp.digamma(mp.mpf("0.25"))) - mp.log(mp.pi)

    # K_ij(1)=2 delta_ij for the orthonormal cosine basis.
    A = h0 * mp.eye(N + 1)

    for n in range(n_terms):
        a = mp.mpf(n) + mp.mpf("0.25")
        decay = 2 * L * a
        for i in range(N + 1):
            for j in range(N + 1):
                K1 = 2 if i == j else 0
                integral_K = 2 * integrated_bilinear_entry(i, j, decay)
                A[i, j] += K1 / (2 * a) - L * integral_K

    return (A + A.T) / 2


def pole_neutral_nullspace(c: int, N: int) -> mp.matrix:
    """Return an orthonormal Euclidean basis for M0=0 and g(i/2)=0."""
    beta = mp.log(c) / (4 * mp.pi)
    C = mp.matrix(2, N + 1)
    C[0, 0] = 1 / beta**2
    C[1, 0] = 1
    for k in range(1, N + 1):
        C[0, k] = mp.sqrt(2) / (k * k + beta**2)
        C[1, k] = mp.sqrt(2)

    # Small dimensions used by the experiment; QR/SVD is deliberately kept
    # in the analysis layer rather than treated as a proof of positivity.
    _, _, V = mp.svd_r(C)
    return V[2:, :].T


def restricted_matrix(A: mp.matrix, c: int) -> mp.matrix:
    Z = pole_neutral_nullspace(c, A.rows - 1)
    return (Z.T * A * Z + (Z.T * A * Z).T) / 2


if __name__ == "__main__":
    c, N = 20, 3
    A = archimedean_matrix(c, N, n_terms=3000, dps=50)
    print(f"c={c} N={N} n_terms=3000")
    print("archimedean_matrix=")
    for row in A.tolist():
        print([mp.nstr(x, 16) for x in row])

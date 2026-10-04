"""Odd sine-basis diagnostic for the localized Prime-Weil block.

This module derives the arithmetic translation block directly in the physical
odd parity sector.  It deliberately does NOT import or transform the existing
cosine/even matrices.

Basis on w in [0,1]:
    psi_k(w) = sqrt(2) sin(2*pi*k*w),  k=1,...,N.

Under y=L(w-1/2), reflection y -> -y is w -> 1-w and
psi_k(1-w) = -psi_k(w), so this is genuinely odd in physical y.

The diagnostic establishes only the finite arithmetic block and the automatic
zero-mean identity M0=0.  The second pole-neutral condition, the archimedean
block, and the normalization bridge remain open.

No RH claim is made.
"""

from __future__ import annotations

import math
from typing import List, Tuple

import mpmath as mp


def _sine_terms(k: int) -> dict[int, mp.mpc]:
    """Exponential coefficients of sqrt(2) sin(2*pi*k*w)."""
    if k < 1:
        raise ValueError("sine index must be >= 1")
    # sqrt(2) * sin(theta) = (e^{i theta} - e^{-i theta})/(sqrt(2)*i)
    return {
        k: 1 / (mp.sqrt(2) * 1j),
        -k: -1 / (mp.sqrt(2) * 1j),
    }


def sine_bilinear_entry(i: int, j: int, w: mp.mpf) -> mp.mpf:
    """Exact finite Fourier evaluation of int_0^w psi_i(t) psi_j(t) dt."""
    ci = _sine_terms(i)
    cj = _sine_terms(j)
    value = mp.mpc(0)
    for m, cm in ci.items():
        for n, cn in cj.items():
            base = cm * cn
            d = m - n
            if d == 0:
                value += base * w * mp.exp(2j * mp.pi * n * w)
            else:
                factor = base / (2j * mp.pi * d)
                value += factor * (
                    mp.exp(2j * mp.pi * m * w)
                    - mp.exp(2j * mp.pi * n * w)
                )
    return mp.re(value)


def prime_powers(c: int) -> List[Tuple[int, int]]:
    out: List[Tuple[int, int]] = []
    for p in range(2, c + 1):
        if all(p % d for d in range(2, int(math.isqrt(p)) + 1)):
            q = p
            while q <= c:
                out.append((q, p))
                if q > c // p:
                    break
                q *= p
    return sorted(out)


def odd_sine_prime_matrix(c: int, N: int, dps: int = 60) -> mp.matrix:
    """Exact finite prime-power translation block in the odd sine basis."""
    if c <= 1 or N < 1:
        raise ValueError("require c > 1 and N >= 1")
    mp.mp.dps = dps
    L = mp.log(c)
    H = mp.matrix(N, N)
    for q, p in prime_powers(c):
        w = 1 - mp.log(q) / L
        weight = -2 * mp.log(p) / mp.sqrt(q)
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                H[i - 1, j - 1] += weight * sine_bilinear_entry(i, j, w)
    return (H + H.T) / 2


def mean_functional(N: int, dps: int = 60) -> mp.matrix:
    """Coefficient row for integral_0^1 sum v_k psi_k(w) dw."""
    mp.mp.dps = dps
    return mp.matrix([[mp.quad(lambda x, k=k: mp.sqrt(2) * mp.sin(2 * mp.pi * k * x), [0, 1])
                      for k in range(1, N + 1)]])


def audit(c: int = 20, N: int = 6, dps: int = 60) -> dict:
    mp.mp.dps = dps
    M0 = mean_functional(N, dps)
    P = odd_sine_prime_matrix(c, N, dps)
    asym = max(abs(P[i, j] - P[j, i]) for i in range(N) for j in range(N))
    m0_max = max(abs(M0[0, j]) for j in range(N))
    return {
        "c": c,
        "N": N,
        "M0_max_abs": m0_max,
        "prime_matrix_max_asymmetry": asym,
        "min_eigenvalue": min(mp.eigsy(P, eigvals_only=True)),
        "classification": "DISCOVERY / ODD-SECTOR ARITHMETIC BLOCK ONLY",
    }


if __name__ == "__main__":
    result = audit()
    for key, value in result.items():
        print(f"{key} = {mp.nstr(value, 18) if isinstance(value, mp.mpf) else value}")

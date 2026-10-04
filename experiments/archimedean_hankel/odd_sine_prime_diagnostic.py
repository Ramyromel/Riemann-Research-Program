"""Physical odd-channel prime translation diagnostic.

The earlier prototype integrated a same-point product on a truncated interval.
That is NOT the physical translated operator.  This version derives the
arithmetic block directly from the localized physical shift

    (S_r f)(x) = 1_{(-1,1)}(x+r) f(x+r),

with r = log(q)/a and a = log(c)/2.

Use the orthonormal odd basis phi_k(x)=sin(k*pi*x), k>=1, on (-1,1).
For a prime power q=p^m the operator contribution is

    -(Lambda(q)/sqrt(q)) (S_r + S_r^*).

This is a normalization-corrected arithmetic diagnostic only.  The
Archimedean/core terms, polar rank-one term, and full physical normalization
are not yet assembled here.
"""

from __future__ import annotations

import math
from typing import List, Tuple

import mpmath as mp


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


def _cos_integral(A: mp.mpf, phase: mp.mpf, lo: mp.mpf, hi: mp.mpf) -> mp.mpf:
    if A == 0:
        return (hi - lo) * mp.cos(phase)
    return (mp.sin(A * hi + phase) - mp.sin(A * lo + phase)) / A


def shifted_entry(i: int, j: int, r: mp.mpf) -> mp.mpf:
    """Exact integral <phi_i, S_r phi_j> for r in [0,2]."""
    lo = mp.mpf(-1)
    hi = mp.mpf(1) - r
    if hi <= lo:
        return mp.mpf(0)

    pi = mp.pi
    A_minus = pi * (i - j)
    A_plus = pi * (i + j)

    # sin(i*pi*x) sin(j*pi*(x+r))
    # = 1/2 [cos((i-j)pi*x - j*pi*r)
    #         - cos((i+j)pi*x + j*pi*r)].
    first = _cos_integral(A_minus, -j * pi * r, lo, hi)
    second = _cos_integral(A_plus, j * pi * r, lo, hi)
    return mp.mpf("0.5") * (first - second)


def physical_prime_matrix(c: int, N: int, dps: int = 60) -> mp.matrix:
    if c <= 1 or N < 1:
        raise ValueError("require c > 1 and N >= 1")
    mp.mp.dps = dps
    a = mp.log(c) / 2
    P = mp.matrix(N, N)

    for q, p in prime_powers(c):
        r = mp.log(q) / a
        weight = -mp.log(p) / mp.sqrt(q)
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                P[i - 1, j - 1] += weight * (
                    shifted_entry(i, j, r) + shifted_entry(j, i, r)
                )

    return (P + P.T) / 2


def audit(c: int = 20, N: int = 6, dps: int = 60) -> dict:
    mp.mp.dps = dps
    P = physical_prime_matrix(c, N, dps)

    # Independent symmetry check and exact endpoint check for the translation.
    asym = max(abs(P[i, j] - P[j, i]) for i in range(N) for j in range(N))
    endpoint = shifted_entry(1, 1, mp.mpf(2))

    return {
        "c": c,
        "N": N,
        "physical_translation_max_asymmetry": asym,
        "shift_endpoint_entry": endpoint,
        "min_eigenvalue": min(mp.eigsy(P, eigvals_only=True)),
        "classification": "DERIVED / CI-VERIFIED PHYSICAL ODD ARITHMETIC BLOCK ONLY",
    }


if __name__ == "__main__":
    result = audit()
    for key, value in result.items():
        print(f"{key} = {mp.nstr(value, 18) if isinstance(value, mp.mpf) else value}")

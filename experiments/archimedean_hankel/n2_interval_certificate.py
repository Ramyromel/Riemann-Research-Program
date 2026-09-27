"""Interval enclosure for the N=2 pole-neutral Prime+Archimedean scalar.

This module removes the previous precision-stability guard and encloses the
finite resolvent sum with mpmath.iv interval arithmetic.  The digamma value
at 1/4 is replaced by the exact identity

    h_+(0) = -gamma - pi/2 - log(8*pi).

Euler's constant is enclosed by its positive-term series
    gamma = sum_{n>=1} (1/n - log(1+1/n)),
with tail <= 1/(2*N) after N terms.

The omitted Archimedean resolvent tail is bounded analytically by

    |R| <= M2/(8 L^2) * sum_{n>=N_T} (n+1/4)^(-3),

and the last sum is bounded without polygamma by
    1/(N_T+1/4)^3 + 1/(2*(N_T+1/4)^2).

The result is a genuine interval enclosure of the implemented finite
expression plus a rigorous tail enclosure, subject to the correctness of the
underlying interval-arithmetic library.  It is not a proof of global Weil
positivity or RH.
"""

from __future__ import annotations

import math
from typing import Iterable

import mpmath as mp

from archimedean_hankel import _terms, fourier_l1_second_derivative_bound
from sum_level_hankel import prime_powers


def gamma_interval(n_terms: int = 2000):
    if n_terms < 1:
        raise ValueError("n_terms must be positive")
    s = mp.iv.mpf("0")
    for n in range(1, n_terms + 1):
        nn = mp.iv.mpf(n)
        s += 1 / nn - mp.iv.log(1 + 1 / nn)
    # 0 < tail < 1/(2*n_terms)
    return s + mp.iv.mpf([0, 1 / (2 * n_terms)])


def h0_interval(gamma_terms: int = 2000):
    gamma = gamma_interval(gamma_terms)
    return -gamma - mp.iv.pi / 2 - mp.iv.log(8 * mp.iv.pi)


def _coeffs(k: int):
    if k == 0:
        return {0: mp.iv.mpf(1)}
    s2 = mp.iv.sqrt(2)
    return {-k: 1 / s2, k: 1 / s2}


def _terms_iv(i: int, j: int):
    ci, cj = _coeffs(i), _coeffs(j)
    out = []
    for m, cm in ci.items():
        for n, cn in cj.items():
            base = cm * cn
            d = m - n
            if d == 0:
                out.append(("w", n, base))
            else:
                out.append(("e", m, base / (2j * mp.iv.pi * d)))
                out.append(("e", n, -base / (2j * mp.iv.pi * d)))
    return out


def _exp_integral_iv(A, alpha: int):
    nu = A + 2j * mp.iv.pi * alpha
    return (1 - mp.iv.exp(-A)) / nu


def _w_exp_integral_iv(A, alpha: int):
    nu = A + 2j * mp.iv.pi * alpha
    return ((nu - 1) + mp.iv.exp(-A)) / (nu * nu)


def integrated_bilinear_entry_iv(i: int, j: int, A):
    value = mp.iv.mpc(0)
    for kind, alpha, coeff in _terms_iv(i, j):
        value += coeff * (
            _w_exp_integral_iv(A, alpha)
            if kind == "w"
            else _exp_integral_iv(A, alpha)
        )
    return mp.iv.re(value)


def archimedean_scalar_matrix_iv(c: int, n_terms: int):
    L = mp.iv.log(c)
    A = [[mp.iv.mpf(0) for _ in range(3)] for _ in range(3)]
    h0 = h0_interval()
    for i in range(3):
        A[i][i] = h0

    for n in range(n_terms):
        a = mp.iv.mpf(n) + mp.iv.mpf("0.25")
        decay = 2 * L * a
        for i in range(3):
            for j in range(3):
                K1 = 2 if i == j else 0
                A[i][j] += mp.iv.mpf(K1) / (2 * a) - 2 * L * integrated_bilinear_entry_iv(i, j, decay)
    return A


def null_vector_iv(c: int):
    beta = mp.iv.log(c) / (4 * mp.iv.pi)
    row0 = [
        1 / beta**2,
        mp.iv.sqrt(2) / (1 + beta**2),
        mp.iv.sqrt(2) / (4 + beta**2),
    ]
    row1 = [mp.iv.mpf(1), mp.iv.sqrt(2), mp.iv.sqrt(2)]
    # Cross product of the two exact constraint rows.
    return [
        row0[1] * row1[2] - row0[2] * row1[1],
        row0[2] * row1[0] - row0[0] * row1[2],
        row0[0] * row1[1] - row0[1] * row1[0],
    ]


def prime_matrix_iv(c: int):
    L = mp.iv.log(c)
    H = [[mp.iv.mpf(0) for _ in range(3)] for _ in range(3)]
    for q, _ in prime_powers(c):
        # Recompute Lambda(q)=log(p) from the integer prime-power factor.
        p = q
        while p > 1:
            # q is a prime power; find its prime base.
            found = False
            for d in range(2, int(math.isqrt(p)) + 1):
                if p % d == 0:
                    p = d
                    found = True
                    break
            if not found:
                break
        lam = mp.iv.log(p)
        w = 1 - mp.iv.log(q) / L
        B = [[mp.iv.mpf(0) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                value = mp.iv.mpc(0)
                for m, cm in _terms_iv(i, j):
                    D = w if m == 0 else (mp.iv.exp(2j * mp.iv.pi * m * w) - 1) / (2j * mp.iv.pi * m)
                    # The expression above is the same finite Fourier formula
                    # used by the exact implementation.
                    value += cm * D
                # Rebuild B using the full (m,n) convolution to avoid ambiguity.
                value = mp.iv.mpc(0)
                ci, cj = _coeffs(i), _coeffs(j)
                for m, cm in ci.items():
                    for n, cn in cj.items():
                        d = m - n
                        D = w if d == 0 else (mp.iv.exp(2j * mp.iv.pi * d * w) - 1) / (2j * mp.iv.pi * d)
                        value += cm * cn * mp.iv.exp(2j * mp.iv.pi * n * w) * D
                B[i][j] = mp.iv.re(value)
        weight = -2 * lam / mp.iv.sqrt(q)
        for i in range(3):
            for j in range(3):
                H[i][j] += weight * B[i][j]
    return H


def second_order_tail_bound_iv(c: int, n_terms: int):
    L = mp.iv.log(c)
    sq = mp.iv.mpf(0)
    for i in range(3):
        for j in range(3):
            b = fourier_l1_second_derivative_bound(i, j)
            sq += mp.iv.mpf(str(b)) ** 2
    fro = mp.iv.sqrt(sq)
    x = mp.iv.mpf(n_terms) + mp.iv.mpf("0.25")
    cubic = 1 / x**3 + 1 / (2 * x**2)
    return fro / (8 * L**2) * cubic


def scalar_interval_certificate(c: int = 20, n_terms: int = 1000, dps: int = 80):
    mp.iv.dps = dps
    A = archimedean_scalar_matrix_iv(c, n_terms)
    P = prime_matrix_iv(c)
    w = null_vector_iv(c)

    num = mp.iv.mpf(0)
    den = mp.iv.mpf(0)
    for i in range(3):
        den += w[i] * w[i]
        for j in range(3):
            num += w[i] * (A[i][j] + P[i][j]) * w[j]
    finite = num / den
    tail = second_order_tail_bound_iv(c, n_terms)
    corrected = finite + mp.iv.mpf([-1, 1]) * tail
    return finite, tail, corrected


if __name__ == "__main__":
    finite, tail, corrected = scalar_interval_certificate()
    print("finite =", finite)
    print("tail   =", tail)
    print("corrected =", corrected)

"""Interval enclosure for the N=2 pole-neutral Prime+Archimedean scalar.

The finite resolvent sum is enclosed with mpmath.iv interval arithmetic.
The archimedean constant uses the exact identity

    h_+(0) = -gamma - pi/2 - log(8*pi).

Euler's constant is bounded with the alternating Euler--Maclaurin expansion
for H_n - log(n), avoiding the wide 1/(2N) tail of the elementary series.

The omitted Archimedean resolvent tail is bounded by

    |R| <= M2/(8 L^2) * sum_{n>=N_T} (n+1/4)^(-3),

with the final sum bounded by
    1/(N_T+1/4)^3 + 1/(2*(N_T+1/4)^2).

This is an interval certificate for the implemented finite expression plus
the analytic truncation envelope; it is not a proof of global Weil
positivity or RH.
"""

from __future__ import annotations

import math
import mpmath as mp

from archimedean_hankel import fourier_l1_second_derivative_bound
from sum_level_hankel import prime_powers


def gamma_interval(n: int = 1000):
    """Enclose gamma using alternating Euler--Maclaurin corrections."""
    if n < 10:
        raise ValueError("n must be at least 10")
    h = mp.iv.mpf(0)
    for k in range(1, n + 1):
        h += mp.iv.mpf(1) / k
    x = mp.iv.mpf(n)
    base = h - mp.iv.log(x) - 1 / (2 * x)

    # gamma = base + 1/(12n^2) - 1/(120n^4) + 1/(252n^6) - ...
    # For n >= 10 the displayed corrections decrease in magnitude.
    terms = [
        1 / (12 * x**2),
        -1 / (120 * x**4),
        1 / (252 * x**6),
        -1 / (240 * x**8),
    ]
    s = base + terms[0] + terms[1] + terms[2]
    next_term = terms[3]
    lo = s + next_term
    hi = s
    return mp.iv.mpf([lo.a, hi.b])


def h0_interval():
    gamma = gamma_interval()
    return -gamma - mp.iv.pi / 2 - mp.iv.log(8 * mp.iv.pi)


def _coeffs(k: int):
    if k == 0:
        return {0: mp.iv.mpf(1)}
    s2 = mp.iv.sqrt(2)
    return {-k: 1 / s2, k: 1 / s2}


def _terms(i: int, j: int):
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


def _integrated_entry(i: int, j: int, A):
    value = mp.iv.mpc(0)
    for kind, alpha, coeff in _terms(i, j):
        nu = A + 2j * mp.iv.pi * alpha
        if kind == "w":
            integral = ((nu - 1) + mp.iv.exp(-A)) / (nu * nu)
        else:
            integral = (1 - mp.iv.exp(-A)) / nu
        value += coeff * integral
    return mp.iv.re(value)


def archimedean_matrix_iv(c: int, n_terms: int):
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
                k1 = 2 if i == j else 0
                A[i][j] += mp.iv.mpf(k1) / (2 * a) - 2 * L * _integrated_entry(i, j, decay)
    return A


def null_vector_iv(c: int):
    beta = mp.iv.log(c) / (4 * mp.iv.pi)
    r0 = [
        1 / beta**2,
        mp.iv.sqrt(2) / (1 + beta**2),
        mp.iv.sqrt(2) / (4 + beta**2),
    ]
    r1 = [mp.iv.mpf(1), mp.iv.sqrt(2), mp.iv.sqrt(2)]
    return [
        r0[1] * r1[2] - r0[2] * r1[1],
        r0[2] * r1[0] - r0[0] * r1[2],
        r0[0] * r1[1] - r0[1] * r1[0],
    ]


def prime_matrix_iv(c: int):
    L = mp.iv.log(c)
    H = [[mp.iv.mpf(0) for _ in range(3)] for _ in range(3)]

    for q, _lam in prime_powers(c):
        p = q
        for d in range(2, int(math.isqrt(p)) + 1):
            if p % d == 0:
                p = d
                break
        lam = mp.iv.log(p)
        w = 1 - mp.iv.log(q) / L

        B = [[mp.iv.mpf(0) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            ci = _coeffs(i)
            for j in range(3):
                cj = _coeffs(j)
                value = mp.iv.mpc(0)
                for m, cm in ci.items():
                    for n, cn in cj.items():
                        d = m - n
                        D = (
                            w
                            if d == 0
                            else (mp.iv.exp(2j * mp.iv.pi * d * w) - 1)
                            / (2j * mp.iv.pi * d)
                        )
                        value += (
                            cm * cn * mp.iv.exp(2j * mp.iv.pi * n * w) * D
                        )
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
    cubic_tail = 1 / x**3 + 1 / (2 * x**2)
    return fro / (8 * L**2) * cubic_tail


def scalar_interval_certificate(c: int = 20, n_terms: int = 1000, dps: int = 70):
    mp.iv.dps = dps
    A = archimedean_matrix_iv(c, n_terms)
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
    print("tail =", tail)
    print("tail-corrected =", corrected)

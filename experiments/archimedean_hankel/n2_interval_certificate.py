"""Interval enclosure for the N=2 pole-neutral finite Weil scalar.

This is a genuine interval-arithmetic audit of the truncated scalar. It uses
mpmath.iv directed interval arithmetic, the exact Fourier/Hankel formulas
already derived in the repository, and a conservative analytic second-order
resolvent-tail envelope. It uses no zeta-zero data.

The certificate is local to (c,N)=(20,2); it is not a proof of RH.
"""

from __future__ import annotations
import math
import mpmath as mp

def _iv(x):
    return mp.iv.mpf(str(x))

def _terms(i, j):
    s2 = mp.iv.sqrt(_iv(2))
    ci = {0: _iv(1)} if i == 0 else {-i: 1 / s2, i: 1 / s2}
    cj = {0: _iv(1)} if j == 0 else {-j: 1 / s2, j: 1 / s2}
    out = []
    for m, cm in ci.items():
        for n, cn in cj.items():
            base = cm * cn
            d = m - n
            if d == 0:
                out.append(("w", n, base))
            else:
                factor = base / (2j * mp.iv.pi * d)
                out.append(("e", m, factor))
                out.append(("e", n, -factor))
    return out

def _exp_integral(A, alpha):
    nu = A + 2j * mp.iv.pi * alpha
    return (mp.iv.exp(2j * mp.iv.pi * alpha) - mp.iv.exp(-A)) / nu

def _w_exp_integral(A, alpha):
    nu = A + 2j * mp.iv.pi * alpha
    return (mp.iv.exp(2j * mp.iv.pi * alpha) * (nu - 1) + mp.iv.exp(-A)) / (nu * nu)

def _integrated_entry(i, j, A):
    value = mp.iv.mpc(0)
    for kind, alpha, coeff in _terms(i, j):
        integral = _w_exp_integral(A, alpha) if kind == "w" else _exp_integral(A, alpha)
        value += coeff * integral
    return mp.iv.re(value)

def _bilinear_entry(i, j, w):
    value = mp.iv.mpc(0)
    for kind, alpha, coeff in _terms(i, j):
        phase = mp.iv.exp(2j * mp.iv.pi * alpha * w)
        value += coeff * (w * phase if kind == "w" else phase)
    return mp.iv.re(value)

def archimedean_matrix_iv(c, N, n_terms):
    if c <= 1 or N < 0 or n_terms < 1:
        raise ValueError("require c > 1, N >= 0, n_terms >= 1")
    L = mp.iv.log(_iv(c))
    # psi(1/4) = -gamma - pi/2 - 3 log(2).
    h0 = -mp.iv.euler - mp.iv.pi / 2 - 3 * mp.iv.log(_iv(2)) - mp.iv.log(mp.iv.pi)
    A = [[h0 if i == j else _iv(0) for j in range(N + 1)] for i in range(N + 1)]
    for n in range(n_terms):
        a = _iv(n) + _iv("0.25")
        decay = 2 * L * a
        for i in range(N + 1):
            for j in range(N + 1):
                K1 = _iv(2) if i == j else _iv(0)
                A[i][j] += K1 / (2 * a) - 2 * L * _integrated_entry(i, j, decay)
    return A

def _prime_powers(c):
    out = []
    for p in range(2, c + 1):
        if all(p % d for d in range(2, int(math.isqrt(p)) + 1)):
            q = p
            while q <= c:
                out.append((q, p))
                if q > c // p:
                    break
                q *= p
    return sorted(out)

def prime_matrix_iv(c, N):
    L = mp.iv.log(_iv(c))
    H = [[_iv(0) for _ in range(N + 1)] for _ in range(N + 1)]
    for q, p in _prime_powers(c):
        w = _iv(1) - mp.iv.log(_iv(q)) / L
        lam = mp.iv.log(_iv(p))
        weight = -2 * lam / mp.iv.sqrt(_iv(q))
        B = [[_bilinear_entry(i, j, w) for j in range(N + 1)] for i in range(N + 1)]
        for i in range(N + 1):
            for j in range(N + 1):
                H[i][j] += weight * B[i][j]
    return H

def pole_neutral_vector_iv(c):
    L = mp.iv.log(_iv(c))
    beta = L / (4 * mp.iv.pi)
    s2 = mp.iv.sqrt(_iv(2))
    a0 = 1 / beta**2
    a1 = s2 / (1 + beta**2)
    a2 = s2 / (4 + beta**2)
    b0, b1, b2 = _iv(1), s2, s2
    det = a0 * b1 - a1 * b0
    rhs0, rhs1 = -a2, -b2
    v0 = (rhs0 * b1 - a1 * rhs1) / det
    v1 = (a0 * rhs1 - rhs0 * b0) / det
    return [v0, v1, _iv(1)]

def scalar_interval(c=20, n_terms=1000, dps=70):
    mp.iv.dps = dps
    A = archimedean_matrix_iv(c, 2, n_terms)
    P = prime_matrix_iv(c, 2)
    v = pole_neutral_vector_iv(c)
    numerator = _iv(0)
    denominator = _iv(0)
    for i in range(3):
        denominator += v[i] * v[i]
        for j in range(3):
            numerator += v[i] * (A[i][j] + P[i][j]) * v[j]
    return numerator / denominator

def _second_derivative_bound_iv(i, j):
    total = _iv(0)
    for kind, alpha, coeff in _terms(i, j):
        cabs = abs(coeff)
        k = 2 * mp.iv.pi * abs(alpha)
        if kind == "w":
            total += cabs * (2 * k + k * k)
        else:
            total += cabs * k * k
    return 2 * total

def second_order_tail_bound_iv(c=20, N=2, n_terms=1000):
    L = mp.iv.log(_iv(c))
    fro_sq = _iv(0)
    for i in range(N + 1):
        for j in range(N + 1):
            b = _second_derivative_bound_iv(i, j)
            fro_sq += b * b
    m_fro = mp.iv.sqrt(fro_sq)
    # Sum_{n>=T}(n+1/4)^(-3) <= 1/[2(T-3/4)^2], T>=1.
    T = _iv(n_terms)
    cubic_tail = 1 / (2 * (T - _iv("0.75")) ** 2)
    return m_fro / (8 * L * L) * cubic_tail

def corrected_lower_bound(c=20, n_terms=1000, dps=70):
    finite = scalar_interval(c, n_terms, dps)
    tail = second_order_tail_bound_iv(c, 2, n_terms)
    return finite, tail, finite.a - tail.b

if __name__ == "__main__":
    finite, tail, lower = corrected_lower_bound()
    print("N=2 interval certificate")
    print("finite_interval =", finite)
    print("tail_upper =", tail.b)
    print("corrected_lower =", lower)
    print("CERTIFIED_POSITIVE =", lower > 0)

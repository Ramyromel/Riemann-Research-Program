"""N=3 restricted Archimedean tail-structure audit.

This experiment strengthens the generic Frobenius tail envelope by combining
the finite Fourier coefficients *after* restriction to the exact
two-dimensional pole-neutral basis. It is still a discovery/audit tool:
the bound is rigorous as an envelope, but positivity is certified only if
the resulting matrix enclosure proves positive semidefiniteness.

No zeta-zero data are used.
"""

from __future__ import annotations

from collections import defaultdict
import math
import mpmath as mp

from archimedean_hankel import archimedean_matrix


def _prime_powers(c: int):
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


def _terms(i: int, j: int):
    s2 = mp.sqrt(2)
    ci = {0: mp.mpf(1)} if i == 0 else {-i: 1 / s2, i: 1 / s2}
    cj = {0: mp.mpf(1)} if j == 0 else {-j: 1 / s2, j: 1 / s2}
    out = []
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


def pole_neutral_basis(c: int) -> mp.matrix:
    beta = mp.log(c) / (4 * mp.pi)
    s2 = mp.sqrt(2)
    C = mp.matrix(
        [
            [
                1 / beta**2,
                s2 / (1 + beta**2),
                s2 / (4 + beta**2),
                s2 / (9 + beta**2),
            ],
            [1, s2, s2, s2],
        ]
    )
    M = mp.matrix([[C[0, 0], C[0, 1]], [C[1, 0], C[1, 1]]])
    raw = []
    for free in (2, 3):
        v = mp.matrix(4, 1)
        v[free] = 1
        sol = M**-1 * mp.matrix([-C[0, free], -C[1, free]])
        v[0], v[1] = sol[0], sol[1]
        raw.append(v)

    basis = []
    for v in raw:
        for q in basis:
            v -= q * (q.T * v)[0]
        basis.append(v / mp.sqrt((v.T * v)[0]))

    Z = mp.matrix(4, 2)
    for j, v in enumerate(basis):
        for i in range(4):
            Z[i, j] = v[i]
    return Z


def _combined_terms(v, w):
    """Combine all finite Fourier terms for K_{v,w} before taking abs."""
    w_terms = defaultdict(lambda: mp.mpc(0))
    e_terms = defaultdict(lambda: mp.mpc(0))
    for i, vi in enumerate(v):
        for j, wj in enumerate(w):
            factor = vi * wj
            for kind, alpha, coeff in _terms(i, j):
                target = w_terms if kind == "w" else e_terms
                target[alpha] += factor * coeff
    return w_terms, e_terms


def second_derivative_l1_bound(v, w) -> mp.mpf:
    w_terms, e_terms = _combined_terms(v, w)
    total = mp.mpf("0")
    for alpha, coeff in w_terms.items():
        k = 2 * mp.pi * abs(alpha)
        total += abs(coeff) * (2 * k + k * k)
    for alpha, coeff in e_terms.items():
        k = 2 * mp.pi * abs(alpha)
        total += abs(coeff) * k * k
    return 2 * total


def restricted_tail_frobenius_bound(c: int, T: int) -> mp.mpf:
    mp.mp.dps = 60
    Z = pole_neutral_basis(c)
    sq = mp.mpf("0")
    for a in range(2):
        va = [Z[i, a] for i in range(4)]
        for b in range(2):
            vb = [Z[i, b] for i in range(4)]
            m2 = second_derivative_l1_bound(va, vb)
            sq += m2 * m2
    return mp.sqrt(sq) / (8 * mp.log(c) ** 2) * (
        -mp.polygamma(2, mp.mpf(T) + mp.mpf("0.25")) / 2
    )


def prime_matrix(c: int) -> mp.matrix:
    L = mp.log(c)
    P = mp.zeros(4)
    for q, p in _prime_powers(c):
        w = 1 - mp.log(q) / L
        weight = -2 * mp.log(p) / mp.sqrt(q)
        for i in range(4):
            for j in range(4):
                value = mp.mpc(0)
                for kind, alpha, coeff in _terms(i, j):
                    phase = mp.exp(2j * mp.pi * alpha * w)
                    value += coeff * (w * phase if kind == "w" else phase)
                P[i, j] += weight * mp.re(value)
    return (P + P.T) / 2


def restricted_eigenvalues(c: int, T: int):
    Z = pole_neutral_basis(c)
    A = archimedean_matrix(c, 3, n_terms=T, dps=60)
    M = (Z.T * (A + prime_matrix(c)) * Z)
    M = (M + M.T) / 2
    return mp.eigsy(M, eigvals_only=True)


if __name__ == "__main__":
    for c in (10, 20, 50):
        for T in (1000, 4000, 10000):
            ev = restricted_eigenvalues(c, T)
            tail = restricted_tail_frobenius_bound(c, T)
            print(
                c,
                T,
                "lambda_min=",
                mp.nstr(ev[0], 18),
                "lambda_max=",
                mp.nstr(ev[-1], 18),
                "tail_fro=",
                mp.nstr(tail, 12),
            )

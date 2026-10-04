"""N=3 matrix-level diagnostic for the pole-neutral Prime-Weil sector.

This is deliberately a DISCOVERY experiment, not a certificate.  It uses
only arithmetic construction and the repository's exact finite
Archimedean/Hankel formulas; no zeta-zero data are used.

For N=3 the two pole-neutral constraints leave a two-dimensional space.
The diagnostic computes the two restricted eigenvalues as the Archimedean
resolvent cutoff T increases.  Near-zero movement is evidence about the
finite-to-infinite bottleneck, not a proof or counterexample to RH.
"""

from __future__ import annotations

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


def _bilinear_entry(i: int, j: int, w: mp.mpf) -> mp.mpf:
    value = mp.mpc(0)
    for kind, alpha, coeff in _terms(i, j):
        phase = mp.exp(2j * mp.pi * alpha * w)
        value += coeff * (w * phase if kind == "w" else phase)
    return mp.re(value)


def prime_matrix(c: int, N: int) -> mp.matrix:
    L = mp.log(c)
    P = mp.zeros(N + 1)
    for q, p in _prime_powers(c):
        w = 1 - mp.log(q) / L
        weight = -2 * mp.log(p) / mp.sqrt(q)
        for i in range(N + 1):
            for j in range(N + 1):
                P[i, j] += weight * _bilinear_entry(i, j, w)
    return (P + P.T) / 2


def pole_neutral_basis(c: int, N: int = 3) -> mp.matrix:
    if N != 3:
        raise NotImplementedError("The diagnostic is intentionally N=3 only.")

    beta = mp.log(c) / (4 * mp.pi)
    s2 = mp.sqrt(2)
    C = mp.matrix([
        [1 / beta**2, s2 / (1 + beta**2), s2 / (4 + beta**2), s2 / (9 + beta**2)],
        [1, s2, s2, s2],
    ])

    M = mp.matrix([[C[0, 0], C[0, 1]], [C[1, 0], C[1, 1]]])
    raw = []
    for free in (2, 3):
        v = mp.matrix(4, 1)
        v[free] = 1
        sol = M ** -1 * mp.matrix([-C[0, free], -C[1, free]])
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


def restricted_eigenvalues(c: int, T: int = 1000, dps: int = 50):
    mp.mp.dps = dps
    N = 3
    Z = pole_neutral_basis(c, N)
    M = Z.T * (archimedean_matrix(c, N, n_terms=T, dps=dps) + prime_matrix(c, N)) * Z
    M = (M + M.T) / 2
    return mp.eigsy(M, eigvals_only=True)


if __name__ == "__main__":
    for c in (10, 20, 50):
        for T in (1000, 4000):
            ev = restricted_eigenvalues(c, T=T, dps=40)
            print(c, T, *(mp.nstr(x, 14) for x in ev))

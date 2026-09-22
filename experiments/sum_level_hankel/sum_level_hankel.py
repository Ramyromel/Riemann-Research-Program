"""Exact finite sum-level/Hankel representation of the Prime–Weil block.

No zeta-zero data are used.  The implementation uses arbitrary precision
arithmetic and the real-even cosine Galerkin basis fixed by the repository.
"""

from __future__ import annotations

import cmath
import math
from typing import Dict, List, Tuple

import mpmath as mp


def prime_powers(c: int) -> List[Tuple[int, mp.mpf]]:
    """Return (q, Lambda(q)) for prime powers q <= c, sorted by q."""
    if c < 2:
        return []

    out: List[Tuple[int, mp.mpf]] = []
    for p in range(2, c + 1):
        is_prime = True
        if p < 2:
            is_prime = False
        else:
            r = int(math.isqrt(p))
            for d in range(2, r + 1):
                if p % d == 0:
                    is_prime = False
                    break
        if not is_prime:
            continue

        q = p
        while q <= c:
            out.append((q, mp.log(p)))
            if q > c // p:
                break
            q *= p

    out.sort()
    return out


def omega(q: int, c: int) -> mp.mpf:
    if not (1 < q <= c):
        raise ValueError("require 1 < q <= c")
    return 1 - mp.log(q) / mp.log(c)


def fourier_coefficients(N: int) -> List[Dict[int, mp.mpf]]:
    """Fourier coefficients of phi_0=1, phi_k=sqrt(2) cos(2 pi k t)."""
    coeffs: List[Dict[int, mp.mpf]] = [{0: mp.mpf(1)}]
    inv_sqrt2 = 1 / mp.sqrt(2)
    for k in range(1, N + 1):
        coeffs.append({-k: inv_sqrt2, k: inv_sqrt2})
    return coeffs


def D(d: int, w: mp.mpf) -> mp.mpc:
    """Integral of exp(2 pi i d t) over [0,w]."""
    if d == 0:
        return mp.mpc(w)
    return (mp.exp(2j * mp.pi * d * w) - 1) / (2j * mp.pi * d)


def bilinear_block(N: int, w: mp.mpf) -> mp.matrix:
    """Exact B_ij(w)=int_0^w phi_i(t) phi_j(w-t) dt."""
    coeffs = fourier_coefficients(N)
    B = mp.matrix(N + 1, N + 1)

    for i in range(N + 1):
        for j in range(N + 1):
            value = mp.mpc(0)
            for m, cm in coeffs[i].items():
                for n, cn in coeffs[j].items():
                    value += (
                        cm
                        * cn
                        * mp.exp(2j * mp.pi * n * w)
                        * D(m - n, w)
                    )
            B[i, j] = mp.re(value)

    # The integral identity is symmetric; symmetrization only removes
    # arbitrary-precision roundoff from the two algebraically equal entries.
    return (B + B.T) / 2


def prime_hankel_matrix(c: int, N: int, dps: int = 80) -> mp.matrix:
    """Return H such that Q_prime(v;c)=v^T H v."""
    if c <= 1 or N < 0:
        raise ValueError("require c > 1 and N >= 0")

    mp.mp.dps = dps
    H = mp.matrix(N + 1, N + 1)

    L = mp.log(c)
    for q, lam in prime_powers(c):
        w = 1 - mp.log(q) / L
        B = bilinear_block(N, w)
        weight = -2 * lam / mp.sqrt(q)
        H += weight * B

    return (H + H.T) / 2


def prime_quadratic_from_matrix(H: mp.matrix, v: List[mp.mpf]) -> mp.mpf:
    if H.rows != len(v) or H.cols != len(v):
        raise ValueError("dimension mismatch")
    x = mp.matrix(v)
    return mp.re((x.T * H * x)[0])


def prime_quadratic_direct(c: int, v: List[mp.mpf], dps: int = 80) -> mp.mpf:
    """Independent quadrature check of -sum w_q K_v(omega_q)."""
    if not v:
        return mp.mpf("0")
    mp.mp.dps = dps
    N = len(v) - 1

    def T(t: mp.mpf) -> mp.mpf:
        value = v[0]
        for k in range(1, N + 1):
            value += mp.sqrt(2) * v[k] * mp.cos(2 * mp.pi * k * t)
        return value

    total = mp.mpf("0")
    L = mp.log(c)
    for q, lam in prime_powers(c):
        w = 1 - mp.log(q) / L
        K = 2 * mp.quad(lambda t: T(t) * T(w - t), [0, w])
        total -= lam / mp.sqrt(q) * K

    return total


def max_abs_entry(A: mp.matrix) -> mp.mpf:
    return max(abs(A[i, j]) for i in range(A.rows) for j in range(A.cols))


if __name__ == "__main__":
    mp.mp.dps = 70
    c, N = 100, 6
    H = prime_hankel_matrix(c, N, dps=70)
    print(f"c={c} N={N} dimension={N + 1}")
    print("symmetric_residual=", max_abs_entry(H - H.T))
    v = [mp.mpf(i + 1) / 10 for i in range(N + 1)]
    qm = prime_quadratic_from_matrix(H, v)
    qd = prime_quadratic_direct(c, v, dps=70)
    print("matrix_quadratic=", mp.nstr(qm, 30))
    print("direct_quadratic=", mp.nstr(qd, 30))
    print("absolute_error=", mp.nstr(abs(qm - qd), 10))

"""Parity-correct odd Archimedean resolvent.

The physical odd sine basis satisfies
    sin(k*pi*(2w-1)) = (-1)^k sin(2*pi*k*w).
For real odd f, the Fourier transform of |F|^2 is an autocorrelation,
which is the negative of the sine convolution used by the first prototype.
After this sign correction, the resolvent matrix is conjugate to the direct
spectral matrix by D=diag((-1)^k). This module is research evidence only.
"""
from __future__ import annotations
import math
import mpmath as mp


def _terms(i: int, j: int):
    ci = {-i: 1 / (mp.sqrt(2) * 1j), i: -1 / (mp.sqrt(2) * 1j)}
    cj = {-j: 1 / (mp.sqrt(2) * 1j), j: -1 / (mp.sqrt(2) * 1j)}
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


def convolution_entry(i: int, j: int, w: mp.mpf) -> mp.mpf:
    value = mp.mpc(0)
    for kind, alpha, coeff in _terms(i, j):
        phase = mp.exp(2j * mp.pi * alpha * w)
        value += coeff * w * phase if kind == "w" else coeff * phase
    return mp.re(value)


def _exp_integral(A, alpha):
    nu = A + 2j * mp.pi * alpha
    return (mp.exp(2j * mp.pi * alpha) - mp.exp(-A)) / nu


def _w_exp_integral(A, alpha):
    nu = A + 2j * mp.pi * alpha
    return (mp.exp(2j * mp.pi * alpha) * (nu - 1) + mp.exp(-A)) / (nu * nu)


def integrated_convolution(i: int, j: int, A):
    value = mp.mpc(0)
    for kind, alpha, coeff in _terms(i, j):
        value += coeff * (
            _w_exp_integral(A, alpha)
            if kind == "w"
            else _exp_integral(A, alpha)
        )
    return mp.re(value)


def archimedean_matrix(c: int, N: int, n_terms: int = 3000, dps: int = 60):
    mp.mp.dps = dps
    L = mp.log(c)
    h0 = mp.re(mp.digamma(mp.mpf("0.25"))) - mp.log(mp.pi)
    A = h0 * mp.eye(N)
    for n in range(n_terms):
        a = mp.mpf(n) + mp.mpf("0.25")
        decay = 2 * L * a
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                K1 = 2 if i == j else 0
                # Physical autocorrelation K = -2*(sine convolution).
                A[i - 1, j - 1] += (
                    K1 / (2 * a) + 2 * L * integrated_convolution(i, j, decay)
                )
    return (A + A.T) / 2


def parity_conjugation(N: int):
    return mp.diag([(-1) ** k for k in range(1, N + 1)])

"""Certified finite-basis bound for the Archimedean resolvent tail."""
from __future__ import annotations
import mpmath as mp
from archimedean_hankel import _terms

def bilinear_derivative_entry(i, j, w):
    value = mp.mpc(0)
    for kind, alpha, coeff in _terms(i, j):
        phase = mp.exp(2j * mp.pi * alpha * w)
        if kind == "w":
            value += coeff * phase * (1 + 2j * mp.pi * alpha * w)
        else:
            value += coeff * (2j * mp.pi * alpha) * phase
    return mp.re(value)

def k_derivative_entry(i, j, w):
    return 2 * bilinear_derivative_entry(i, j, w)

def fourier_l1_derivative_bound(i, j):
    total = mp.mpf("0")
    for kind, alpha, coeff in _terms(i, j):
        cabs = abs(coeff)
        if kind == "w":
            total += cabs * (1 + 2 * mp.pi * abs(alpha))
        else:
            total += cabs * (2 * mp.pi * abs(alpha))
    return 2 * total

def matrix_tail_frobenius_bound(c, N, n_terms):
    if c <= 1 or N < 0 or n_terms < 1:
        raise ValueError("require c > 1, N >= 0, n_terms >= 1")
    L = mp.log(c)
    coeff_bound_sq = mp.mpf("0")
    for i in range(N + 1):
        for j in range(N + 1):
            b = fourier_l1_derivative_bound(i, j)
            coeff_bound_sq += b * b
    m_fro = mp.sqrt(coeff_bound_sq)
    harmonic_tail = mp.polygamma(1, mp.mpf(n_terms) + mp.mpf("0.25"))
    return m_fro / (4 * L) * harmonic_tail

def fourier_l1_second_derivative_bound(i, j):
    """Bound sup_w |K_ij''(w)| for the finite cosine basis."""
    total = mp.mpf("0")
    for kind, alpha, coeff in _terms(i, j):
        cabs = abs(coeff)
        k = 2 * mp.pi * abs(alpha)
        if kind == "w":
            # |d²[w exp(i k w)]| <= 2|k| + |k|² on [0,1].
            total += cabs * (2 * k + k * k)
        else:
            total += cabs * k * k
    return 2 * total


def pole_neutral_second_order_tail_bound(c, N, n_terms):
    """Frobenius envelope for the restricted tail using two integrations by parts.

    On M0(v)=0, T_v(0)=T_v(1)=0, hence K_v'(0)=K_v'(1)=0.
    The omitted resolvent tail therefore obeys
        |R(v)| <= M2(v)/(8 L^2) * sum_{n>=n_terms} a_n^-3.
    The returned Frobenius envelope uses the entrywise Fourier bounds for
    K_ij'' and is intentionally conservative.
    """
    if c <= 1 or N < 0 or n_terms < 1:
        raise ValueError("require c > 1, N >= 0, n_terms >= 1")
    L = mp.log(c)
    bound_sq = mp.mpf("0")
    for i in range(N + 1):
        for j in range(N + 1):
            b = fourier_l1_second_derivative_bound(i, j)
            bound_sq += b * b
    m_fro = mp.sqrt(bound_sq)
    # sum_{n=n_terms}^infinity (n+1/4)^(-3) = -1/2 psi_2(n_terms+1/4)
    cubic_tail = -mp.polygamma(2, mp.mpf(n_terms) + mp.mpf("0.25")) / 2
    return m_fro / (8 * L * L) * cubic_tail

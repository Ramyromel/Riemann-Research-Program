"""Scalar audit of the first nontrivial pole-neutral case N=2.

For N=2 the two exact pole-neutral constraints leave a one-dimensional
subspace. The restricted combined form is therefore a scalar Rayleigh
quotient, which avoids an eigenvalue solver entirely.

This module combines:
  * the exact finite prime Hankel matrix,
  * the truncated exact-Fourier Archimedean matrix,
  * the pole-neutral null vector,
  * the derived second-order Archimedean tail bound.

The resulting lower margin is a truncation-corrected arbitrary-precision
numerical audit. It is NOT an interval-arithmetic proof of the finite
floating-point evaluation; the arithmetic-stability guard is therefore
reported separately.
"""

from __future__ import annotations

import mpmath as mp

from archimedean_hankel import archimedean_matrix, pole_neutral_nullspace
from archimedean_tail_certificate import pole_neutral_second_order_tail_bound
from sum_level_hankel import prime_hankel_matrix


def scalar_restricted_value(c: int, n_terms: int, dps: int = 80) -> mp.mpf:
    """Return the N=2 restricted combined Rayleigh quotient."""
    if c <= 1 or n_terms < 1:
        raise ValueError("require c > 1 and n_terms >= 1")
    mp.mp.dps = dps
    A = archimedean_matrix(c, 2, n_terms=n_terms, dps=dps)
    P = prime_hankel_matrix(c, 2, dps=dps)
    Z = pole_neutral_nullspace(c, 2)
    w = Z[:, 0]
    return mp.re(((w.T * (A + P) * w)[0]) / ((w.T * w)[0]))


def precision_stability_guard(c: int, n_terms: int) -> mp.mpf:
    """Conservative observed arithmetic guard from two precision runs."""
    low = scalar_restricted_value(c, n_terms, dps=60)
    high = scalar_restricted_value(c, n_terms, dps=90)
    return abs(high - low) * 10


def truncation_corrected_margin(c: int, n_terms: int, dps: int = 80):
    """Return value, tail bound, arithmetic guard, and residual margin."""
    value = scalar_restricted_value(c, n_terms, dps=dps)
    tail = pole_neutral_second_order_tail_bound(c, 2, n_terms)
    guard = precision_stability_guard(c, n_terms)
    margin = value - tail - guard
    return value, tail, guard, margin


if __name__ == "__main__":
    mp.mp.dps = 90
    c, n_terms = 20, 10000
    value, tail, guard, margin = truncation_corrected_margin(c, n_terms)
    print("N=2 pole-neutral scalar audit")
    print("c =", c)
    print("n_terms =", n_terms)
    print("truncated_value =", mp.nstr(value, 30))
    print("second_order_tail_bound =", mp.nstr(tail, 30))
    print("precision_stability_guard =", mp.nstr(guard, 30))
    print("residual_margin =", mp.nstr(margin, 30))
    print("STATUS = positive numerical margin only; not interval-certified")

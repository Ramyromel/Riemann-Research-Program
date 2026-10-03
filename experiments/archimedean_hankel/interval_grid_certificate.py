"""Interval-certified grid for low-dimensional pole-neutral sectors.

This extends the audited N=2,c=20 certificate to a small explicit grid.
Every point is evaluated independently with interval arithmetic and the
same analytic second-order Archimedean tail envelope.

No zeta-zero data are used. A failed certificate is recorded as inconclusive,
not as a negative theorem.
"""

from __future__ import annotations

import mpmath as mp

from n2_interval_certificate import (
    scalar_interval,
    second_order_tail_bound_iv,
)


def run_case(c, N, n_terms=1000, dps=60):
    if N != 2:
        raise NotImplementedError(
            "The current exact pole-neutral scalar reduction is only N=2."
        )
    finite = scalar_interval(c, n_terms, dps)
    tail = second_order_tail_bound_iv(c, N, n_terms)
    lower = finite.a - tail.b
    upper = finite.b + tail.b
    return {
        "c": c,
        "N": N,
        "T": n_terms,
        "finite_lower": finite.a,
        "finite_upper": finite.b,
        "tail_upper": tail.b,
        "corrected_lower": lower,
        "corrected_upper": upper,
        "certified_positive": lower > 0,
    }


def run_grid(c_values=(10, 20, 30, 50, 100), n_terms=1000, dps=60):
    mp.iv.dps = dps
    return [run_case(c, 2, n_terms, dps) for c in c_values]


if __name__ == "__main__":
    rows = run_grid()
    print("c,N,T,finite_lower,finite_upper,tail_upper,corrected_lower,certified")
    for row in rows:
        print(
            row["c"], row["N"], row["T"],
            row["finite_lower"], row["finite_upper"],
            row["tail_upper"], row["corrected_lower"],
            row["certified_positive"],
            sep=",",
        )

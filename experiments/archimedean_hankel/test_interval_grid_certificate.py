from __future__ import annotations

import mpmath as mp

from interval_grid_certificate import run_case


def test_grid_cases_are_certified():
    mp.iv.dps = 60
    for c in (10, 20, 30, 50, 100):
        row = run_case(c, 2, 1000, 60)
        assert row["finite_upper"] > row["finite_lower"]
        assert row["tail_upper"] > 0
        assert row["certified_positive"], row


def test_grid_is_not_silently_widened_to_other_dimensions():
    try:
        run_case(20, 3, 1000, 60)
    except NotImplementedError:
        pass
    else:
        raise AssertionError("N != 2 must not be silently treated as N=2")

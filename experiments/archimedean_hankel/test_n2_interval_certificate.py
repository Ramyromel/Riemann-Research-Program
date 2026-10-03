from __future__ import annotations

import mpmath as mp

from n2_interval_certificate import (
    corrected_lower_bound,
    scalar_interval,
    second_order_tail_bound_iv,
)


def test_interval_scalar_is_positive_and_narrow():
    mp.iv.dps = 60
    value = scalar_interval(20, 1000)
    assert value.a > 0
    assert value.b > value.a
    assert value.b - value.a < mp.iv.mpf("1e-55")


def test_second_order_tail_is_conservative():
    mp.iv.dps = 60
    tail = second_order_tail_bound_iv(20, 2, 1000)
    assert tail.a > 0
    assert tail.b < mp.iv.mpf("4e-6")


def test_corrected_lower_bound_is_positive():
    mp.iv.dps = 60
    _, _, lower = corrected_lower_bound(20, 1000)
    assert lower > mp.iv.mpf("3e-5")

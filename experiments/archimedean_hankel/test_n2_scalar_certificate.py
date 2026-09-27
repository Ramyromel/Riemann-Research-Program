import unittest

import mpmath as mp

from n2_scalar_certificate import (
    precision_stability_guard,
    scalar_restricted_value,
    truncation_corrected_margin,
)


class N2ScalarAuditTests(unittest.TestCase):
    def test_scalar_value_is_reproducible(self):
        v60 = scalar_restricted_value(20, 1000, dps=60)
        v90 = scalar_restricted_value(20, 1000, dps=90)
        self.assertLess(abs(v60 - v90), mp.mpf("1e-45"))

    def test_second_order_tail_is_below_positive_margin(self):
        value, tail, guard, margin = truncation_corrected_margin(20, 1000, dps=80)
        self.assertGreater(value, 0)
        self.assertGreater(tail, 0)
        self.assertGreater(guard, 0)
        self.assertGreater(margin, mp.mpf("3e-5"))

    def test_higher_cutoff_preserves_positive_margin(self):
        value, tail, guard, margin = truncation_corrected_margin(20, 10000, dps=80)
        self.assertGreater(value, mp.mpf("3.7e-5"))
        self.assertLess(tail, mp.mpf("4e-8"))
        self.assertGreater(margin, mp.mpf("3.7e-5"))


if __name__ == "__main__":
    unittest.main()

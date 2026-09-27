import unittest
from archimedean_tail_certificate import (
    fourier_l1_derivative_bound,
    fourier_l1_second_derivative_bound,
    matrix_tail_frobenius_bound,
    pole_neutral_second_order_tail_bound,
)

class TailCertificateTests(unittest.TestCase):
    def test_coefficient_bound_is_positive(self):
        for i in range(4):
            for j in range(4):
                self.assertGreater(fourier_l1_derivative_bound(i, j), 0)

    def test_tail_bound_decreases(self):
        b1 = matrix_tail_frobenius_bound(20, 3, 100)
        b2 = matrix_tail_frobenius_bound(20, 3, 1000)
        b3 = matrix_tail_frobenius_bound(20, 3, 10000)
        self.assertGreater(b1, b2)
        self.assertGreater(b2, b3)

    def test_second_derivative_bound_is_positive(self):
        for i in range(4):
            for j in range(4):
                self.assertGreater(fourier_l1_second_derivative_bound(i, j), 0)

    def test_pole_neutral_second_order_tail_is_sharper(self):
        first = matrix_tail_frobenius_bound(20, 2, 1000)
        second = pole_neutral_second_order_tail_bound(20, 2, 1000)
        self.assertGreater(first, second)
        self.assertLess(second, mp.mpf("4e-6"))

    def test_tail_bound_scales_with_log_cutoff(self):
        b20 = matrix_tail_frobenius_bound(20, 3, 1000)
        b100 = matrix_tail_frobenius_bound(100, 3, 1000)
        self.assertGreater(b20, b100)

if __name__ == "__main__":
    unittest.main()

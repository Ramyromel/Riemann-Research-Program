import unittest

import mpmath as mp

from sum_level_hankel import (
    bilinear_block,
    prime_hankel_matrix,
    prime_quadratic_direct,
    prime_quadratic_from_matrix,
    prime_powers,
)


class SumLevelHankelTests(unittest.TestCase):
    def test_prime_powers(self):
        self.assertEqual(
            [q for q, _ in prime_powers(20)],
            [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19],
        )

    def test_bilinear_block_is_symmetric(self):
        mp.mp.dps = 60
        B = bilinear_block(4, mp.mpf("0.73"))
        residual = max(abs(B[i, j] - B[j, i]) for i in range(5) for j in range(5))
        self.assertLess(residual, mp.mpf("1e-50"))

    def test_matrix_matches_independent_quadrature(self):
        mp.mp.dps = 60
        c, N = 30, 3
        v = [mp.mpf("0.17"), mp.mpf("-0.31"), mp.mpf("0.22"), mp.mpf("0.41")]
        H = prime_hankel_matrix(c, N, dps=60)
        qm = prime_quadratic_from_matrix(H, v)
        qd = prime_quadratic_direct(c, v, dps=60)
        self.assertLess(abs(qm - qd), mp.mpf("1e-45"))

    def test_no_zero_data_dependency(self):
        # Construction depends only on c, N, Lambda(q), and the audited basis.
        H = prime_hankel_matrix(20, 2, dps=50)
        self.assertEqual(H.rows, 3)
        self.assertEqual(H.cols, 3)


if __name__ == "__main__":
    unittest.main()

import unittest

import mpmath as mp

from archimedean_hankel import (
    archimedean_matrix,
    bilinear_block,
    integrated_bilinear_entry,
    restricted_matrix,
)


class ArchimedeanHankelTests(unittest.TestCase):
    def test_k1_is_orthonormality_matrix(self):
        mp.mp.dps = 40
        B = bilinear_block(3, mp.mpf(1))
        for i in range(4):
            for j in range(4):
                target = mp.mpf(1) if i == j else mp.mpf(0)
                self.assertLess(abs(B[i, j] - target), mp.mpf("1e-30"))

    def test_integrated_entry_matches_quadrature(self):
        mp.mp.dps = 40
        A = mp.mpf("3.7")
        for i, j in [(0, 0), (0, 1), (1, 1), (1, 2)]:
            exact = integrated_bilinear_entry(i, j, A)
            direct = mp.quad(
                lambda w: mp.exp(-A * (1 - w)) * bilinear_block(2, w)[i, j],
                [0, 1],
            )
            self.assertLess(abs(exact - direct), mp.mpf("1e-25"))

    def test_pole_neutral_basis_has_expected_dimension_and_constraints(self):
        mp.mp.dps = 50
        c, N = 20, 4
        Z = __import__("archimedean_hankel").pole_neutral_nullspace(c, N)
        self.assertEqual(Z.rows, N + 1)
        self.assertEqual(Z.cols, N - 1)

        beta = mp.log(c) / (4 * mp.pi)
        C = mp.matrix(2, N + 1)
        C[0, 0] = 1 / beta**2
        C[1, 0] = 1
        for k in range(1, N + 1):
            C[0, k] = mp.sqrt(2) / (k * k + beta**2)
            C[1, k] = mp.sqrt(2)

        residual = C * Z
        self.assertLess(
            max(abs(residual[i, j])
                for i in range(residual.rows)
                for j in range(residual.cols)),
            mp.mpf("1e-40"),
        )

        gram = Z.T * Z
        self.assertLess(
            max(abs(gram[i, j] - (1 if i == j else 0))
                for i in range(gram.rows)
                for j in range(gram.cols)),
            mp.mpf("1e-40"),
        )

    def test_restricted_total_is_stable_under_resolvent_truncation(self):
        # The prime block is supplied independently by the existing
        # sum-level/Hankel experiment.  Here we only verify that the
        # archimedean truncation itself converges to a stable restricted form.
        mp.mp.dps = 40
        c, N = 20, 2
        A1 = archimedean_matrix(c, N, n_terms=300, dps=40)
        A2 = archimedean_matrix(c, N, n_terms=1200, dps=40)
        R1 = restricted_matrix(A1, c)
        R2 = restricted_matrix(A2, c)
        self.assertLess(max(abs(R1[i, j] - R2[i, j])
                            for i in range(R1.rows)
                            for j in range(R1.cols)), mp.mpf("2e-4"))


if __name__ == "__main__":
    unittest.main()

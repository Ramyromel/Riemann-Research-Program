import unittest

from prime_intersection_audit import (
    cholesky_psd,
    exponential,
    log_distance,
    overlap,
    sources,
    weighted_kernel,
    exact_affine_ratio,
)


class PrimeIntersectionAuditTests(unittest.TestCase):
    def setUp(self):
        self.src = sources(100)

    def test_affine_transform_is_exactly_trivial(self):
        ok, ratio = exact_affine_ratio(self.src)
        self.assertTrue(ok)
        self.assertAlmostEqual(ratio, 2.0, places=14)

    def test_overlap_kernel_is_psd(self):
        self.assertTrue(
            cholesky_psd(weighted_kernel(self.src, overlap))
        )

    def test_exponential_log_kernel_is_psd(self):
        self.assertTrue(
            cholesky_psd(weighted_kernel(self.src, exponential(1.0)))
        )

    def test_log_distance_is_not_psd(self):
        # Any two distinct sources give a principal block
        # [[0,d],[d,0]], whose determinant is -d^2 < 0.
        a, b = self.src[0], self.src[1]
        self.assertGreater(abs(a.log_q - b.log_q), 0.0)
        self.assertFalse(
            cholesky_psd(
                weighted_kernel([a, b], log_distance)
            )
        )


if __name__ == "__main__":
    unittest.main()

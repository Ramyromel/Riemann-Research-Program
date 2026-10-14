import sys
sys.path.insert(0, "experiments/archimedean_hankel")

from odd_sine_archimedean_resolvent_corrected import archimedean_matrix
from odd_sine_archimedean_diagnostic import arch_matrix as diagnostic_arch_matrix, K_entry
import mpmath as mp
from direct_physical_spectral_archimedean_audit import spectral_archimedean_matrix
import numpy as np


def check(c, n, R=300, nr=30001, terms=2000):
    a = 0.5 * np.log(c)
    physical = spectral_archimedean_matrix(a, n, R=R, nr=nr)
    odd = np.asarray(
        archimedean_matrix(c, n, n_terms=terms, dps=50).tolist(),
        dtype=float,
    )
    diagnostic = np.asarray(
        diagnostic_arch_matrix(c, n, n_terms=terms).tolist(), dtype=float
    )
    mp.mp.dps = 50
    endpoint_gap = max(
        abs(K_entry(i, j, mp.mpf(1)) + (1 if i == j else 0))
        for i in range(1, n + 1) for j in range(1, n + 1)
    )
    assert endpoint_gap < mp.mpf("1e-40"), (
        f"raw convolution endpoint mismatch: max gap={mp.nstr(endpoint_gap, 8)}"
    )
    implementation_gap = np.max(np.abs(diagnostic - odd))
    assert implementation_gap < 1e-10, (
        f"odd Archimedean implementations disagree: max gap={implementation_gap:.3e}"
    )
    D = np.diag([(-1) ** k for k in range(1, n + 1)])
    transported = D @ odd @ D
    d = transported - physical
    return np.linalg.norm(d), np.max(np.abs(d))


def main():
    for c, n in ((8, 2), (20, 6)):
        frob, mx = check(c, n)
        print(f"c={c} n={n} frobenius={frob:.12e} max={mx:.12e}")
        assert frob < 2e-4
        assert mx < 2e-4


if __name__ == "__main__":
    main()

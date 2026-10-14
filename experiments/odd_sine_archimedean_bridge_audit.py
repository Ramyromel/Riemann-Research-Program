"""Compare the odd Volterra resolvent candidate with the direct spectral integral.

The spectral matrix is the independently assembled reference from
h_+(r) and the exact sine transform. The candidate matrix comes from the
repository's current odd Volterra implementation. This is a diagnostic:
a mismatch blocks promotion of the resolvent identity.
"""
from __future__ import annotations
import numpy as np
from direct_physical_spectral_archimedean_audit import spectral_archimedean_matrix
from archimedean_hankel.odd_sine_archimedean_diagnostic import arch_matrix


def run(c: int = 20, n: int = 6):
    a = 0.5 * np.log(c)
    spectral = spectral_archimedean_matrix(a, n, R=500.0, nr=100001)
    candidate = np.asarray(arch_matrix(c, n, n_terms=3000).tolist(), dtype=float)
    diff = candidate - spectral
    print(f"c={c} n={n} a={a:.16g}")
    print("spectral_lambda_min=", np.linalg.eigvalsh(spectral)[0])
    print("candidate_lambda_min=", np.linalg.eigvalsh(candidate)[0])
    print("frobenius_difference=", np.linalg.norm(diff, ord="fro"))
    print("max_entry_difference=", np.max(np.abs(diff)))
    print("classification=BLOCKED_ODD_RESOLVENT_BRIDGE")


if __name__ == "__main__":
    run()

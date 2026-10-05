"""Direct physical odd Archimedean matrix audit.

This diagnostic independently discretizes the physical normalized form
H_Leg + c0(a) I + V - K_gamma,a on (-1,1) in the sine basis
phi_k(x)=sin(k*pi*x), and compares it with the repository's odd
resolvent representation.

The quadrature is deliberately diagnostic, not a certificate. A mismatch
is evidence that the normalization bridge is not yet established; it is
not a counterexample to Weil positivity or RH.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

sys.path.insert(0, str(Path(__file__).resolve().parent / "archimedean_hankel"))
from odd_sine_archimedean_diagnostic import archimedean_matrix


from physical_odd_archimedean import physical_archimedean_matrix
def run(c=20, n=6):
    a = 0.5 * math.log(c)
    direct_prev = None
    for order in (160, 240, 320, 480):
        direct = physical_archimedean_matrix(a, n, order)
        if direct_prev is not None:
            conv = np.linalg.norm(direct - direct_prev, ord="fro")
        else:
            conv = float("nan")
        direct_prev = direct
        print(f"order={order} direct_lambda_min={np.linalg.eigvalsh(direct)[0]:.15g} convergence={conv:.3e}")

    resolvent = np.asarray(archimedean_matrix(c, n, n_terms=3000, dps=50).tolist(), dtype=float)
    diff = direct - resolvent
    print("frobenius_difference=", np.linalg.norm(diff, ord="fro"))
    print("max_entry_difference=", np.max(np.abs(diff)))
    print("resolvent_lambda_min=", np.linalg.eigvalsh(resolvent)[0])
    print("classification=NUMERICAL_NORMALIZATION_MISMATCH_OPEN")


if __name__ == "__main__":
    run()

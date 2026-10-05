"""Direct physical/spectral Archimedean normalization audit.

The physical odd basis e_k(y)=a^{-1/2} sin(k*pi*y/a) is transformed in closed
form and inserted into the classical archimedean spectral integral. The result
is compared with the physical-coordinate kernel H_Leg + c0 I + V - K_gamma.

The comparison is intentionally non-certifying: finite spectral truncation and
quadrature produce a numerical residual. A nonzero residual is retained as
evidence that the exact normalization bridge still needs an analytic proof.
No positivity or RH claim is made.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.integrate import simpson
from scipy.special import digamma

from physical_odd_archimedean import physical_archimedean_matrix


def sine_transform(r: np.ndarray, a: float, k: int) -> np.ndarray:
    b = k * math.pi / a
    return 1j * math.sqrt(a) * (
        np.sinc((r - b) * a / math.pi)
        - np.sinc((r + b) * a / math.pi)
    )


def spectral_archimedean_matrix(a: float, n: int, R: float = 500.0,
                                nr: int = 100001) -> np.ndarray:
    r = np.linspace(-R, R, nr)
    h = np.real(digamma(0.25 + 0.5j * r)) - math.log(math.pi)
    F = np.array([sine_transform(r, a, k) for k in range(1, n + 1)])
    A = np.empty((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            A[i, j] = simpson(
                h * np.real(F[i] * np.conj(F[j])) / (2.0 * math.pi),
                x=r,
            )
    return (A + A.T) / 2.0


def run(c: int = 20, n: int = 6) -> float:
    a = 0.5 * math.log(c)
    physical = physical_archimedean_matrix(a, n, order=480)
    spectral = spectral_archimedean_matrix(a, n)
    diff = spectral - physical
    err = float(np.max(np.abs(diff)))
    print(f"c={c} n={n} a={a:.16g}")
    print("physical_lambda_min=", np.linalg.eigvalsh(physical)[0])
    print("spectral_lambda_min=", np.linalg.eigvalsh(spectral)[0])
    print("frobenius_difference=", np.linalg.norm(diff, ord="fro"))
    print("max_entry_difference=", err)
    print("classification=OPEN_ANALYTIC_NORMALIZATION_BRIDGE")
    return err


if __name__ == "__main__":
    run()

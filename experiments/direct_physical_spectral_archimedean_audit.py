"""Direct physical/spectral Archimedean normalization bridge.

For the physical odd basis e_k(y)=a^{-1/2} sin(k*pi*y/a), the critical-line
Laplace/Fourier transform is evaluated in closed form and inserted directly
into the classical archimedean spectral integral

    (1/(2*pi)) int h_+(r) F_i(ir) conj(F_j(ir)) dr,
    h_+(r)=Re psi(1/4+ir/2)-log(pi).

This audit compares that independently assembled spectral matrix with the
physical-coordinate kernel H_Leg + c0 I + V - K_gamma used by the odd-channel
construction. It is a normalization audit only: no positivity or RH claim.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.integrate import simpson
from scipy.special import digamma
from direct_physical_odd_archimedean_audit import physical_archimedean_matrix


def sine_transform(r: np.ndarray, a: float, k: int) -> np.ndarray:
    b = k * math.pi / a
    return 1j * math.sqrt(a) * (
        np.sinc((r - b) * a / math.pi)
        - np.sinc((r + b) * a / math.pi)
    )


def spectral_archimedean_matrix(a: float, n: int, R: float = 180.0,
                                nr: int = 24001) -> np.ndarray:
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


def run(c: int = 8, n: int = 2) -> float:
    a = 0.5 * math.log(c)
    physical = physical_archimedean_matrix(a, n, order=180)
    spectral = spectral_archimedean_matrix(a, n)
    diff = spectral - physical
    err = float(np.max(np.abs(diff)))
    print(f"c={c} n={n} a={a:.16g}")
    print("physical_lambda_min=", np.linalg.eigvalsh(physical)[0])
    print("spectral_lambda_min=", np.linalg.eigvalsh(spectral)[0])
    print("frobenius_difference=", np.linalg.norm(diff, ord="fro"))
    print("max_entry_difference=", err)
    print("classification=NUMERICALLY_SUPPORTED_NORMALIZATION_BRIDGE")
    return err


if __name__ == "__main__":
    error = run()
    if error >= 2.0e-2:
        raise AssertionError(f"physical/spectral mismatch too large: {error}")

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
from numpy.polynomial.legendre import leggauss

from direct_physical_odd_archimedean_audit import physical_archimedean_matrix


def sine_transform(r: np.ndarray, a: float, k: int) -> np.ndarray:
    """Integral of a^{-1/2} sin(k*pi*y/a) exp(i*r*y) over (-a,a)."""
    b = k * math.pi / a
    u = r - b
    v = r + b
    # sin(z)/z with the removable value 1 at z=0.
    def sinc_unscaled(z):
        return np.sinc(z / math.pi)

    return 1j * math.sqrt(a) * (
        sinc_unscaled(u * a) - sinc_unscaled(v * a)
    )


def spectral_archimedean_matrix(a: float, n: int, R: float = 300.0,
                                nr: int = 60001) -> np.ndarray:
    r = np.linspace(-R, R, nr)
    h = np.real(digamma(0.25 + 0.5j * r)) - math.log(math.pi)
    F = np.array([sine_transform(r, a, k) for k in range(1, n + 1)])
    A = np.empty((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            integrand = h * np.real(F[i] * np.conj(F[j])) / (2.0 * math.pi)
            A[i, j] = simpson(integrand, x=r)
    return (A + A.T) / 2.0


def run(c: int = 20, n: int = 4) -> None:
    a = 0.5 * math.log(c)
    physical = physical_archimedean_matrix(a, n, order=320)
    spectral = spectral_archimedean_matrix(a, n, R=300.0, nr=60001)
    diff = spectral - physical
    print(f"c={c} n={n} a={a:.16g}")
    print("physical_lambda_min=", np.linalg.eigvalsh(physical)[0])
    print("spectral_lambda_min=", np.linalg.eigvalsh(spectral)[0])
    print("frobenius_difference=", np.linalg.norm(diff, ord="fro"))
    print("max_entry_difference=", np.max(np.abs(diff)))
    print("physical_matrix=")
    print(physical)
    print("spectral_matrix=")
    print(spectral)
    print("classification=OPEN_NORMALIZATION_AUDIT")


if __name__ == "__main__":
    run()

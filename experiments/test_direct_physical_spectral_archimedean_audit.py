import numpy as np

from direct_physical_spectral_archimedean_audit import (
    physical_archimedean_matrix,
    spectral_archimedean_matrix,
)


def test_physical_spectral_bridge_is_close():
    c = 8
    n = 2
    a = 0.5 * np.log(c)
    physical = physical_archimedean_matrix(a, n, order=180)
    spectral = spectral_archimedean_matrix(a, n, R=180.0, nr=24001)
    err = np.max(np.abs(spectral - physical))
    # This is deliberately a diagnostic tolerance. The finite spectral
    # window and quadrature leave a nonzero tail error.
    assert err < 2.0e-2, err

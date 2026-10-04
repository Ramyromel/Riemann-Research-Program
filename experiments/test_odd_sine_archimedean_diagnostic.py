from odd_sine_archimedean_diagnostic import (
    _exp_integral,
    _w_exp_integral,
    bilinear_block_entry,
    endpoint_check,
    integrated_bilinear_entry,
    archimedean_matrix,
)
import mpmath as mp


def main():
    mp.mp.dps = 50

    endpoint_err = endpoint_check(6, 50)
    assert endpoint_err < mp.mpf("1e-40"), endpoint_err

    # Independent quadrature checks for the analytic finite Fourier formulas.
    w = mp.mpf("0.37")
    Adecay = mp.mpf("3.25")
    for i, j in ((1, 1), (1, 2), (2, 3)):
        direct_B = mp.quad(
            lambda t: (
                mp.sqrt(2) * mp.sin(2 * mp.pi * i * t)
                * mp.sqrt(2) * mp.sin(2 * mp.pi * j * (w - t))
            ),
            [0, w],
        )
        analytic_B = bilinear_block_entry(i, j, w)
        assert abs(direct_B - analytic_B) < mp.mpf("1e-35"), (
            i, j, direct_B, analytic_B
        )

        direct_I = mp.quad(
            lambda u: mp.exp(-Adecay * (1 - u))
            * bilinear_block_entry(i, j, u),
            [0, 1],
        )
        analytic_I = integrated_bilinear_entry(i, j, Adecay)
        assert abs(direct_I - analytic_I) < mp.mpf("1e-35"), (
            i, j, direct_I, analytic_I
        )

    A = archimedean_matrix(20, 6, n_terms=1000, dps=50)
    symmetry_err = max(
        abs(A[i, j] - A[j, i]) for i in range(6) for j in range(6)
    )
    assert symmetry_err < mp.mpf("1e-45")

    eig = mp.eigsy(A, eigvals_only=True)
    print("endpoint_K_error=", mp.nstr(endpoint_err, 20))
    print("analytic_integral_checks=PASS")
    print("symmetry_error=", mp.nstr(symmetry_err, 20))
    print("lambda_min=", mp.nstr(min(eig), 20))


if __name__ == "__main__":
    main()

from odd_sine_archimedean_diagnostic import endpoint_check, archimedean_matrix
import mpmath as mp

def main():
    err = endpoint_check(6, 50)
    assert err < mp.mpf("1e-40"), err
    A = archimedean_matrix(20, 6, n_terms=1000, dps=50)
    assert max(abs(A[i,j]-A[j,i]) for i in range(6) for j in range(6)) < mp.mpf("1e-45")
    eig = mp.eigsy(A, eigvals_only=True)
    print("endpoint_K_error=", mp.nstr(err, 20))
    print("symmetry_error=", mp.nstr(max(abs(A[i,j]-A[j,i]) for i in range(6) for j in range(6)), 20))
    print("lambda_min=", mp.nstr(min(eig), 20))

if __name__ == "__main__":
    main()

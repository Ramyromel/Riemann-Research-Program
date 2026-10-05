import sys\nsys.path.insert(0, "experiments/archimedean_hankel")\nfrom odd_sine_archimedean_resolvent_corrected import archimedean_matrix
from direct_physical_spectral_archimedean_audit import spectral_archimedean_matrix
import numpy as np

def check(c, n, R=500, nr=100001, terms=3000):
    a=0.5*np.log(c)
    physical=spectral_archimedean_matrix(a,n,R=R,nr=nr)
    odd=np.asarray(archimedean_matrix(c,n,n_terms=terms,dps=50).tolist(),dtype=float)
    D=np.diag([(-1)**k for k in range(1,n+1)])
    transported=D@odd@D
    d=transported-physical
    return np.linalg.norm(d), np.max(np.abs(d))

def main():
    for c,n in ((8,2),(20,4),(20,6),(50,6)):
        frob, mx=check(c,n)
        print(f"c={c} n={n} frobenius={frob:.12e} max={mx:.12e}")
        assert frob < 1e-4
        assert mx < 1e-4

if __name__=="__main__":
    main()

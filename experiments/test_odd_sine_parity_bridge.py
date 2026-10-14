from odd_sine_parity_bridge import parity_conjugation, verify_basis_identity
import numpy as np

def main():
    assert verify_basis_identity()
    A=np.arange(36,dtype=float).reshape(6,6)
    B=parity_conjugation(A)
    D=np.diag([-1,1,-1,1,-1,1])
    assert np.array_equal(B,D@A@D)
    print("basis_identity=PASS")
    print("D_conjugation=PASS")

if __name__=="__main__":
    main()

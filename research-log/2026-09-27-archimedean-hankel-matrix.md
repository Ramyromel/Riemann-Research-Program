# 2026-09-27 — Archimedean Hankel Matrix on the Shared Finite Basis

## Objective

Complete the next load-bearing step after the exact sum-level/Hankel representation: express the cutoff-free archimedean block as a matrix on the same real-even cosine basis.

## Derived result

For
[
phi_0=1,qquad phi_k=sqrt2cos(2pi kt),
]
define
[
B_{ij}(omega)=int_0^omegaphi_i(t)phi_j(omega-t),dt,
qquad
K_{ij}=2B_{ij}.
]

The audited resolvent identity gives
[
A^{m arch}_{ij}
=
h_+(0)delta_{ij}
+
sum_{nge0}
left[
rac{delta_{ij}}{a_n}
-
2Lint_0^1B_{ij}(omega)e^{-2La_n(1-omega)}domega
ight],
quad a_n=n+rac14.
]

The inner integral was reduced exactly to a finite combination of
[
int_0^1 e^{-A(1-omega)}e^{2pi ialphaomega}domega
]
and
[
int_0^1 omega e^{-A(1-omega)}e^{2pi ialphaomega}domega,
]
so numerical quadrature is not used in the resolvent summand.

## Critical correction

The pole-neutral parameter is not a fixed (1/2). The audited pole row has
[
eta=rac{log c}{4pi}.
]
An exploratory calculation with (eta=1/2) generated false negative directions and is rejected.

Using the correct (eta(c)), the restricted combined prime-plus-archimedean matrix at (c=20) is numerically nonnegative within the tested truncation error. For (N=2), the sole restricted eigenvalue was approximately
[
3.63	imes10^{-5},quad
3.75	imes10^{-5},quad
3.76	imes10^{-5}
]
at 1000, 3000, and 10000 resolvent terms respectively.

The previously recorded small eigenvalues for N=3,4,5 were produced through the broken restricted-basis implementation and must not be used as evidence. They are removed from the evidentiary chain pending recomputation.

## Interpretation boundary

The numerical pattern is compatible with a positive-semidefinite restricted form, but it does not establish it. In particular:

- the infinite resolvent series has not yet been given a rigorous tail bound;
- no exact Gram/Schur factorization has been found;
- the odd sector remains open;
- finite positivity does not by itself imply global Weil positivity.

## Next attack

After the basis correction is merged, the next attack will recompute the restricted spectrum and only then target any surviving near-null modes and the exact restricted kernel. The main questions are whether the constraints force an algebraic nullspace, whether the combined kernel admits a positive factorization, and whether the outer series can be resummed into a manifestly positive Stieltjes kernel.

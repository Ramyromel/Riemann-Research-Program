# N=2 pole-neutral scalar audit

## Purpose

For the real-even basis with (N=2), the two exact pole-neutral constraints leave a one-dimensional subspace. Therefore the restricted combined Prime–Weil form is a scalar Rayleigh quotient rather than a matrix eigenvalue problem.

This is the cleanest finite test of the current restricted construction.

## Exact restricted vector

At (c=20), with
[
eta=rac{log c}{4pi},
]
the two constraints are
[
rac{v_0}{eta^2}
+sqrt2rac{v_1}{1+eta^2}
+sqrt2rac{v_2}{4+eta^2}=0,
]
[
v_0+sqrt2v_1+sqrt2v_2=0.
]

After Euclidean normalization, the computed vector is approximately
[
vapprox
(0.04111780071455923,,
-0.7208965446628290,,
0.6918218689500871).
]

The repository implementation constructs this vector from the two constraints rather than from an eigenvector.

## Combined finite form

The audited finite quantity is
[
q_{N_T}(c)
=
v^{mathsf T}
left(
A_{m arch}^{(N_T)}(c)+P_{m prime}(c)
ight)v.
]

For (c=20,N=2), independent high-precision evaluation gives:

| resolvent terms | truncated combined value |
|---:|---:|
| 100 | (-9.6838071953	imes10^{-5}) |
| 1,000 | (3.6314631174	imes10^{-5}) |
| 10,000 | (3.7640396396	imes10^{-5}) |

The change between 1,000 and 10,000 terms is consistent with the derived (O(N_T^{-2})) tail behavior.

## Truncation correction

For the pole-neutral subspace, the second-order tail bound gives, at (c=20,N=2,N_T=1000),
[
B_{m tail}approx2.9876932753	imes10^{-6}.
]

At (N_T=10000),
[
B_{m tail}<4	imes10^{-8}.
]

Thus the **truncation-corrected numerical margin** remains positive at both cutoffs.

## Arithmetic status

The scalar value was recomputed at 60 and 90 decimal digits. The observed precision difference is negligible relative to the (10^{-5}) scale of the positive margin.

However, this is an observed precision-stability guard, not a formal interval-arithmetic enclosure. The repository therefore classifies this result as:

**NUMERICALLY SUPPORTED — TRUNCATION-CORRECTED — NOT INTERVAL-CERTIFIED.**

## What this establishes

It establishes a nontrivial, reproducible finite (N=2) positive direction for the current restricted Prime–Weil construction, with an analytic bound on the omitted Archimedean resolvent tail.

It does **not** establish:

- positivity for all admissible vectors;
- positivity for (N>2);
- positivity for all cutoffs (c);
- infinite-dimensional Weil positivity;
- the Riemann Hypothesis.

The next technical target is a genuine interval enclosure of this scalar quantity, or an exact symbolic lower bound that removes the remaining arithmetic-certification gap.

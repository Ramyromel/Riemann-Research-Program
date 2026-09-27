# Research log — 2026-09-27 — N=2 scalar restricted audit

## Execution

The corrected pole-neutral nullspace construction leaves dimension (N-1). At (N=2), this is exactly one dimension, so no eigensolver is required.

A scalar audit was implemented in:
- `experiments/archimedean_hankel/n2_scalar_certificate.py`
- `experiments/archimedean_hankel/test_n2_scalar_certificate.py`

The audit combines the exact finite prime Hankel matrix, the exact-Fourier truncated Archimedean matrix, and the analytic second-order pole-neutral tail bound.

## Independent high-precision result

For (c=20,N=2):

- (N_T=100): (-9.6838071952899666	imes10^{-5})
- (N_T=1000): (3.6314631173657719	imes10^{-5})
- (N_T=10000): (3.7640396396206897	imes10^{-5})

The second-order tail envelope at (N_T=1000) is approximately
(2.987693275258882	imes10^{-6}).

At (N_T=10000), it is below (4	imes10^{-8}).

## Interpretation

The finite restricted combined form has a positive truncation-corrected numerical margin at the tested cutoffs.

The result is stronger than a raw floating-point eigenvalue because:
1. the restricted space is exactly one-dimensional;
2. the prime block is represented by the exact finite Hankel construction;
3. the Archimedean omitted tail has an analytic (O(N_T^{-2})) bound;
4. the arithmetic was recomputed at high precision.

It is still not an interval-arithmetic theorem. The remaining numerical-certification gap is the finite arithmetic enclosure itself.

## Integrity note

The local runtime could not clone GitHub because outbound DNS/network access was unavailable. Therefore no claim is made that the repository unittest suite was executed in this environment. The implementation was source-reviewed against the current repository files, and the scalar numerical values were independently recomputed at high precision.

## Next target

Build a true interval enclosure for the scalar (N=2,c=20) value, preferably using:
- exact algebraic construction of the null vector from the two constraints;
- interval bounds for all finite prime terms;
- a rigorously bounded evaluation of the Archimedean finite sum;
- the already-derived analytic tail bound.

Only after that should this case be promoted beyond NUMERICALLY SUPPORTED.

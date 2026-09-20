# Lemma Analysis — 2026-09-20

## Research question

Can finite positivity be transferred to the cutoff-free Weil form?

## Current conclusion

Not yet.

The decisive obstacle is not simply convergence of eigenvalues. The object whose sign is required by Weil's criterion is a quadratic form on a function space. Therefore spectral convergence of one finite matrix sequence is insufficient unless the matrix sequence is linked to the same quadratic form through a controlled form convergence.

## Working decomposition

\[
\boxed{
\text{finite representation}
\rightarrow
\text{form convergence}
\rightarrow
\text{sign preservation}
\rightarrow
\text{globalization}
}
\]

### 1. Finite representation

Need an exact identity, not a fitted matrix.

### 2. Form convergence

Need explicit control of

\[
|Q_c(f)-Q(f)|
\]

for every relevant fixed \(f\), with the dependence on support, smoothness, frequency scale, and cutoff explicit.

### 3. Sign preservation

Pointwise convergence alone is not automatically sufficient for a global semidefinite statement when the relevant test functions vary with the cutoff.

### 4. Globalization

Even a theorem for compact support or a dense subspace must be connected to the exact domain appearing in Weil's criterion.

## Strategic consequence

The repository will prioritize **quadratic-form convergence** over raw eigenvalue convergence.

Eigenvalues remain diagnostic. They are not the proof object.

## Status

DERIVED RESEARCH CONCLUSION.

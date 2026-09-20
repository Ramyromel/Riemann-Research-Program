# Finite Weil Route — Exactness Audit

## External result under audit

Groskin (2026), arXiv:2607.02828, reports an exact finite Guinand–Weil dictionary for a class of truncated Weil quadratic forms and an explicit archimedean tail budget.

The paper states a certification rule in which controlled finite-cutoff positivity can imply cutoff-free positivity, while sufficiently negative finite eigenvalues can certify a cutoff-free negative; values inside the tail budget are inconclusive.

These are external results and are **not** treated as repository theorems until their exact hypotheses, normalization, and proof are independently checked.

## Audit questions

### A. Exact object

What is the exact definition of the finite quadratic form \(Q_{c,N,T}\)?

Record:

- prime cutoff \(c\);
- Galerkin dimension \(N\);
- archimedean cutoff \(T\);
- basis normalization;
- symmetry sector;
- source quotient;
- test-function mapping.

### B. Exact target

What precise cutoff-free Weil form \(Q\) is recovered?

The normalization must match the Weil criterion used by this repository.

### C. Tail

Determine the exact theorem behind the reported budget

\[
B_T \sim \frac{(2N+1)\rho\log(T)}{\pi^2T},
\qquad
\rho=\frac{2\pi}{\log c}.
\]

The asymptotic notation cannot be used as a proof bound. We require the explicit finite-constant inequality, range of \(T\), and all dependencies.

### D. Positivity transfer

If the finite-cutoff form is positive and the tail is a positive semidefinite increment, determine exactly why the cutoff-free form is positive.

This may bypass a generic spectral-limit argument.

### E. Globalization

Even if every finite construction is exact, determine whether the family of corresponding test functions is sufficient to establish the full Weil criterion.

This is the principal remaining global question.

## Acceptance standard

No imported theorem becomes a project theorem merely because its abstract or numerical artifacts are convincing. The exact statement and proof dependencies must be checked.

## Status

EXTERNAL RESULT UNDER FORMAL AUDIT.

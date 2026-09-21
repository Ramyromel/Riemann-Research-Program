# Hilbert–Pólya Finite-Matrix Experiments

## Purpose

Numerically audit a finite arithmetic spectral candidate derived from the Weil construction.

## Required separation

The experiment has two non-interchangeable tracks:

### A — Arithmetic candidate

Inputs:

- Galerkin dimension (N);
- arithmetic cutoff (c);
- exact project normalization;
- pole/archimedean/prime-power data.

Outputs:

- (S_{N,c});
- metric (G_N);
- generalized eigenvalues;
- symmetry and conditioning diagnostics;
- trace/characteristic-function diagnostics.

No zeta ordinates are allowed as construction inputs.

### B — Zero-side reconstruction control

Inputs:

- known ordinates (gamma_1,ldots,gamma_N).

Purpose:

- verify the algebra of the quotient/pencil representation;
- test basis and parity conventions;
- establish expected finite spectral symmetry.

This track is explicitly reconstruction, not discovery and not proof.

## Acceptance gates

A candidate proceeds only if:

1. (S=S^{\mathsf T}) to exact symbolic construction or certified numerical tolerance;
2. (G=G^{\mathsf T}succ0);
3. the quotient constraints are preserved;
4. eigenvalues are stable under precision escalation;
5. arithmetic coefficients reproduce the expected prime-power weights;
6. no fitted zero-dependent parameter is present;
7. an independent implementation agrees.

## Required future certification

For any promising candidate:

- arbitrary-precision arithmetic;
- interval/ball arithmetic where practical;
- independent matrix construction;
- basis-size and cutoff escalation;
- generalized-eigenvalue residuals;
- trace identity residuals;
- explicit condition numbers;
- separation of numerical evidence from theorem status.

## No-RH rule

A finite spectral match to known zeros is never, by itself, evidence that RH has been proved.

The decisive target is an exact arithmetic operator identity plus a controlled infinite-dimensional limit.

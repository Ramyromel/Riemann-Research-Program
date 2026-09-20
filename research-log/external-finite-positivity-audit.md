# External Finite-Positivity Certificate Audit

Date: 2026-09-20

## Finding

The upstream Groskin reproducibility package for arXiv:2607.02828 contains a cutoff-free interval-LDL^T inertia certificate for the finite Connes–van Suijlekom matrix at

c=100, N=200, dimension 2N+1=401.

The archived certificate reports n_pos=401 and n_neg=0, using a 9000-bit Arb computation. The package documents a self-test and an independent mpmath recomputation of the same closed forms. This is useful as an externally reproducible finite-parameter positivity result.

## Critical interpretation

This does not establish Weil positivity globally and does not prove RH.

The finite theorem gives positivity only at the selected parameter pair (c,N)=(100,200). The upstream package explicitly states that no RH or global Weil-positivity claim follows.

Thus the result may be used only as a calibration anchor:

Q_infty(100,200) is positive semidefinite at the certified finite level.

It cannot be promoted to Q_infty(c,N) positive semidefinite for all c,N, nor to the infinite-dimensional Weil form.

## New research implication

The project should not spend primary effort proving positivity at isolated finite points. The useful question is whether the certified finite matrix family has a structural positivity mechanism stable under the two limits:

1. Galerkin/band limit N -> infinity;
2. arithmetic/support limit c -> infinity.

The companion Groskin arithmetic paper adds an exact structural fact: at every prime-power event q=p^a, the first derivative jump of the finite matrix path is

-2 Lambda(q)/(sqrt(q) log(q)) times the all-ones rank-one matrix.

Its second-derivative jump is positive semidefinite. This gives an exact matrix-valued von Mangoldt measure, but the paper explicitly proves no positivity theorem for the full path.

This suggests a concrete attack on the missing sign: seek a representation of the full matrix path as a sum or integral of positive kernels plus a controlled boundary/pole term, rather than attempting to infer positivity from eigenvalues.

## Required project test

For a future claimed positivity theorem, require all of:

- exact formula for every matrix entry;
- exact pole-neutral restriction;
- positive/negative decomposition of each source;
- proof that the decomposition survives all prime-power events;
- uniform control in N;
- uniform control in c;
- compatibility with the archimedean tail;
- independent interval verification of finite instances;
- final analytic passage to the Weil criterion.

Until these are supplied, status remains OPEN.

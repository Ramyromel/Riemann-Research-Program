# 2026-09-21 — Prime Intersection / Distance Route

## Trigger

A user-supplied hypothesis proposed that the transform 2x-1, combined with additional functions selecting a prime range, might reveal a key through intersection points and distances between them.

## Decision

The hypothesis is accepted as a research lead, not as a conclusion. The first exact observation is that 2x-1 maps integers to odd integers and rescales pairwise distances by exactly 2. Therefore the transform alone is mathematically non-novel for prime-gap geometry.

The route is upgraded only when prime-power weights, logarithmic coordinates, and a nontrivial intersection/kernel functional are introduced.

## Hard constraints

- No RH claim from visual or numerical pattern matching.
- No known zeta zeros in arithmetic construction or parameter fitting.
- Prime powers must be retained through Lambda(n) or an explicitly equivalent source.
- Any correspondence with the existing Prime–Weil route must be derived symbolically.

## Main test

Determine whether a weighted intersection kernel built from prime-power data has a substantive Gram/Loewner/Hankel/Toeplitz/definiteness/spectral structure and whether that structure is exactly related to the finite Weil kernel.

## Possible outcomes

1. Trivial affine reduction -> route closed as non-novel.
2. Nontrivial arithmetic kernel without Weil correspondence -> independent research result.
3. Exact Prime–Weil correspondence -> theorem candidate with explicit hypotheses.

No proof claim is made at this stage.

## First executable result

The reference audit was implemented for c=100 using 35 prime-power sources. It confirms exactly that the 2x-1 transform has distance ratio 2 for every distinct source pair.

The canonical kernel controls separate the geometry from the transform:

- weighted logarithmic distance is not positive semidefinite (already its 2x2 principal block has negative determinant);
- weighted min(log q, log r) is positive semidefinite by an exact overlap/Gram representation;
- weighted exp(-|log q-log r|) is positive semidefinite by the standard exponential kernel structure.

These PSD results are **generic kernel facts**, not evidence for RH and not yet evidence of a Prime–Weil correspondence. They establish that the route can generate mathematically nontrivial weighted intersection kernels, while also showing that positivity alone is too weak to identify the Riemann object.

The experiment uses zero zeta ordinates: **0**.

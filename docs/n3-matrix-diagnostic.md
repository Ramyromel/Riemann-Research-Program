# N=3 matrix diagnostic

## Purpose

This experiment is the first matrix-level extension beyond the certified N=2 scalar sector. For N=3, the two pole-neutral constraints leave a two-dimensional admissible space.

The diagnostic is intentionally **not** an interval certificate. It is a discovery instrument for the load-bearing finite-to-infinite step.

## Construction

For each cutoff c:

1. build the exact finite prime-power Hankel block;
2. build the shared-basis Archimedean resolvent truncation;
3. impose the two pole-neutral constraints;
4. form the restricted 2 x 2 symmetric matrix;
5. inspect its eigenvalues as the resolvent cutoff T increases.

No zeta-zero ordinates enter the construction.

## Result observed during independent high-precision execution

At T=1000 the smallest restricted eigenvalue was slightly negative for c = 10, 20, and 50. At T=4000 it moved substantially toward zero; c=10 became slightly positive while c=20 and c=50 remained very close to zero on the displayed precision.

These observations are **not** counterexamples. The finite resolvent truncation has an analytically bounded omitted tail, and the observed scale is comparable to that tail. The correct conclusion is therefore:

> N=3 exposes the finite-to-infinite limit as the critical mechanism. A stronger matrix-level tail enclosure is required before the sign can be classified.

This is exactly the kind of result the project should surface early rather than hiding it behind numerical positivity.

## Status

**DISCOVERY / UNRESOLVED.**

- No RH claim.
- No negative theorem.
- No zero data.
- No interval certification yet.
- Next target: a certified 2 x 2 matrix enclosure at N=3, with the analytic tail applied at matrix/operator level rather than as a loose scalar correction.

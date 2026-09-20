# Frontier Update — 2026-09-20

## Question

What changed after the repository baseline was created?

## Observation

Recent 2026 work materially sharpens the finite-to-infinite problem. In particular, finite truncated Weil forms now have stronger exact dictionaries and explicit tail estimates in the published/preprint literature.

## Consequence

The original research target is refined.

Instead of treating finite-to-infinite convergence as one monolithic gap, split it into four obligations:

### L1 — Finite exactness
Prove that the finite representation computes the intended Weil quadratic form on the declared test-function subspace.

### L2 — Tail bound
Establish a rigorous bound for the omitted archimedean/geometric contribution with all constants and domains explicit.

### L3 — Positivity transfer
Determine conditions under which finite positivity plus the tail bound implies positivity of the cutoff-free form.

### L4 — Globalization
Show that the family of test-function subspaces is sufficiently rich to recover the full Weil criterion.

## Falsification test

The program fails on this route if any of the following occurs:

- the tail estimate is insufficient at the spectral scale required for globalization;
- positivity does not survive the chosen limit;
- the finite dictionary covers only a restricted quotient that cannot be made dense in the required topology;
- the resulting positive form is not exactly the Weil form;
- an off-line-zero construction survives all proposed positivity constraints.

## Status

DERIVED RESEARCH PLAN — not a theorem.

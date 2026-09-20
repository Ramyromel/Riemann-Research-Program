# Adversarial Counterexample Challenges

## Purpose

This file defines explicit attempts to falsify the current research path. A successful counterexample should be treated as a valuable research result, not as a failure of the review process.

## Challenge A — Finite-to-global instability

Attempt to construct a sequence of admissible finite objects whose quadratic forms are nonnegative at every finite stage but whose proposed limiting form becomes negative.

Required checks:

- common versus varying domains;
- pointwise versus uniform convergence;
- convergence of quadratic forms;
- boundary/tail terms;
- dependence of error bounds on dimension and cutoff.

A successful construction would invalidate the corresponding transfer argument.

## Challenge B — Coverage failure

Attempt to produce an admissible Weil test function that cannot be approximated by the proposed finite-function family in the topology required for continuity of the Weil form.

A failure of density or closure is a direct attack on the globalization step.

## Challenge C — Sector obstruction

Attempt to construct an odd-sector example for which the even-sector construction provides no valid extension.

The absence of an odd-sector theorem must not be hidden by results established only in the even sector.

## Challenge D — Spectral mismatch

Given a proposed limiting operator, search for a mismatch between:

- the operator's spectral data;
- the required zero-side data;
- multiplicities;
- symmetry;
- normalization;
- boundary contributions.

Self-adjointness alone is not accepted as evidence of arithmetic identification.

## Challenge E — Numerical certification failure

Recompute finite positivity using an independent implementation and precision strategy. Search for:

- sign instability;
- precision-dependent inertia;
- ill-conditioning;
- incorrect normalization;
- omitted tail contributions;
- parameter-dependent failure.

## Review rule

A counterexample, failed proof step, or corrected normalization should be recorded with the same transparency as a positive result.

**The program is designed to survive attempts to break it, not to avoid them.**

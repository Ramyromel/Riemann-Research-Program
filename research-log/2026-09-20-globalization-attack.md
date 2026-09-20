# Research Log — Globalization Attack

**Date:** 2026-09-20

## Decision

The finite Guinand–Weil result is now treated as a finite-level theorem under audit, not as evidence of an already available global density theorem.

The next mathematical attack is therefore deliberately adversarial: try to prove or disprove that the finite generated test-function family is sufficient for the Weil criterion.

## Starting point

The authoritative Weil framework uses a broad admissible test-function class and an explicit formula whose zero-side term is paired with arithmetic and archimedean terms. The finite dictionary constructs a much smaller, parameterized band-limited family.

The gap is therefore a functional-analytic one:

\[
\text{finite generated family}
\stackrel{?}{\longrightarrow}
\text{sufficient class for Weil positivity}.
\]

## First attack: identify a workable dense core

A viable route would be to choose a standard smooth compactly supported core in logarithmic coordinates, impose the required vanishing constraints by a finite-rank correction, and then determine whether the finite dictionary's band-limited functions can approximate that corrected core while preserving the constraints.

This must be proved, not inferred from Fourier intuition.

## Second attack: quadratic-form continuity

Even if \(g_N\to g\) in a natural norm, the Weil form may contain prime, pole, and archimedean contributions whose separate convergence requires explicit estimates.

The target is an inequality of the form

\[
|Q(g_N)-Q(g)|\le E_N(g),\qquad E_N(g)\to0,
\]

on a specified dense core, with all cutoff parameters visible.

## Third attack: falsification

A counterexample to density, constraint preservation, or form continuity would block this route and force a different RH strategy.

## Result

No counterexample or proof of global density has yet been established in this log. The repository remains **OPEN RESEARCH**.

The finite exactness result is useful because it lets this attack operate on exact finite identities rather than numerical surrogates.

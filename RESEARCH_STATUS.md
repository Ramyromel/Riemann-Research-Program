# Research Status

Date: 2026-09-20

## Global status

- Riemann Hypothesis: OPEN
- Complete proof in this repository: NONE
- Weil positivity route: ACTIVE RESEARCH
- Spectral/operator route: ACTIVE RESEARCH
- Finite-to-infinite convergence: CRITICAL OPEN GAP
- Finite Guinand–Weil dictionary: EXTERNAL THEOREM UNDER AUDIT
- Full unrestricted globalization: OPEN
- Fixed-support factor approximation: DERIVED SUBTARGET / OPEN BRIDGE
- Numerical computation: SUPPORTING EVIDENCE ONLY
- Independent verification: REQUIRED

## Current frontier

The finite-level problem has been sharpened. Groskin (arXiv:2607.02828v3) supplies an exact finite dictionary between the audited Galerkin construction and a corresponding band-limited Guinand–Weil test-function family, plus a positive archimedean tail theorem. The paper explicitly does not claim realization of arbitrary admissible test functions.

A stronger structural observation now narrows the global problem further: Weil positivity can be formulated using compactly supported factors, and for a fixed support window only finitely many prime-power terms contribute. Therefore the prime cutoff need not be sent to infinity for one fixed test function; the remaining limit is primarily the frequency/factor approximation limit.

## Active proof program

1. **Finite dictionary audit:** verify the exact normalization, signs, and hypotheses independently.
2. **Fixed-support factor space:** identify the exact target factor space in the Weil criterion and its rescaling to the finite Volterra construction.
3. **Cosine-polynomial approximation:** prove density of the finite even Galerkin factors in the chosen smooth compact-support core.
4. **Nonlinear continuity:** prove continuity of the Volterra/convolution map under the selected norm.
5. **Constraint correction:** impose pole/moment constraints exactly at finite N and prove the correction vanishes in the limit.
6. **Weil-form continuity:** establish convergence of prime and archimedean contributions under the same approximants.
7. **Positivity closure:** use the proved pointwise quadratic-form closure lemma once the common admissible approximation sequence is established.
8. **Global support exhaustion:** only after the fixed-window theorem is closed, extend to all compact supports required by the external Weil criterion.

## What remains the principal bottleneck

The decisive unresolved statement is now:

> Every admissible compact-support Weil factor can be approximated, after the exact normalization/rescaling, by the finite Galerkin factor space in a topology that preserves the pole/moment constraints and makes the Weil quadratic form continuous.

This is narrower than unrestricted density of the full Guinand–Weil test-function class, but it is still unproved.

## Status semantics

CONJECTURAL = proposed statement without proof.
DERIVED = logically derived from established premises.
NUMERICALLY_SUPPORTED = reproducible computation without analytic proof.
VERIFIED = independently checked against stated assumptions.
PROVED = complete proof with all dependencies and limiting arguments closed.
REFUTED = counterexample or contradiction established.
BLOCKED = unresolved dependency prevents progress.

## Rule

No numerical experiment, symbolic pattern, fitted formula, or plausible operator construction may be promoted to PROVED without a complete mathematical argument.

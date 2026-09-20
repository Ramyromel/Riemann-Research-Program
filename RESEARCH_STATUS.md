# Research Status

Date: 2026-09-20

## Global status

- Riemann Hypothesis: OPEN
- Complete proof in this repository: NONE
- Weil positivity route: ACTIVE RESEARCH
- Spectral/operator route: ACTIVE RESEARCH
- Finite-to-infinite convergence: CRITICAL OPEN GAP
- Finite Guinand–Weil dictionary: EXTERNAL THEOREM UNDER AUDIT
- Globalization/density of the finite test-function family: OPEN
- Numerical computation: SUPPORTING EVIDENCE ONLY
- Independent verification: REQUIRED

## Current frontier

The finite-level problem has been sharpened. Groskin (arXiv:2607.02828v3) supplies an exact finite dictionary between the audited Galerkin construction and a corresponding band-limited Guinand–Weil test-function family, plus a positive archimedean tail theorem. This removes a major ambiguity at the finite level.

The remaining bottleneck is **globalization**, not merely eigenvalue convergence:

1. establish the exact normalization bridge used by this repository;
2. prove that the finite test-function families are sufficient for the full Weil criterion, or replace them with a provably sufficient class;
3. prove convergence of the quadratic form under the required joint limits in prime cutoff, frequency band, and archimedean cutoff;
4. preserve all admissibility, pole, and moment constraints;
5. apply a valid closure/limit argument to obtain global Weil positivity.

The external theorem explicitly does not claim that arbitrary admissible Guinand–Weil test functions are realized by the finite dictionary. Therefore increasing the finite dimension cannot be treated as density without a separate theorem.

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

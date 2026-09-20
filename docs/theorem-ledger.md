# Theorem Ledger

This ledger separates imported theorems from project conjectures and numerical observations.

## T-001 — Riemann Hypothesis

**Statement.** Every nontrivial zero \(\rho\) of \(\zeta(s)\) satisfies \(\Re(\rho)=1/2\).

**Status:** EXTERNAL / OPEN PROBLEM.

**Authority:** Clay Mathematics Institute.

**Use:** Final target only. No downstream statement may silently assume T-001.

---

## T-002 — Weil explicit formula

For an admissible test function in the class used by the standard Weil formulation, the Mellin transform of the test function relates the sum over nontrivial zeros to prime-power and archimedean terms.

**Status:** EXTERNAL THEOREM.

**Use:** Establishes the arithmetic/geometric decomposition from which the Weil quadratic criterion is constructed.

**Repository rule:** Before using a specialized normalization, record the exact transform convention, function space, convergence prescription, and sign convention.

---

## T-003 — Weil criterion

A standard formulation gives an RH-equivalent sign condition for a class of convolution-type test functions satisfying the required vanishing constraints.

**Status:** EXTERNAL THEOREM.

**Use:** Converts RH into a positivity/negativity problem.

**Critical caution:** Equivalent formulations use different sign conventions and different definitions of the quadratic form. The repository must never switch conventions without an explicit conversion.

---

## T-004 — Finite truncated Weil constructions

Recent work studies finite/cutoff approximations of Weil-type forms and their spectra.

**Status:** EXTERNAL RESEARCH INPUT.

**Use:** Discovery and construction of candidate finite objects.

**Limitation:** Finite spectral agreement does not imply the cutoff-free Weil criterion.

---

## T-005 — Compact-window certified positivity

Recent work gives certified positivity bounds for certain compact-support windows.

**Status:** EXTERNAL RESEARCH INPUT.

**Use:** Evidence that nontrivial finite/compact positivity regions can be certified.

**Limitation:** A compact window is not the global test-function class required for RH.

---

## T-006 — Finite-to-infinite transfer

**Statement sought by this project:** A theorem giving sufficient hypotheses under which a family of finite/cutoff quadratic forms converges to the exact Weil form in a topology strong enough to preserve the required sign condition.

**Status:** OPEN RESEARCH TARGET.

This is not an imported theorem.

### Required ingredients

1. Exact finite form.
2. Exact limiting form.
3. Convergence mode.
4. Uniform or otherwise sufficient error bound.
5. Sign margin or semidefinite-limit argument.
6. Density/globalization of the test-function family.

Until all six are proved, finite positivity cannot be promoted to RH.

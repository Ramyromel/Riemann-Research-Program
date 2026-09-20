# Spectral Operator Bridge Audit — 2026-09-20

## Status

**OPEN RESEARCH TARGET — NO RH CLAIM**

A new external input in the Connes/Groskin line is the 2026 paper *Bulk trace laws and algebraic boundary interaction for the sine Loewner operator*. The upstream repository describes uniform trace laws for the infinite sine Loewner operator and its finite matrices, half-line boundary flow, algebraic boundary interaction, and a certified nonzero even–odd boundary splitting. The paper explicitly makes no claim of proving the Riemann Hypothesis.

## Why this matters to this program

The repository currently has two distinct spectral tasks:

1. obtain a finite positivity mechanism for the Weil quadratic form;
2. identify a limiting self-adjoint/spectral object whose spectrum is exactly the nontrivial zeta ordinates.

The sine-Loewner results are relevant to task (2), but they do **not** establish the required identification. A trace law or self-adjoint operator is not enough: the project still needs an exact theorem connecting the limiting operator, its spectral measure, and the Weil/zeta explicit formula.

## Required bridge theorem

A useful future theorem would have to establish, with all domains and normalizations explicit, a chain of the form

[
	ext{finite Weil matrices}
longrightarrow
	ext{limiting operator}
longrightarrow
	ext{spectral measure}
longleftrightarrow
{gamma:zeta(1/2+igamma)=0}.
]

At minimum the bridge must prove:

- **B1 — Operator convergence:** the finite matrices converge to a specified self-adjoint operator in a mathematically adequate sense (for example strong resolvent convergence, norm resolvent convergence, or an explicitly stronger/weaker topology with the needed spectral consequences).
- **B2 — Arithmetic identification:** the limiting operator or its spectral transform reproduces the Weil explicit-formula terms, including prime, pole, and archimedean contributions.
- **B3 — Spectral identification:** the limiting spectral measure has atoms/eigenvalues exactly at the nontrivial zeta ordinates, with multiplicities handled correctly.
- **B4 — Positivity link:** the operator's positivity/nonnegativity is equivalent to the required Weil quadratic-form positivity on the full admissible test-function class.
- **B5 — Boundary control:** parity and boundary effects do not introduce spurious spectral data or remove required zeta data in the limiting construction.
- **B6 — Infinite-dimensional domain control:** all quadratic forms/operators are defined on compatible dense domains and all limiting interchanges are justified.

## Attack strategy

The project should **not** attempt to prove B1–B6 by numerical fitting to known zeros.

Instead:

1. derive the exact finite matrix/path formula already audited in the Guinand–Weil work;
2. compare its quadratic form, resolvent, and trace identities with the sine-Loewner operator;
3. isolate the boundary contribution as an explicit finite-rank or trace-class correction where possible;
4. test whether the correction vanishes, stabilizes, or carries genuine arithmetic information under the relevant limit;
5. derive an operator-level explicit formula;
6. only then attempt spectral identification.

## Falsification conditions

This route should be rejected or downgraded if any of the following occurs:

- finite matrices have multiple inequivalent operator limits;
- the candidate limit has spectral components not represented by the Weil form;
- boundary terms remain uncontrolled in the limit;
- trace convergence holds but resolvent/spectral convergence fails;
- the operator reproduces numerical zeta ordinates but no exact explicit-formula identity can be proved;
- positivity of the operator does not imply Weil positivity on the required test-function domain.

## Current disposition

**DERIVED STRATEGY / EXTERNAL INPUT**

The existence of the external sine-Loewner spectral results is verified from the upstream reproducibility repository. The bridge to the Riemann zeta zeros is **not** established here.

This track is complementary to the finite-positivity track; it does not replace the load-bearing positivity problem.

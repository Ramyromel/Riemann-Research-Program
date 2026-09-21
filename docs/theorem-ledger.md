# Theorem Ledger

## T-001 — Riemann Hypothesis
**Status:** EXTERNAL / OPEN PROBLEM.

## T-002 — Weil explicit formula
**Status:** EXTERNAL THEOREM.

## T-003 — Weil criterion
**Status:** EXTERNAL THEOREM. RH-equivalent sign condition on the required convolution/autocorrelation class with pole constraints.

## T-004 — Finite Guinand–Weil dictionary and archimedean tail theorem
**Source:** Groskin, arXiv:2607.02828v3 (2026).

For fixed finite parameters, the real-even Galerkin construction has an exact map to admissible band-limited Guinand–Weil test functions, and the cutoff-free finite quadratic value equals the corresponding zero-side sum. The omitted archimedean tail is a positive Cauchy–Stieltjes increment with an explicit certification budget.

**Status:** EXTERNAL THEOREM UNDER PROJECT AUDIT.

No global positivity or RH inference is imported.

## T-005 — Compact-window certified positivity
Recent work gives rigorous positivity certificates for selected compact-support windows.

**Status:** EXTERNAL RESEARCH INPUT. Not a global theorem.

## T-006 — Global finite-to-infinite transfer
**Status:** OPEN.

### T-006A — Even-sector fixed-support factor approximation
For fixed \(L\), smooth compactly supported real-even admissible factors can be approximated in every \(C^m\) norm by finite cosine/Galerkin factors, with the two pole moments imposed exactly by a fixed two-dimensional correction. The induced autocorrelations converge and the fixed-support Weil form is continuous along the sequence.

**Status:** DERIVED. Proof recorded in docs/fixed-support-density-lemma.md.

**Limitation:** approximation does not supply the missing sign.

### T-006B — Even-sector finite positivity
\[
\langle v,Q_\infty(c,N)v\rangle\ge0
\]
for every admissible real-even finite vector and every \(c>1,N\).

**Status:** OPEN / LOAD-BEARING.

### T-006C — Odd-sector dictionary and positivity
A matching finite dictionary, constraint-preserving approximation theorem, and positivity mechanism for the odd sector.

**Status:** OPEN.

### T-006D — Full Weil assembly
Combine parity sectors, form continuity, support exhaustion, and the external Weil criterion.

**Status:** OPEN.

### T-006E — Fixed-support positivity closure
For a fixed admissible core, if finite generated admissible objects have nonnegative cutoff-free quadratic values and their quadratic values converge to the target Weil form, then target positivity follows by closedness of \([0,\infty)\). No positive spectral gap is required.

**Status:** DERIVED. Proof recorded in docs/fixed-support-positivity-transfer-theorem.md.

**Limitation:** this closes only the logical limit step. It does not prove finite positivity, finite-family density, normalization, odd-sector coverage, or RH.

### T-006F — Prime-path Loewner concavity
At fixed Galerkin level, the cutoff-free finite prime block has negative-semidefinite rank-one derivative jumps at every prime-power threshold. Equivalently, its singular second derivative is a negative-semidefinite matrix-valued von Mangoldt measure. This is an external structural theorem under audit; the Loewner-concavity consequence is derived from it.

**Status:** EXTERNAL THEOREM UNDER PROJECT AUDIT + DERIVED CONSEQUENCE.

**Limitation:** concavity of the prime block does not imply positivity of the complete matrix. The remaining load-bearing problem is domination by the pole/archimedean block on the exact pole-neutral subspace, uniformly in (c,N).

## Status rule
No numerical spectral match, finite positive-definiteness result, or external claim may be promoted to PROVED without an analytic theorem covering all parameters and the final limiting argument.

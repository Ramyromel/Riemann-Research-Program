# External Audit — Groskin Finite Guinand–Weil Dictionary

**Date:** 2026-09-20  
**Source:** Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, arXiv:2607.02828v3 (14 Aug 2026).

## Audit objective

Determine exactly what the external result supplies to the project's finite-to-infinite Weil-positivity program, and prevent an accidental upgrade from a finite theorem to a proof of the Riemann Hypothesis.

## External claims verified from the v3 paper

1. For fixed prime cutoff (c>1) and frequency band (N), the Connes–van Suijlekom / Connes–Consani–Moscovici construction produces a finite Galerkin matrix.
2. Every real even Galerkin vector (v\in\mathbb R^{N+1}) is mapped to a band-limited Guinand–Weil test function (g_v).
3. The paper states an exact finite dictionary: the quadratic value of the cutoff-free finite form equals the zero-side explicit-formula sum for the induced (g_v).
4. The source-to-form map factors through an exact (2N+1)-dimensional quotient.
5. A pole-neutral subfamily exists under stated finite-dimensional constraints.
6. The archimedean tail beyond a finite frequency cutoff is proved to be a positive Cauchy–Stieltjes Gram increment.
7. The paper derives a two-sided finite-cutoff certification rule with an explicit tail budget (B_T): finite-(T) positivity certifies cutoff-free positivity for the same finite matrix; a sufficiently negative eigenvalue certifies a cutoff-free negative; values inside the error band are inconclusive.
8. The paper explicitly states that its dictionary does **not** realize arbitrary Guinand–Weil test functions.

## What this closes

The external theorem materially strengthens the project's **finite-level exactness** layer:

[
v \longmapsto g_v \longmapsto
\text{exact zero sum}
\longleftrightarrow
\text{finite Weil quadratic value}.
]

It also supplies a controlled relationship between finite archimedean computation and the corresponding cutoff-free finite matrix.

Therefore the project can no longer treat "finite matrix -> zero-side identity" as merely a numerical hypothesis.

## What it does not close

The following remain open in this repository:

### G-A — Global test-function coverage

The finite dictionary is an ((N+1))-parameter family at each fixed (N). The source explicitly says no claim is made that arbitrary admissible Guinand–Weil test functions are realized.

A proof of RH through Weil positivity therefore still needs a theorem showing that the union/closure of the constructed family is sufficient for the **full** Weil criterion, or an alternative argument proving the criterion directly on the restricted family.

### G-B — Globalization in (N)

Increasing (N) does not by itself prove density in the topology relevant to the Weil quadratic form. A candidate density theorem must specify:

- the target test-function space;
- its topology/norm;
- the approximation operator (P_N);
- convergence (P_N f\to f);
- convergence of the quadratic form, including the prime, pole, and archimedean pieces;
- preservation of the admissibility/vanishing constraints.

### G-C — Parameter coupling

The finite construction uses a prime cutoff (c), a frequency band (N), and an archimedean cutoff (T). A global argument must specify an admissible directed limit or a sequence ((c_k,N_k,T_k)) and prove that every required component converges to the same cutoff-free Weil object.

### G-D — Final implication

Even if positivity is established for the closure of the finite family, the exact theorem needed is:

[
\text{positivity on a sufficient class}
\Longrightarrow
\text{Weil criterion}
\Longrightarrow
RH.
]

The first implication is currently the principal mathematical gap. The second is imported from the Weil criterion once the exact normalization and test-function class have been matched.

## Status

**T-004:** EXTERNAL THEOREM UNDER AUDIT — finite dictionary and tail theorem are strong enough to use as external research input, but not yet imported as project-proved results.

**T-006:** OPEN RESEARCH TARGET — the decisive remaining problem is now formulated more narrowly as a **globalization/density + quadratic-form convergence theorem**, not merely generic eigenvalue convergence.

## Falsification tests

Any proposed globalization theorem must be attacked for:

1. finite-dimensional families whose union is not dense in the required topology;
2. approximation that preserves (L^2) norm but not the Weil form;
3. prime-cutoff errors that fail to vanish uniformly on the chosen family;
4. pole/moment constraints that are lost under projection;
5. archimedean convergence that is only pointwise in parameters;
6. non-commuting limits (c\to\infty), (N\to\infty), (T\to\infty);
7. hidden dependence of admissibility constants on (N,c,T).

**No RH claim follows from this audit.**

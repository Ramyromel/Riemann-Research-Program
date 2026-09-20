# Globalization Target: Finite Guinand–Weil Families

**Status:** OPEN RESEARCH TARGET  
**Depends on:** T-004, T-006

## Objective

Let \(\mathcal G_{c,N}\) denote the finite family of Guinand–Weil test functions produced by the audited finite dictionary. The goal is to determine whether

\[
\overline{\bigcup_{c,N}\mathcal G_{c,N}}
\]

is sufficient for the exact Weil criterion, in a topology for which the Weil quadratic form is continuous along admissible approximants.

This document deliberately does **not** assume that the union is dense.

## Required theorem

A successful globalization theorem must identify:

1. the exact target Weil test-function space \(\mathcal W\);
2. the exact topology \(\tau\) on \(\mathcal W\);
3. the finite spaces \(\mathcal G_{c,N}\subseteq\mathcal W\);
4. an approximation map \(P_{c,N}:\mathcal W_0\to\mathcal G_{c,N}\) on a dense core \(\mathcal W_0\);
5. admissibility preservation, including all moment/pole-neutral constraints;
6. \(P_{c,N}f\to f\) in \(\tau\);
7. \(Q(P_{c,N}f)\to Q(f)\);
8. a limit argument transferring nonnegativity from the finite family to \(\mathcal W_0\), followed by density/continuity to all of \(\mathcal W\).

## Critical distinction

The finite dictionary proves an exact identity **for each generated finite test function**. It does not, by itself, prove density.

Likewise, convergence of eigenvalues of finite matrices is not a substitute for density of their associated test functions.

## Attack program

Any candidate theorem must be tested against:

- non-density of the band-limited union;
- failure of moment constraints under projection;
- loss of the relevant Weil-form topology;
- non-uniform prime-cutoff errors;
- non-uniform archimedean errors;
- incompatible joint limits in \(c,N,T\);
- finite families that reproduce known zeros but miss a valid test direction.

## Acceptance criterion

Do not mark this target VERIFIED unless an explicit theorem and proof establish the approximation and form-convergence statements above.

Do not infer RH from numerical density evidence.

## Current mathematical opportunity

The elementary positivity-closure lemma already proved in this repository shows that if a **common admissible test function** \(f\) can be approximated by finite objects with nonnegative quadratic values and those values converge to \(Q(f)\), then positivity passes to the limit. The difficult work is therefore the construction and control of the approximation sequence, not the order-topology closure step itself.

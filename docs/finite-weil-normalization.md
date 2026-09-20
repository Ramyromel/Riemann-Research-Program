# Weil Finite-Level Normalization Map

This document records the normalization bridge required before any external finite Weil result can be promoted into a project theorem.

## Reference normalization

The classical Weil framework expresses an explicit-formula functional as a zero-side term plus prime/pole/archimedean contributions. The Clay reference formulation uses a Mellin transform and a specified admissible test-function class.

The finite construction audited here instead uses:

- prime cutoff (c>1);
- frequency/Galerkin band (N);
- archimedean cutoff (T) for numerical evaluation;
- an even-sector Galerkin vector (v);
- a source-to-test-function map (v\mapsto g_v);
- a cutoff-free finite matrix (Q_\infty).

## Required identity chain

For every proposed project instantiation, the following must be written with no omitted constants or sign changes:

[
v
\xrightarrow{\;\mathcal G\;}
g_v
\xrightarrow{\;\text{explicit formula}\;}
\sum_\rho g_v(\rho)
\xleftrightarrow{\text{normalization audit}}
\langle v,Q_\infty v\rangle.
]

The equality must specify whether the project calls the resulting quantity (Q), (-Q), (W^{(1)}), or another convention.

## Three independent checks required

### N1 — Analytic convention

Match:

- Mellin/Fourier transform convention;
- normalization of the completed zeta function;
- location and multiplicity convention for nontrivial zeros;
- admissible test-function class;
- convergence prescription for the zero sum.

### N2 — Matrix convention

Match:

- basis and even-sector embedding;
- index set;
- inner-product convention;
- prime block sign;
- pole block sign;
- archimedean block sign;
- diagonal divided-difference convention.

### N3 — Criterion convention

Match the project's positivity statement against an authoritative Weil criterion. A sign reversal is harmless only when explicitly transformed everywhere; an untracked sign reversal invalidates the inference.

## Current disposition

**Verified externally:** the v3 paper states the finite dictionary and archimedean tail theorem.

**Not yet project-verified:** a line-by-line normalization identity between the external construction and the exact convention selected by this repository.

**Research consequence:** before implementing a large numerical matrix, complete N1–N3. Numerical agreement cannot substitute for this normalization bridge.

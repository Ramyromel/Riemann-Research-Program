# Globalization Attack: Autocorrelation / Band-Limited Core

**Status:** OPEN RESEARCH — CANDIDATE ROUTE, NOT A THEOREM

## Objective

Replace the overly broad question

> "Are the finite Guinand–Weil families dense in the full admissible test-function class?"

by the narrower question actually required by Weil positivity:

> Can every admissible positivity test be represented or approximated by autocorrelations of finite-band functions that occur in the finite dictionary, with convergence strong enough for the Weil quadratic form?

This distinction matters because Weil positivity is naturally tested on convolution/autocorrelation forms rather than on arbitrary test functions.

## External mathematical basis

The Clay/Bombieri formulation records Weil positivity as an RH-equivalent positivity condition on a class of convolution-type test functions. A separate Connes–Consani formulation notes that one may restrict attention to compactly supported auxiliary functions in its positivity formulation. These are external results and are not re-proved here.

Groskin's finite dictionary supplies, for every finite real-even Galerkin vector, an explicit band-limited Guinand–Weil test function and an exact zero-side identity. It explicitly does **not** claim that arbitrary admissible Guinand–Weil functions are realized.

Therefore the missing bridge may be smaller than unrestricted density.

## Candidate factorization

Let the target positivity class be represented schematically by

\[
g = f * \widetilde f,
\]

with the required symmetry, decay, and pole/moment-neutral constraints.

Let \(f_N\) be a finite-band approximation to \(f\), and define

\[
g_N = f_N * \widetilde{f_N}.
\]

If:

1. \(f_N\) belongs to the finite Galerkin class;
2. the admissibility constraints are preserved exactly or by a controlled finite-rank correction;
3. \(f_N \to f\) in a topology implying \(g_N \to g\) in the Weil-form topology;
4. \(Q(g_N) \to Q(g)\);
5. the finite dictionary identifies \(Q(g_N)\) with the corresponding finite quadratic form;

then finite positivity plus the already-proved pointwise positivity-closure lemma would imply \(Q(g)\ge 0\).

This would reduce the global problem to a concrete approximation theorem for the auxiliary factor \(f\), rather than an unrestricted density theorem for all test functions.

## The decisive obstruction

The candidate route is **not yet established** because the finite dictionary's map \(v\mapsto g_v\) is not merely an arbitrary linear band-limit truncation. The paper describes a Volterra/convolution construction and an exact finite source quotient. We must therefore prove that the resulting finite family contains, or approximates sufficiently well, the required autocorrelation factors.

In particular, it is insufficient to show that ordinary trigonometric polynomials are dense. We must show compatibility with the specific Volterra map, its even-sector constraints, and the pole/moment-neutral hyperplanes.

## Required globalization lemma

A useful target statement is:

> **Finite-factor approximation lemma (target).** For every admissible compactly supported auxiliary factor \(f\) in a dense core, there exists a sequence of finite Galerkin vectors \(v_N\) such that the induced \(g_{v_N}\) converges to \(g_f\) in a topology \(\tau_Q\) for which the Weil quadratic form is continuous, while all required pole/moment constraints are preserved.

A proof of this lemma, together with the external Weil criterion and the finite dictionary, would close the current globalization gap.

## Falsification tests

The route must be rejected if any of the following is demonstrated:

- the Volterra image is not dense in the required factor space;
- the even-sector restriction removes a necessary admissible direction;
- pole/moment-neutral corrections become unbounded with N;
- convergence of factors does not imply convergence of the Weil form;
- prime-cutoff errors fail to vanish uniformly along the approximating sequence;
- the finite family only reproduces a restricted spectral subspace and misses a valid Weil test direction.

## Current disposition

**DERIVED RESEARCH TARGET:** the route is mathematically narrower than unrestricted test-function density.

**NOT PROVED:** no approximation theorem has yet been established here.

**NO RH CLAIM:** this document provides a research reduction, not a proof of the Riemann Hypothesis.

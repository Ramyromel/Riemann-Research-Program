# Autocorrelation Globalization Attack — 2026-09-20

## Decision

The next attack is the factor-space rather than full test-function-space globalization problem.

The motivation is structural: Weil positivity is naturally expressed on convolution/autocorrelation test objects, while the finite Groskin dictionary is generated through a Volterra/convolution construction. Groskin proves exact finite transport for the generated family but explicitly declines any claim of arbitrary test-function realization.

## What was verified externally

- Clay's official problem statement still lists RH as unsolved. 
- Bombieri's official Clay description gives Weil's explicit formula and the RH-equivalent positivity formulation.
- Groskin v3 states an exact finite Guinand–Weil dictionary for the generated finite family, plus archimedean tail control; it explicitly states that it makes no RH claim.
- Connes–van Suijlekom's 2025 work gives a continuous analogue of the finite spectral construction and connects positivity/zero localization through Fourier transforms.

## New reduction

Instead of proving

\[
\overline{\bigcup_{c,N}\mathcal G_{c,N}} = \mathcal W,
\]

seek a dense core of admissible factors \(f\) and prove

\[
f_N \to f
\quad\Longrightarrow\quad
g_{f_N}=f_N*\widetilde{f_N}\to f*\widetilde f
\]

in a topology controlling the Weil quadratic form.

The finite dictionary then needs to be shown compatible with \(g_{f_N}\), including the pole/moment-neutral conditions.

## Why this is a material improvement

The previous globalization target treated the image family as an unexplained subset of the full test-function space. The new formulation uses the algebraic structure already present in the positivity criterion and in the finite construction.

The main unknown is now explicit:

> Is the finite Volterra image sufficiently rich in the admissible factor space?

That question can be attacked by functional analysis and finite-dimensional rank calculations rather than by spectral numerics alone.

## Immediate proof program

1. Extract the exact finite map \(v\mapsto T_v\mapsto K_v\mapsto g_v\) from Groskin v3.
2. Identify the ambient factor space and its norm/topology.
3. Prove density of the finite coefficient factors, if true.
4. Prove continuity of the Volterra/convolution map.
5. Construct exact finite-rank corrections for the two pole/moment constraints.
6. Prove continuity of the Weil form under the resulting approximation.
7. Combine with the elementary positivity-closure lemma already proved in this repository.
8. Only after all seven steps, test whether the resulting implication reaches the full Weil criterion.

## Hard stop conditions

Do not promote this route to VERIFIED if density is only numerical, if the topology is left implicit, if constraints are only asymptotically satisfied, or if convergence is shown only for known zeta zeros.

## Current result

**No proof. No counterexample.**

The research target has been narrowed from unrestricted density to a concrete factorization-and-continuity problem.

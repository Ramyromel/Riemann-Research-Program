# Research Log — 2026-09-21 — Hilbert–Pólya Finite-Matrix Track

## Decision

Open a dedicated Hilbert–Pólya research track using the finite Weil/Galerkin structure already present in the repository.

## External input

Yaoming Shi, “Construction of Finite Hilbert–Pólya Matrices from Weil's Explicit Formula,” arXiv:2609.04908 (2026), describes finite real-symmetric Prime–Weil matrices assembled from pole, archimedean, and prime-power data and a Hermitian definite generalized eigenproblem on a fixed zero-mean contrast space.

The paper explicitly distinguishes reconstruction from proof: when zeta ordinates are supplied as inputs, the resulting finite spectral match is a reconstruction theorem. It does not claim a proof of RH.

## Project interpretation

This is closely aligned with the repository's existing finite Weil work, but the external construction must not be imported as a black-box proof.

The project therefore defines the candidate finite Hamiltonian through a generalized eigenproblem

[
S_{N,c}x=lambda G_Nx,
qquad G_Nsucc0,
]

with

[
H_{N,c}=G_N^{-1/2}S_{N,c}G_N^{-1/2}.
]

The required arithmetic content is that (S_{N,c}) be derived from pole, archimedean, and prime-power data without using the zeta ordinates as fitted parameters.

## Load-bearing questions

1. Can the published Prime–Weil matrix be reconstructed exactly from the normalization already audited in this repository?
2. Does the fixed zero-mean/contrast quotient coincide with the repository's pole-neutral constraints?
3. Can the prime-power contribution be written as an exact trace/distributional identity?
4. Does the resulting finite pencil admit a limit with sufficient self-adjoint spectral convergence?
5. Can the limiting spectral measure be identified exactly with the nontrivial zeta ordinates?
6. Can the operator formulation be shown equivalent to the repository's Weil positivity formulation rather than merely numerically correlated with it?

## Negative-control rule

Known zeta ordinates may be used only in a quarantined zero-side reconstruction/control experiment.

They must never be used to tune the arithmetic matrix, select its parameters, or claim spectral evidence for an independently derived Hamiltonian.

## Status

**CANDIDATE / OPEN.**

This log records a research direction and exact obligations, not a theorem.

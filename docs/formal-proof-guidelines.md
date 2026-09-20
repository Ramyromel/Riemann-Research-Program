# Formal Proof Guidelines

## Purpose

This document defines the minimum standard for promoting a mathematical claim in the Riemann Research Program from DERIVED or VERIFIED to PROVED.

The repository does not treat numerical agreement, finite-dimensional positive definiteness, self-adjointness, or asymptotic plausibility as substitutes for a complete theorem.

## Function-space discipline

Every theorem must state the exact function space being used. In particular, distinguish explicitly between:

- $C_c^\infty(\mathbb{R})$: smooth compactly supported functions;
- $\mathcal{S}(\mathbb{R})$: Schwartz functions;
- real/even/odd subspaces;
- any admissibility or pole-neutral subspace;
- finite-dimensional Galerkin subspaces.

A proof must not silently replace one space by another.

## Proof checklist

Before a claim is marked PROVED, the following must be explicit:

1. **Statement** — exact mathematical proposition.
2. **Domain** — complete definition of every function/operator/form domain.
3. **Hypotheses** — every assumption, parameter range, regularity condition, and boundary condition.
4. **Normalization** — Fourier/Mellin conventions, constants, signs, and scaling.
5. **Dependencies** — every external theorem is cited with the exact version and hypotheses used.
6. **Finite construction** — matrix/operator definition and parameter dependence.
7. **Limit mechanism** — topology, mode of convergence, and common or variable domains.
8. **Uniform control** — explicit bounds where an interchange of limits, sums, integrals, derivatives, or quadratic forms is required.
9. **Globalization** — proof that the finite/test-function family reaches the exact target class required by the Weil criterion.
10. **Arithmetic identification** — exact correspondence to the zeta-side or prime-side object.
11. **No hidden sector** — even/odd or other symmetry sectors are handled or their exclusion is mathematically justified.
12. **Independent check** — an independent derivation, formal verification, or line-by-line audit is required for a load-bearing new theorem.

## Status rule

A claim remains DERIVED, VERIFIED, NUMERICALLY_SUPPORTED, or BLOCKED if any load-bearing item above is unresolved.

In particular:

- finite positivity does not imply global positivity;
- pointwise convergence does not imply uniform convergence;
- self-adjointness does not by itself identify a zeta spectrum;
- an asymptotic estimate does not supply a finite-parameter bound;
- numerical zero matching does not prove a spectral correspondence.

## Promotion rule

Only a complete argument with all load-bearing dependencies closed may be labeled PROVED. The repository must record the exact proof boundary and any external assumptions.

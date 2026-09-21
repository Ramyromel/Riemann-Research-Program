# Hilbert–Pólya Finite-Matrix Route

**Status:** ACTIVE RESEARCH — CANDIDATE FINITE SPECTRAL MODEL — NO RH CLAIM

## 1. Research decision

The project now opens an independent Hilbert–Pólya track, but it remains coupled to the existing Weil program at the level of exact arithmetic data.

The first target is **not** an arbitrary Hamiltonian such as the formal Berry–Keating (xp) operator. The first target is a finite, explicitly defined, real-symmetric arithmetic matrix constructed from the same Weil data already audited in this repository.

A recent external construction by Yaoming Shi, arXiv:2609.04908 (2026), provides a directly relevant finite model: real-symmetric Prime–Weil matrices built from pole, archimedean, and finite prime-power data, followed by a Hermitian definite generalized eigenproblem on a fixed zero-mean contrast space. The paper explicitly states that its zero-ordinate reconstruction uses the ordinates as inputs and does not prove RH.

## 2. Canonical finite object

Let (S_{N,c}) denote a finite Prime–Weil matrix at Galerkin dimension (N) and arithmetic cutoff (c), with the construction fixed by the audited Weil normalization.

The Hilbert–Pólya candidate is a **pencil**, not automatically (S_{N,c}) itself:

[
S_{N,c}x=lambda,G_Nx,
qquad
xinmathcal C_N,
]

where:

- (G_N) is the positive-definite metric required by the finite spectral quotient;
- (mathcal C_N) is the fixed zero-mean/contrast space;
- (S_{N,c}=S_{N,c}^{mathsf T});
- (G_N=G_N^{mathsf T}succ0).

The associated finite Hamiltonian is the (G_N)-self-adjoint operator

[
H_{N,c}=G_N^{-1/2}S_{N,c}G_N^{-1/2}
]

on the quotient space.

This definition is preferable to simply declaring (H=S), because the generalized eigenproblem preserves the finite quotient structure and makes the metric explicit.

## 3. What would count as genuine progress

A finite matrix with real eigenvalues is only the first layer.

The research obligations are:

### HP-1 — Exact finite construction
Derive every entry of (S_{N,c}) from the project normalization. No fitted coefficients.

### HP-2 — Hermitian/self-adjoint finite realization
Prove (S=S^{mathsf T}) and (Gsucc0), then verify the induced (H) is self-adjoint in the standard inner product.

### HP-3 — Arithmetic trace identity
Find a test-function class for which

[
operatorname{Tr}f(H_{N,c})
]

or the corresponding generalized trace reproduces the finite prime-power, pole, and archimedean terms with the correct signs and normalizations.

Prime-power coefficients must arise structurally from (Lambda(p^k)), not from fitting known zero ordinates.

### HP-4 — Spectral identification
Prove, rather than fit, that the limiting spectral measure is the nontrivial-zero measure

[
sum_gamma delta_gamma
]

with multiplicities.

### HP-5 — Limit control
Establish a mathematically sufficient operator convergence statement as (N,c	oinfty), including domains and spectral consequences.

### HP-6 — No spurious spectrum
Show that the limiting construction neither loses required zero ordinates nor introduces unrelated spectral components.

## 4. Zero-data reconstruction must be quarantined

A zero-side matrix built directly from known ordinates can be useful as a control experiment, but it is **not** an arithmetic derivation of a Hamiltonian.

If (gamma_1,ldots,gamma_N) are supplied as inputs and a finite pencil is constructed whose spectrum is exactly ({pmgamma_k}), the result is a reconstruction theorem.

It must therefore be reported separately from the arithmetic candidate.

This distinction is essential for preventing circularity.

## 5. Connection to the existing Weil route

The existing repository already established a finite Guinand–Weil dictionary and exact pole-neutral reductions. The Hilbert–Pólya route should reuse that structure.

The desired bridge is:

[
	ext{finite Weil data}
longrightarrow
(S_{N,c},G_N)
longrightarrow
H_{N,c}
longrightarrow
	ext{operator limit}
longrightarrow
	ext{zeta spectral measure}.
]

The same construction should also remain compatible with

[
Q_{mathrm{Weil}}(f)
leftrightarrow
	ext{spectral quadratic form}.
]

If the two routes require incompatible normalizations, domains, or limits, that incompatibility is itself a falsification result.

## 6. Immediate falsification tests

The candidate is downgraded or rejected if any of the following is established:

1. (G_N) ceases to be positive definite on the declared quotient.
2. (S_{N,c}) is not exactly symmetric under the stated normalization.
3. the prime-power trace coefficients cannot be derived exactly;
4. spectral matching to known zeros requires fitted parameters;
5. different admissible finite constructions have incompatible limits;
6. trace convergence holds but the required spectral/resolvent convergence fails;
7. boundary or parity terms carry uncontrolled spectral mass;
8. the limiting spectrum contains persistent non-zeta components.

## 7. Current status

**CANDIDATE / DERIVED RESEARCH DESIGN.**

No self-adjoint infinite-dimensional Hamiltonian has been constructed here.

No RH implication has been proved.

The next implementation step is to instantiate the finite pencil from the repository's exact finite Weil normalization and independently compare it with the published Prime–Weil construction. Any discrepancy must be documented before numerical spectral work is interpreted.

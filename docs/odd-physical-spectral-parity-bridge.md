# Odd physical/spectral parity bridge

## Status

**NUMERICALLY SUPPORTED; ANALYTIC IDENTIFICATION STILL OPEN.**

The direct physical odd basis is

[
e_k(x)=sin(kpi x),qquad -1<x<1.
]

The repository Volterra coordinate uses (w=(x+1)/2). Therefore

[
e_k(2w-1)
=sin(2pi k w-kpi)
=(-1)^ksin(2pi k w).
]

Hence the coordinate-change matrix between the physical sine basis and the
repository odd sine basis is the diagonal involution

[
D=operatorname{diag}((-1)^1,(-1)^2,ldots,(-1)^N),qquad D^2=I.
]

Consequently, if (A_{m odd}) denotes the matrix produced in the repository
(w)-coordinate and (A_{m phys}) the same operator in the physical
(x)-coordinate, the basis relation predicts

[
A_{m phys}=D A_{m odd}D.
]

This is a **basis-conjugation statement**, not a new positivity theorem.

## Independent numerical check

At (c=20, N=6), using a direct critical-line spectral integral with
(R=500) and (100001) quadrature points,

- (lambda_{min}(A_{m phys})=-1.4606167723436219)
- (lambda_{min}(D A_{m odd}D)=-1.4606167016519247)
- Frobenius residual: (2.5567112018101907	imes10^{-6})
- maximum entry residual: (1.352693253076076	imes10^{-6})

The residual is consistent with finite spectral-window / numerical truncation
error at this stage, but this does **not** establish an exact identity.

## Critical correction

Before applying (D), the candidate had an apparent large residual

[
|A_{m odd}-A_{m phys}|_Fapprox 0.784,
]

with a structured alternating-sign pattern in off-diagonal entries. The
explicit basis identity above explains that pattern. This supersedes the
earlier interpretation that the mismatch necessarily represented a failure
of the odd resolvent itself.

## Remaining analytic obligation

The numerical agreement must still be replaced by a derivation from the
repository's explicit-formula normalization:

1. derive the odd Fourier/Mellin transform;
2. derive the autocorrelation sign exactly;
3. derive the (wleftrightarrow x) basis map;
4. derive the Volterra/resolvent expansion term-by-term;
5. prove equality with the physical Archimedean form;
6. only then combine with the prime block and pole-neutral constraints.

Until those steps are completed, the result remains
**NUMERICALLY_SUPPORTED**, not VERIFIED as an operator identity.

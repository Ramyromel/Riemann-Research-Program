# 2026-09-22 — Sum-Level Convolution/Hankel Operator

## Objective

Close the first mathematical subtask of Issue #22: derive the finite-dimensional operator induced by the exact Prime–Weil sum-level kernel.

## Exact starting point

The audited finite prime contribution is

\[
Q_{\mathrm{prime}}(v;c)
=
-\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}
K_v(\omega_q),
\qquad
\omega_q=1-\frac{\log q}{\log c},
\]

with

\[
K_v(\omega)
=
2\int_0^\omega T_v(t)T_v(\omega-t)\,dt.
\]

Use the real-even basis

\[
\phi_0(t)=1,
\qquad
\phi_k(t)=\sqrt2\cos(2\pi kt).
\]

Define

\[
B_{ij}(\omega)
=
\int_0^\omega
\phi_i(t)\phi_j(\omega-t)\,dt.
\]

Then

\[
K_v(\omega)=2v^{\mathsf T}B(\omega)v
\]

and the exact finite prime matrix is

\[
H^{\mathrm{prime}}_{N,c}
=
-2\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}
B(\omega_q).
\]

Therefore

\[
Q_{\mathrm{prime}}(v;c)
=
v^{\mathsf T}H^{\mathrm{prime}}_{N,c}v.
\]

## Exact closed form

For

\[
\phi_i(t)=\sum_m c_{i,m}e^{2\pi imt},
\]

define

\[
D_d(\omega)=
\begin{cases}
\omega,&d=0,\\
\frac{e^{2\pi id\omega}-1}{2\pi i d},&d\ne0.
\end{cases}
\]

Then

\[
B_{ij}(\omega)
=
\sum_{m,n}
c_{i,m}c_{j,n}
e^{2\pi in\omega}D_{m-n}(\omega).
\]

This is an exact finite Galerkin formula, evaluated with arbitrary precision in the implementation.

## Operator interpretation

The corresponding distributional kernel is

\[
H_c(t,s)
=
-2\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}
\delta(t+s-\omega_q).
\]

Hence the arithmetic object is a weighted discrete **Hankel/sum-level operator**. It is not the previously tested pairwise source-overlap Gram matrix.

This resolves the structural ambiguity identified in PR #21: the natural intersections are constrained by

\[
t+s=\omega_q,
\]

not by an independent source-pair overlap.

## Independent verification

A separate high-precision quadrature implementation was used to evaluate

\[
-\sum_q\frac{\Lambda(q)}{\sqrt q}K_v(\omega_q)
\]

directly from the cosine expansion of \(T_v\).

For \(c=30\), \(N=3\), and a nontrivial deterministic test vector, the matrix and independent quadrature values agreed to approximately

\[
6.8\times10^{-62}
\]

at 60 decimal digits.

Additional checks:

- the constructed matrix is symmetric to the working precision;
- prime-power enumeration is independently checked through \(c=20\);
- construction contains no zeta-zero ordinates or zero-dependent fitting;
- no positivity conclusion is drawn.

## Research classification

- Exact finite sum-level/Hankel representation: **DERIVED**
- Independent numerical audit of the identity: **VERIFIED**
- Positivity of the prime block: **OPEN**
- Joint prime–archimedean positivity: **OPEN**
- Infinite-dimensional operator identification: **OPEN**
- RH: **OPEN**

The result advances the operator construction but does not close the load-bearing positivity or limit gaps.

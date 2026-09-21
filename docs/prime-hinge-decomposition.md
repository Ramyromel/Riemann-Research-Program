# Prime-Path Hinge Decomposition — Finite Even Sector

**Status:** DERIVED PARTIAL STRUCTURAL REDUCTION  
**Scope:** fixed Galerkin level \(N\), cutoff-free prime block as a function of \(u=\log c\)  
**Does not prove:** finite positivity, global Weil positivity, or RH

## 1. Starting point

The audited external structural result gives, at every prime-power threshold
\[
u_q=\log q,
\]
the derivative jump
\[
\Delta P_N'(u_q)
=
-\frac{2\Lambda(q)}{\sqrt q\,\log q}\,J,
\qquad
J=\mathbf1\mathbf1^{\mathsf T}\succeq0.
\]

The singular part of the second derivative is therefore
\[
(P_N'')_{\mathrm{sing}}
=
-2J\sum_q
\frac{\Lambda(q)}{\sqrt q\,\log q}\,
\delta_{\log q}.
\]

## 2. Correct distributional decomposition

The jump measure alone does **not** justify treating the entire prime path as piecewise affine. The exact external result identifies the singular arithmetic measure; it does not, by itself, eliminate a possible absolutely-continuous/smooth part of \(P_N''\).

Accordingly, the rigorous decomposition is
\[
P_N(u)
=
A_N^{(0)}+uB_N^{(0)}
+
R_N(u)
-
2J
\sum_q
\frac{\Lambda(q)}{\sqrt q\,\log q}
(u-\log q)_+,
\]
where \(R_N\) is the remaining twice-integrated absolutely-continuous/smooth contribution, if present under the chosen finite-matrix convention.

The exact source formula must determine \(R_N\), \(A_N^{(0)}\), and \(B_N^{(0)}\). They must not be inferred from numerical fitting.

This correction is deliberate: the project now distinguishes the **certified singular arithmetic component** from the unclassified regular component.

## 3. What is nevertheless proved

For every vector \(v\),
\[
v^{\mathsf T}(P_N'')_{\mathrm{sing}}v
=
-2(\mathbf1^{\mathsf T}v)^2
\sum_q
\frac{\Lambda(q)}{\sqrt q\,\log q}
\delta_{\log q}
\le0.
\]

Thus the arithmetic singular curvature is negative semidefinite and rank one at every prime-power event.

The cumulative singular contribution is exactly
\[
-H(u)J,
\]
with
\[
H(u)=
2\sum_{q=p^a}
\frac{\Lambda(q)}{\sqrt q\,\log q}
(u-\log q)_+.
\]

This is a genuine structural extraction even without classifying \(R_N\).

## 4. Pole-neutral interaction becomes the next decisive test

Let \(\mathcal V_{N,\mathrm{PN}}\) be the exact finite pole-neutral subspace.

The rank-one operator \(J\) acts through
\[
v^{\mathsf T}Jv=(\mathbf1^{\mathsf T}v)^2.
\]

Therefore the next exact question is whether
\[
\mathbf1^{\mathsf T}v=0
\quad\text{for every }v\in\mathcal V_{N,\mathrm{PN}}.
\]

Two cases follow:

### Case A — \(J\) is annihilated

If the pole-neutral constraints imply
\[
\mathbf1^{\mathsf T}v=0,
\]
then the entire singular prime-power curvature vanishes after restriction. The finite positivity problem must then be controlled by the regular prime component, pole term, and archimedean term.

### Case B — \(J\) survives

If there exists admissible \(v\) with
\[
\mathbf1^{\mathsf T}v\ne0,
\]
then the restricted form contains the explicit negative arithmetic term
\[
-H(u)(\mathbf1^{\mathsf T}v)^2.
\]

Any uniform positivity theorem must exhibit an explicit compensating positive contribution.

This is a finite-dimensional, directly testable dichotomy.

## 5. Revised load-bearing target

The previous target
\[
A_N\succeq-P_N(u)
\]
is equivalent to finite positivity but hides the arithmetic structure.

The sharper target is now:

1. compute the exact pole-neutral constraint matrix;
2. compute its interaction with \(\mathbf1\);
3. classify \(J\) as annihilated or surviving;
4. derive the exact regular component \(R_N\);
5. only then seek a Gram/Schur/Loewner representation or a uniform lower bound.

This ordering prevents an invalid inference from the singular jump theorem to full-path positivity.

## 6. Classification

- Prime-power jump identity: **EXTERNAL THEOREM UNDER PROJECT AUDIT**.
- Negative-semidefinite rank-one singular measure: **DERIVED**.
- Hinge representation of the singular component: **DERIVED**.
- Full prime path as piecewise affine: **NOT ASSUMED**.
- Pole-neutral interaction with \(J\): **OPEN — NEXT SUBTARGET**.
- Full finite positivity: **OPEN / LOAD-BEARING**.
- Global Weil positivity: **OPEN**.
- RH: **OPEN**.

No RH inference is made.

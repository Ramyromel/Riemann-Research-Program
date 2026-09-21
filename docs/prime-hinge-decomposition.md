# Prime-Path Hinge Decomposition — Finite Even Sector

**Status:** DERIVED STRUCTURAL REDUCTION  
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

Here \(P_N(u)\) denotes the finite prime contribution to the cutoff-free matrix.

## 2. Distributional integration

A piecewise-affine function whose derivative has jumps \(a_q\) admits the hinge representation
\[
P_N(u)
=
A_N^{(0)}+uB_N^{(0)}
+
\sum_{q}
a_q\,(u-\log q)_+,
\]
where
\[
(x)_+=\max(x,0),
\]
and the sum is locally finite in \(u\).

Substituting the exact jump coefficients gives
\[
\boxed{
P_N(u)
=
A_N^{(0)}+uB_N^{(0)}
-
2J
\sum_{q=p^a}
\frac{\Lambda(q)}{\sqrt q\,\log q}
(u-\log q)_+ .
}
\]

The matrices \(A_N^{(0)}\) and \(B_N^{(0)}\) are the two integration constants determined by the exact finite source formula and the chosen reference interval. They must not be guessed from numerical fits.

## 3. Immediate consequence

The entire nonlinear arithmetic dependence on the prime cutoff has now been isolated into the scalar function
\[
H(u)
=
2\sum_{q=p^a}
\frac{\Lambda(q)}{\sqrt q\,\log q}
(u-\log q)_+,
\]
so that
\[
P_N(u)=A_N^{(0)}+uB_N^{(0)}-H(u)J.
\]

Thus every prime-power event acts only in the single matrix direction \(J\).

For any vector \(v\),
\[
v^{\mathsf T}P_N(u)v
=
v^{\mathsf T}(A_N^{(0)}+uB_N^{(0)})v
-
H(u)\,(\mathbf1^{\mathsf T}v)^2.
\]

This is stronger than merely saying that the prime block is Loewner-concave: its entire singular arithmetic curvature is rank one.

## 4. Interaction with the pole-neutral subspace

Let \(\mathcal V_{N,\mathrm{PN}}\) denote the exact finite pole-neutral subspace.

The rank-one direction \(J\) must now be compared with the two pole/moment constraints. There are two logically distinct possibilities:

1. \(J\) vanishes on the pole-neutral subspace. Then the prime-power curvature disappears after restriction, and the remaining finite positivity problem has a fundamentally different structure.
2. \(J\) survives on that subspace. Then the full positivity problem contains the explicit negative scalar term
   \[
   -H(u)(\mathbf1^{\mathsf T}v)^2,
   \]
   and any proposed uniform positivity proof must supply an equally explicit compensating positive term.

This distinction is testable directly from the exact constraint matrix and should be resolved before attempting an all-\((c,N)\) inequality.

## 5. Load-bearing reduction

With
\[
Q_N(u)=A_N+P_N(u),
\]
the finite positivity target becomes
\[
v^{\mathsf T}Q_N(u)v\ge0
\]
for every admissible \(v\).

Using the hinge form,
\[
v^{\mathsf T}Q_N(u)v
=
v^{\mathsf T}\!\left(A_N+A_N^{(0)}+uB_N^{(0)}\right)v
-
H(u)(\mathbf1^{\mathsf T}v)^2.
\]

Therefore a sufficient analytic theorem is a scalar/vector inequality of the form
\[
v^{\mathsf T}\!\left(A_N+A_N^{(0)}+uB_N^{(0)}\right)v
\ge
H(u)(\mathbf1^{\mathsf T}v)^2
\]
on the exact pole-neutral space.

This separates the arithmetic difficulty from the finite harmonic-analysis difficulty.

## 6. Important limitation

The hinge representation does **not** determine the integration constants \(A_N^{(0)},B_N^{(0)}\). The derivative-jump theorem alone therefore cannot prove positivity.

The next exact task is to derive those constants from the primary finite source formula, then test whether the pole-neutral constraints annihilate or retain the \(J\)-direction.

## 7. Classification

- Prime-power jump identity: **EXTERNAL THEOREM UNDER PROJECT AUDIT**.
- Hinge integration of the jump measure: **DERIVED**.
- Rank-one arithmetic curvature: **DERIVED**.
- Pole-neutral interaction with \(J\): **OPEN — NEXT SUBTARGET**.
- Finite positivity: **OPEN / LOAD-BEARING**.
- Global Weil positivity: **OPEN**.
- RH: **OPEN**.

No RH inference is made.

# Pole-Neutral Cancellation of the Prime-Power Singular Curvature

**Status:** DERIVED — VERIFIED AGAINST EXTERNAL PRIMARY FORMULAS  
**Scope:** finite real-even Galerkin sector and the exact pole-neutral family  
**Does not prove:** finite positivity, global Weil positivity, or RH

## 1. External finite construction

Use the standard even embedding
\[
u_0=v_0,\qquad
u_k=u_{-k}=\frac{v_k}{\sqrt2},
\qquad 1\le k\le N.
\]

The exact pole-neutral moment appearing in the finite Guinand–Weil construction is
\[
M_0(v)
=
v_0+\sqrt2\sum_{k=1}^{N}v_k.
\]

The pole-neutral family imposes \(M_0(v)=0\), together with the remaining moment/pole constraints required by the selected subfamily.

## 2. The rank-one jump direction is exactly the \(M_0\) direction

The audited prime-power jump has the full-coordinate form
\[
\Delta Q_N'(u_q)
=
-\frac{2\Lambda(q)}{\sqrt q\,\log q}\,
\mathbf1\mathbf1^{\mathsf T}.
\]

For the embedded even vector \(u\),
\[
\mathbf1^{\mathsf T}u
=
u_0+\sum_{k=1}^{N}(u_k+u_{-k})
=
v_0+\sqrt2\sum_{k=1}^{N}v_k
=
M_0(v).
\]

Therefore
\[
u^{\mathsf T}\mathbf1\mathbf1^{\mathsf T}u
=
M_0(v)^2.
\]

Consequently the singular arithmetic curvature acts on the even sector through the single scalar \(M_0(v)^2\).

## 3. Exact cancellation on the pole-neutral family

For every pole-neutral vector satisfying \(M_0(v)=0\),
\[
u^{\mathsf T}\mathbf1\mathbf1^{\mathsf T}u=0.
\]

Hence every prime-power singular jump vanishes after restriction:
\[
v^{\mathsf T}\Delta Q_N'(u_q)v=0.
\]

Equivalently,
\[
v^{\mathsf T}(Q_N'')_{\mathrm{sing}}v=0
\]
as a measure in \(u\) for every admissible pole-neutral \(v\).

This is stronger than merely knowing that the singular curvature is negative semidefinite: **its quadratic action is identically zero on this restricted family.**

## 4. Independent pole cancellation

The external finite construction gives the pole quadratic form
\[
\langle v,Q_{\mathrm{pole}}v\rangle
=
C_c\beta^2
\left(
\frac{v_0}{\beta^2}
+
\sqrt2\sum_{k=1}^{N}\frac{v_k}{k^2+\beta^2}
\right)^2,
\]
with
\[
\beta=\frac{\log c}{4\pi},
\qquad
C_c>0.
\]

Thus the exact pole-neutral row also annihilates the pole quadratic form.

Therefore, on the pole-neutral family:

- the **pole contribution vanishes**;
- the **prime-power singular curvature vanishes**.

The remaining sign problem is consequently not a competition between a cumulative rank-one negative prime curvature and a pole term.

## 5. What remains

After these two cancellations, the load-bearing finite problem is reduced to the regular prime contribution plus the archimedean contribution on the exact constrained space.

The next theorem target is therefore:

\[
Q_{\mathrm{restricted}}
=
Q_{\mathrm{prime,regular}}
+
Q_{\mathrm{arch},\infty}
\succeq0
\]

for the required finite family, with all dependence on \(c,N\) explicit.

This must be derived from the exact source formulas; it cannot be inferred from the vanishing singular measure.

## 6. Consequence for the research strategy

The earlier strategy of proving
\[
A_N\succeq-P_N(u)
\]
uniformly was too coarse on the pole-neutral route.

The sharper sequence is now:

1. impose \(M_0=0\) exactly;
2. remove the vanishing pole block;
3. remove the vanishing singular prime-power curvature;
4. identify the remaining regular prime kernel;
5. combine it with the archimedean kernel;
6. seek a Gram/Loewner/Schur representation or a rigorous lower bound;
7. attack the resulting statement with certified counterexamples if necessary.

## 7. Classification

- Prime-power jump identity: **EXTERNAL THEOREM UNDER PROJECT AUDIT**.
- \(M_0\)-identification: **VERIFIED AGAINST EXTERNAL PRIMARY FORMULAS**.
- Singular curvature cancellation on \(M_0=0\): **DERIVED**.
- Pole quadratic cancellation on the exact pole-neutral row: **VERIFIED AGAINST EXTERNAL PRIMARY FORMULAS**.
- Restricted finite positivity: **OPEN / LOAD-BEARING**.
- Odd sector: **OPEN**.
- Global Weil positivity: **OPEN**.
- RH: **OPEN**.

No RH inference is made.

# Prime-Path Concavity Lemma — Finite Even Sector

**Status:** EXTERNAL STRUCTURAL THEOREM UNDER PROJECT AUDIT  
**Scope:** fixed Galerkin level \(N\), cutoff-free finite matrix path \(u=\log c\)  
**Does not prove:** finite positivity, global Weil positivity, or RH

## 1. External structural input

A 2026 result of Akiva Groskin analyzes the cutoff-free finite Connes–van Suijlekom path \(u\mapsto Q_N(u)\). At each prime-power threshold \(u_q=\log q\), the first-derivative jump is

\[
\Delta Q_N'(u_q)
=
-\frac{2\Lambda(q)}{\sqrt q\,\log q}\,\mathbf 1\mathbf 1^{\mathsf T},
\]

where \(\mathbf 1\mathbf 1^{\mathsf T}\) is positive semidefinite and \(\Lambda(q)\ge0\).

Equivalently, the singular part of the second derivative is the negative-semidefinite matrix-valued measure

\[
Q_N''(u)_{\mathrm{sing}}
=
-\sum_q
\frac{2\Lambda(q)}{\sqrt q\,\log q}
\mathbf 1\mathbf 1^{\mathsf T}\,\delta_{\log q}.
\]

The statement is finite-dimensional and cutoff-free on the archimedean side. It identifies the arithmetic singularity exactly; it is not itself a positivity theorem.

## 2. Loewner consequence for the prime block

Because the prime contribution is piecewise affine in \(u\), its derivative is constant between prime-power events and decreases by a positive-semidefinite rank-one amount at every event.

Therefore the prime block is Loewner-concave as a distributional/piecewise-affine path:

\[
Q_{N,\mathrm{prime}}''\preceq0
\]

in the distributional sense.

This is a genuine structural constraint on the finite path.

## 3. Why this does not close T-006B

The full cutoff-free matrix is

\[
Q_N(u)=Q_{N,\mathrm{prime}}(u)+Q_{N,\mathrm{pole}}+Q_{N,\mathrm{arch},\infty}.
\]

The pole and archimedean terms do not acquire the prime-power jump structure. Hence the lemma reduces the sign problem to a compensation problem:

> Can the fixed positive/indefinite non-prime part dominate the cumulative negative arithmetic contribution on the exact pole-neutral subspace, uniformly in \(u\) and \(N\)?

A proof of this domination would be a load-bearing finite-positivity theorem. The concavity lemma alone does not imply it.

In particular, monotonicity of the prime block cannot be turned into positivity of the full matrix: a decreasing matrix path may remain positive, cross zero, or become indefinite.

## 4. A sharper reduction

Let

\[
A_N:=Q_{N,\mathrm{pole}}+Q_{N,\mathrm{arch},\infty}
\]

and let \(P_N(u)\) denote the prime block. Then

\[
Q_N(u)=A_N+P_N(u).
\]

If \(P_N'(u)\preceq0\) and \(P_N(u_0)=0\) at a reference cutoff \(u_0\) before the first prime-power event, then

\[
Q_N(u)
=
A_N+
\int_{u_0}^{u}P_N'(t)\,dt.
\]

Thus a sufficient condition for \(Q_N(u)\succeq0\) is the operator inequality

\[
A_N\succeq -P_N(u)
\]

on the admissible subspace for every \(u\).

This is the exact finite sign target after the arithmetic path structure has been extracted.

## 5. Research consequence

The next analytic attack should therefore not be “prove positivity from the jump signs.” It should be one of:

1. factor \(A_N+P_N(u)\) as a Gram/Schur complement;
2. derive a uniform lower bound on \(A_N+P_N(u)\);
3. identify a positive kernel whose integral representation equals the complete matrix;
4. reduce the obstruction to a finite-dimensional Schur complement and prove that complement positive;
5. find a certified negative direction, which would falsify the proposed universal finite-positivity route.

Any successful proof must include the exact pole-neutral restriction and uniform dependence on \(N\) and \(u\).

## 6. Correction to an earlier project note

An earlier repository status sentence described the second-derivative jump as positive semidefinite. That sign is incorrect for the external matrix-valued von Mangoldt measure.

The correct statement is **negative semidefinite**:

\[
Q_N''(u)_{\mathrm{sing}}\preceq0.
\]

The corrected sign is now treated as the authoritative project wording.

## 7. Classification

- **External theorem:** prime-power derivative jump identity.
- **Derived consequence under the external identity:** distributional Loewner concavity of the prime block.
- **Open:** domination by the pole/archimedean block.
- **Open:** all-\(N\), all-\(c\) even-sector positivity.
- **Open:** full Weil positivity and RH.

No RH inference is made.

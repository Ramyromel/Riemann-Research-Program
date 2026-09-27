# Archimedean Hankel Matrix on the Same Finite Basis

**Status:** DERIVED EXACT FINITE FORM + NUMERICAL INFINITE-SERIES EVALUATION  
**Scope:** real-even finite Galerkin sector  
**Does not prove:** archimedean positivity, finite Weil positivity, global Weil positivity, or RH

## 1. Purpose

The sum-level/Hankel experiment already gives the exact prime block on the cosine basis
[
phi_0(t)=1,qquad phi_k(t)=sqrt2cos(2pi kt).
]

The next requirement is to put the archimedean block on exactly the same finite basis, without changing normalization.

From the audited resolvent identity,
[
Q_{mathrm{arch},infty}(v;c)
=
rac{h_+(0)}2K_v(1)
+
sum_{nge0}
left[
rac{K_v(1)}{2a_n}
-
Lint_0^1K_v(omega)e^{-2La_n(1-omega)},domega
ight],
quad
a_n=n+rac14.
]

For the orthonormal cosine basis,
[
K_{ij}(omega)=2B_{ij}(omega),
qquad
B_{ij}(omega)=int_0^omegaphi_i(t)phi_j(omega-t),dt,
]
and
[
K_{ij}(1)=2delta_{ij}.
]

Therefore the archimedean matrix is exactly
[
oxed{
A^{mathrm{arch}}_{ij}
=
h_+(0)delta_{ij}
+
sum_{nge0}
left[
rac{delta_{ij}}{a_n}
-
2Lint_0^1
B_{ij}(omega)e^{-2La_n(1-omega)},domega
ight].
}
]

This is a matrix identity, not a numerical fit.

## 2. Finite Fourier evaluation

Each (B_{ij}) is a finite sum of exponentials and (w e^{2pi ialpha w}). Consequently the Laplace integral above is also evaluated in closed finite form.

For integer (alpha), set
[

u=A+2pi ialpha.
]
Then
[
int_0^1e^{-A(1-w)}e^{2pi ialpha w},dw
=
rac{e^{2pi ialpha}-e^{-A}}{
u},
]
and
[
int_0^1w,e^{-A(1-w)}e^{2pi ialpha w},dw
=
rac{e^{2pi ialpha}(
u-1)+e^{-A}}{
u^2}.
]

Thus no numerical quadrature is required for the inner Laplace integral. Only truncation of the outer resolvent series remains.

## 3. Pole-neutral restriction

The pole parameter is
[
eta=rac{log c}{4pi}.
]

The restricted subspace is defined by
[
v_0+sqrt2sum_{k=1}^Nv_k=0
]
and
[
rac{v_0}{eta^2}
+
sqrt2sum_{k=1}^N
rac{v_k}{k^2+eta^2}
=0.
]

The first removes the singular prime-power curvature direction; the second removes the pole quadratic form.

The earlier exploratory calculation that used a fixed (eta=1/2) was incorrect. It produced spurious negative directions and has been discarded. With the exact (eta(c)), the restricted combined matrix moves toward a nonnegative spectrum as the resolvent truncation is increased.

## 4. Current numerical observation

At (c=20), using the exact (eta(c)), the restricted total matrix
[
P^{(c,N)}+A^{mathrm{arch},(c,N)}
]
has, for example, a single restricted eigenvalue for (N=2) that is approximately

- (3.63	imes10^{-5}) at (10^3) resolvent terms;
- (3.76	imes10^{-5}) at (3	imes10^3);
- (3.76	imes10^{-5}) at (10^4).

For larger (N), several restricted eigenvalues are numerically close to zero. These observations are **not** a positivity theorem: the archimedean series is truncated, and the finite prime block itself is only one component of the full proof architecture.

The intended near-zero modes were observed only with the previously broken restricted-basis implementation. Those numerical observations are invalidated pending recomputation with the corrected nullspace basis. The two exact pole-neutral constraints still reduce the dimension by two. They should be investigated as possible null/near-null directions before any Gram factorization is attempted.

## 5. Next load-bearing target

The next target is not “prove positivity from eigenvalues.” It is:

1. derive the exact restricted combined kernel;
2. identify whether the near-null directions have an analytic description;
3. seek an exact Gram/Schur factorization of the combined prime–archimedean operator;
4. derive a certified tail bound for the outer resolvent series;
5. test the resulting identity against independent direct evaluation.

Any failure will be recorded as an obstruction rather than absorbed into a numerical claim.

## 6. Verification boundary

- Basis normalization: **VERIFIED / DERIVED**
- (K_{ij}(1)=2delta_{ij}): **DERIVED / TESTED**
- Inner Laplace integrals: **DERIVED EXACTLY**
- Outer series evaluation: **NUMERICALLY TRUNCATED**
- Pole-neutral parameter (eta(c)): **VERIFIED AGAINST PROJECT'S EXTERNAL NORMALIZATION**
- Restricted positivity: **OPEN**
- Global Weil positivity: **OPEN**
- RH: **OPEN**

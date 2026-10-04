# Support-monotone route: replacing the Galerkin limit by exact compression

**Status: TARGET / UNVERIFIED**

## Motivation

The finite Galerkin route has reached a structurally important point: at N=3
the smallest restricted eigenvalue moves toward zero as the Archimedean
resolvent cutoff increases. This makes the finite-dimensional limit itself
the wrong object to treat as the final proof mechanism.

A different route is to work directly with the localized Weil operator at
physical logarithmic support radius (a). If the quadratic form satisfies
an exact zero-extension compression law

[
E_{a,b}^{*}A_bE_{a,b}=A_a,qquad 0<a<b,
]

then positivity at any cofinal sequence (a_j\to\infty) implies positivity
at every finite (a). This removes the need to prove a delicate
(N\to\infty) Galerkin spectral convergence theorem.

## Normalization target

In the repository finite formulation,

[
L=\log c,
]

and the source coordinate is

[
\omega_q=1-\frac{\log q}{L}.
]

The corresponding physical support radius is

[
a=\frac{L}{2}.
]

Thus increasing (c) is equivalent to increasing the physical support
radius. The prime-power activation threshold is

[
\log q < 2a.
]

For a test function supported in ([-a,a]), a newly activated translation
with shift (\log q>2a) has no old--old overlap. This is the arithmetic
mechanism that could make compression exact.

## What must be proved independently

### 1. Archimedean block

Show that the change produced by extending a test function by zero from
([-a,a]) to ([-b,b]) is exactly canceled by the corresponding change in
the endpoint/potential part of the archimedean functional.

This must be derived in the repository's Fourier/Mellin normalization, not
imported from another paper.

### 2. Polar block

The pole-neutral formulation used by the finite matrices must be reconciled
with the physical localized polar rank-one term. The physical polar profile
must be tracked before any rescaling so that zero extension is an actual
restriction identity.

### 3. Prime-power block

For every old prime power (q<e^{2a}), its contribution is unchanged.
For every newly activated (qin(e^{2a},e^{2b})), prove that its old--old
overlap vanishes under zero extension.

### 4. Full compression

Combine the three blocks to obtain

[
\boxed{E_{a,b}^{*}A_bE_{a,b}=A_a}.
]

Only after this identity is established can the following reduction be used.

## Cofinal-support reduction

If (a_j\to\infty) and (A_{a_j}\succeq0) for every (j), then for any
finite (a), choose (j) with (a<a_j) and use

[
\langle f,A_af\rangle
=
\langle E_{a,a_j}f,A_{a_j}E_{a,a_j}f\rangle
\ge0.
]

Therefore

[
\boxed{
A_{a_j}\succeq0 	ext{on a cofinal sequence}
\Longrightarrow
A_a\succeq0 	ext{for every finite }a.
}
]

This is a structural reduction, not yet a theorem of the repository.

## Strategic consequence

If the compression identity is proved, the principal load-bearing problem
changes from

[
\text{finite positivity}+
(N\to\infty\text{ spectral convergence})
]

to

[
\text{positivity at a cofinal sequence of physical support endpoints}.
]

That is potentially a substantially cleaner route because support growth is
naturally synchronized with prime-power activation.

The N=2 and N=3 Galerkin experiments remain useful as diagnostics for the
local operator, but they no longer need to carry the global limit argument.

## External lead — audit only

A September 2026 preprint, *The Three Gates: A Rooted-Operator Approach
to Weil Positivity* (arXiv:2609.20367v2), explicitly uses an exact
zero-extension compression identity and a cofinal-support reduction before
its own Schur-induction argument. Its existence is a research lead only.
No theorem from that work is treated as established here; every identity
needed by this repository must be re-derived and normalized independently.

## Verification boundary

- (a=L/2): **DERIVED from repository normalization**
- prime activation threshold (\log q=2a): **DERIVED**
- exact full compression identity: **UNVERIFIED**
- cofinal-support reduction in this repository: **TARGET**
- positivity at a cofinal sequence: **OPEN**
- global Weil positivity: **OPEN**
- RH: **OPEN**

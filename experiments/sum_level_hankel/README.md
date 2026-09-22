# Sum-Level Prime–Weil Hankel Operator

**Status:** DERIVED EXACT FINITE REPRESENTATION + INDEPENDENT NUMERICAL AUDIT  
**Scope:** real-even Galerkin sector, finite prime-power cutoff (c)  
**No RH claim. No zero ordinates are used in construction.**

## Purpose

The prime part of the audited finite Weil form is

[
Q_{\mathrm{prime}}(v;c)
=
-\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}
K_v(\omega_q),
qquad
\omega_q=1-\frac{\log q}{\log c},
]

with

[
K_v(\omega)
=
2\int_0^\omega T_v(t)T_v(\omega-t)\,dt.
]

The correct operator structure is therefore **sum-level/Hankel**, not the previously rejected pairwise source-overlap Gram ansatz.

For the real-even cosine basis

[
\phi_0(t)=1,
qquad
\phi_k(t)=\sqrt2\cos(2\pi kt),quad 1\le k\le N,
]

write

[
T_v(t)=\sum_{i=0}^{N}v_i\phi_i(t).
]

Define the exact bilinear kernel

[
B_{ij}(\omega)
=
\int_0^\omega
\phi_i(t)\phi_j(\omega-t)\,dt.
]

Then

[
K_v(\omega)
=
2v^{\mathsf T}B(\omega)v,
]

and hence the exact finite prime matrix is

[
\boxed{
H^{\mathrm{prime}}_{N,c}
=
-2\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}
B(\omega_q)
}
]

with

[
Q_{\mathrm{prime}}(v;c)
=
v^{\mathsf T}H^{\mathrm{prime}}_{N,c}v.
]

The matrix is symmetric because

[
B_{ij}(\omega)
=
\int_0^\omega\phi_i(t)\phi_j(\omega-t)dt
=
B_{ji}(\omega)
]

after the substitution (t\mapsto\omega-t).

## Exact closed form used by the implementation

Let

[
\phi_i(t)=\sum_m c_{i,m}e^{2\pi imt},
]

where

[
c_{0,0}=1,
qquad
c_{k,k}=c_{k,-k}=1/\sqrt2.
]

For (d=m-n), define

[
D_d(\omega)=
\begin{cases}
\omega,&d=0,\\
\displaystyle
\frac{e^{2\pi id\omega}-1}{2\pi i d},&d\ne0.
\end{cases}
]

Then

[
B_{ij}(\omega)
=
\sum_{m,n}
c_{i,m}c_{j,n}
e^{2\pi in\omega}
D_{m-n}(\omega).
]

This is an exact finite formula; the implementation evaluates it with arbitrary precision.

## Structural conclusion

The operator kernel can be written distributionally as

[
H_c(t,s)
=
-2\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}
\delta(t+s-\omega_q),
]

on (0\le t,s\le1). Thus it is a **weighted discrete Hankel kernel** supported on the sum-level lines

[
t+s=\omega_q.
]

This directly captures the nontrivial content of the earlier intersection idea: the arithmetic data select sum-level intersections in the test-function coordinate.

It does **not** establish positivity. The weights have a fixed negative sign, while the bilinear Hankel blocks are indefinite in general.

## Audit rules

- No zeta zeros enter the matrix construction.
- No fitted parameters are permitted.
- No finite positivity observation is promoted to a theorem for all (c,N).
- This operator is an exact representation of the finite prime block, not an RH proof.
- The archimedean block remains a separate load-bearing component.

## Next theorem target

Combine this exact prime Hankel operator with an independently derived archimedean matrix on the same basis and test whether the pole-neutral restriction admits an exact positive-kernel/Schur-complement representation.

If such a representation cannot be derived, the route remains open rather than being promoted by numerical agreement.

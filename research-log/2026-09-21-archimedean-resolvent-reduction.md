# 2026-09-21 — Archimedean resolvent reduction

## Objective

Sharpen the load-bearing even-sector restricted positivity problem after the exact pole-neutral cancellation.

## External source audit

The current primary source for the finite dictionary gives:

- the exact map \(v\mapsto T_v\mapsto K_v\mapsto\widehat g_v\mapsto g_v\);
- the source functions for prime, pole, and archimedean blocks;
- the exact pole-neutral row;
- the cutoff-free archimedean block.

The source explicitly does not claim an RH proof.

## Derived result

Using the digamma partial-fraction expansion anchored at \(r=0\), the archimedean density admits the exact decomposition
\[
h_+(r)=h_+(0)+\sum_{n\ge0}
\left(\frac1{a_n}-\frac{a_n}{a_n^2+r^2/4}\right),
\qquad a_n=n+\tfrac14.
\]

Fourier transformation of each Lorentzian term gives an exact exponential resolvent kernel. In the Volterra coordinate this yields
\[
Q_{\mathrm{arch},\infty}
=
\frac{h_+(0)}2K_v(1)
+
2\pi\sum_{n\ge0}\int_0^1
K_v(\omega)
\left[\frac1{a_n}-e^{-2La_n(1-\omega)}\right]d\omega.
\]

## Important sign finding

The scalar density is increasing and its nonconstant partial-fraction summands are nonnegative, but this does not imply quadratic-form positivity because \(K_v\) can change sign.

Moreover,
\[
h_+(0)<0
\]
and for nonzero real-even v,
\[
K_v(1)=2\|T_v\|_{L^2(0,1)}^2>0.
\]

Thus the archimedean block contains an explicit negative anchor. Any future positivity proof must account for it quantitatively; it cannot be removed by pole-neutrality or by a sign convention.

## Status

- Exact archimedean resolvent representation: DERIVED.
- Positive-kernel representation of the full restricted form: OPEN.
- Uniform restricted finite positivity: OPEN / LOAD-BEARING.
- RH: OPEN.

## Next attack

Search for a positive Gram/Schur representation after combining:

1. prime samples at \(\omega_q\);
2. the exponential resolvent kernels \(e^{-2La_n(1-\omega)}\);
3. the exact pole-neutral and \(M_0=0\) constraints.

If no such representation emerges, run an adversarial certified-negative search on the restricted subspace.

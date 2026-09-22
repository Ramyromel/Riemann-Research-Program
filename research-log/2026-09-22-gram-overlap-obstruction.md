# Research Log — Gram/Overlap Obstruction

**Date:** 2026-09-22

## Result

The first canonical source-intersection Gram candidate
\[
G_{qr}=
\frac{\Lambda(q)}{\sqrt q}
\frac{\Lambda(r)}{\sqrt r}
\min(\omega_q,\omega_r)
\]
was audited.

It has an exact indicator-function Gram representation and is therefore PSD.

However, the Prime–Weil arithmetic term is
\[
-\sum_q\frac{\Lambda(q)}{\sqrt q}K_v(\omega_q),
\qquad
K_v(\omega)=2\int_0^\omega T_v(t)T_v(\omega-t)\,dt.
\]

The candidate Gram form is a pairwise source construction with two independent source indices. The Weil term is a one-source sum whose source value is itself a quadratic functional of the test function.

The first candidate therefore does not reproduce the Prime–Weil block.

## New interpretation

The relevant "intersection" geometry is at the level sets
\[
t+s=\omega_q,
\]
not simply between pairs of prime sources.

This redirects the route toward convolution/Toeplitz/Hankel structure in the Galerkin/test-function coordinate.

No zeta zeros were used. No RH claim is made.

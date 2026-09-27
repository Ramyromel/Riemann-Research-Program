# 2026-09-27 — Archimedean Resolvent Tail Certificate

A key numerical limitation in T-006K was the truncation of the outer resolvent series.

For
[
I(a)=Lint_0^1K_v(omega)e^{-2La(1-omega)}domega
]
integration by parts gives, using (K_v(0)=0),
[
rac{K_v(1)}{2a}-I(a)
=
rac1{2a}int_0^1K_v'(1-x)e^{-2Lax}dx.
]

Hence each omitted term is bounded by (M_1(v)/(4La^2)), where
(M_1(v)=sup|K_v'|), and the tail after (N_T) terms satisfies
[
|R_{N_T}(v)|
le
rac{M_1(v)}{4L}
sum_{n=N_T}^{infty}(n+	frac14)^{-2}
le
rac{M_1(v)}{4L(N_T-	frac34)}.
]

This is an actual analytic error certificate, not an empirical convergence estimate.

Next implementation task: compute a rigorous finite-basis bound for (sup\|K'(\omega)\|), propagate it to a matrix/operator norm, and use interval eigenvalue bounds for the restricted combined form.

No positivity or RH conclusion follows from this bound alone.

# N=3 restricted tail-structure audit

**Status: DISCOVERY / RIGOROUS ENVELOPE — NOT A POSITIVITY CERTIFICATE**

This experiment addresses the load-bearing N=3 problem after the successful
diagnostic run.  The pole-neutral space has dimension two.  Rather than bound
the Archimedean tail in the ambient four-dimensional basis and then restrict,
the experiment first combines the exact finite Fourier coefficients for each
restricted basis pair and only then takes the absolute-value envelope.

For a restricted pair (v,w), the finite Fourier representation of
(K_{v,w}'') is bounded coefficient-by-coefficient.  This gives a rigorous
entrywise envelope (M_{2,ab}), hence

[
\|R_T\|_F \le
\frac{\left(\sum_{a,b}M_{2,ab}^2\right)^{1/2}}
{8L^2}
\sum_{n=T}^{\infty}(n+1/4)^{-3}.
]

The cubic tail follows from the exact pole-neutral endpoint identities

[
T_v(0)=T_v(1)=0,qquad K_v'(0)=K_v'(1)=0.
]

The experiment is deliberately conservative.  If its matrix envelope does not
exclude zero, the result is **INCONCLUSIVE**, not a counterexample.

## Why this matters

The N=3 diagnostic showed the smallest restricted eigenvalue moving toward
zero as the resolvent cutoff increases.  This can be caused by:

1. a genuinely null direction of the cutoff-free Weil form;
2. a small positive eigenvalue obscured by truncation;
3. insufficient tail control.

The present audit separates (3) from the first two possibilities.

## Verification boundary

- exact pole-neutral basis: **DERIVED**
- combined finite Fourier coefficient envelope: **DERIVED**
- (O(T^{-2})) Archimedean tail envelope: **DERIVED**
- N=3 positive definiteness: **OPEN**
- finite-to-infinite positivity: **OPEN**
- global Weil positivity: **OPEN**
- RH: **OPEN**

No zeta-zero ordinates are used anywhere in this experiment.

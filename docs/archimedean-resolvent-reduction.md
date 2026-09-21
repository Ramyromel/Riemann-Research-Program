# Archimedean Resolvent Reduction on the Pole-Neutral Family

**Status:** DERIVED EXACT REPRESENTATION  
**Scope:** real-even finite dictionary; cutoff-free archimedean block  
**Purpose:** expose the archimedean term as an explicit resolvent/Lorentzian series before attempting any positivity claim.

## 1. Exact starting point

Let
\[
h_+(r)=\operatorname{Re}\psi\!\left(\tfrac14+\tfrac{ir}{2}\right)-\log\pi
\]
and
\[
Q_{\mathrm{arch},\infty}(v;c)
=\frac1{2\pi}\int_{\mathbb R}h_+(r)g_v(r)\,dr.
\]

The finite dictionary gives an even compactly supported Fourier transform
\[
\widehat g_v(\xi)=\pi K_v(1-|\xi|/\Delta),
\qquad
\Delta=\frac{L}{2\pi},
\]
with
\[
K_v(\omega)=2\int_0^\omega T_v(t)T_v(\omega-t)\,dt.
\]

These identities are exact finite identities; no RH assumption is used.

## 2. Partial-fraction expansion anchored at r=0

Writing
\[
a_n=n+\tfrac14,
\]
the digamma partial fraction formula yields the exact difference expansion
\[
h_+(r)
=
h_+(0)
+
\sum_{n=0}^{\infty}
\left(
\frac1{a_n}
-
\frac{a_n}{a_n^2+r^2/4}
\right).
\]

Equivalently,
\[
h_+(r)
=
h_+(0)
+
\sum_{n=0}^{\infty}
\frac{r^2/4}
{a_n\left(a_n^2+r^2/4\right)}.
\]

Every summand in the second expression is nonnegative for real r. This establishes monotonicity of h_+ directly at the scalar-density level, but **does not imply positivity of the quadratic form**, because g_v(r) need not be nonnegative.

## 3. Fourier-side resolvent identity

For each a>0, under the Fourier convention
\[
g(r)=\int_{\mathbb R}\widehat g(\xi)e^{2\pi i r\xi}\,d\xi,
\]
one has
\[
\int_{\mathbb R}
\frac{a}{a^2+r^2/4}g(r)\,dr
=
2\pi
\int_{\mathbb R}
e^{-4\pi a|\xi|}
\widehat g(\xi)\,d\xi.
\]

Therefore the anchored summand contributes exactly
\[
\frac1{2\pi}
\int_{\mathbb R}
\left(
\frac1a-\frac{a}{a^2+r^2/4}
\right)g_v(r)\,dr
=
\frac{\widehat g_v(0)}{2\pi a}
-
\int_{\mathbb R}
e^{-4\pi a|\xi|}
\widehat g_v(\xi)\,d\xi.
\]

Hence
\[
\boxed{
Q_{\mathrm{arch},\infty}(v;c)
=
\frac{h_+(0)}{2\pi}\widehat g_v(0)
+
\sum_{n=0}^{\infty}
\left[
\frac{\widehat g_v(0)}{a_n}
-
\int_{\mathbb R}
e^{-4\pi a_n|\xi|}
\widehat g_v(\xi)\,d\xi
\right].
}
\]

The individual bracketed terms are not asserted to be nonnegative. Their sign depends on the Fourier weight.

## 4. Equivalent kernel in the Volterra coordinate

Substituting
\[
\widehat g_v(\xi)
=
\pi K_v(1-|\xi|/\Delta)
\quad (|\xi|\le\Delta)
\]
and using evenness gives
\[
\boxed{
Q_{\mathrm{arch},\infty}(v;c)
=
\frac{h_+(0)}{2}\,K_v(1)
+
\sum_{n=0}^{\infty}
\left[
\frac{K_v(1)}{2a_n}
-
L\int_0^1 K_v(\omega)e^{-2La_n(1-\omega)}d\omega
\right].
}
\]

Here \(4\pi a_n\Delta=2La_n\).

This is an exact scalar representation of the archimedean block in the same \(K_v\)-coordinate used by the prime dictionary.

## 5. Structural consequence for the current proof target

The pole-neutral restriction has two logically distinct roles:

1. The row
\[
\frac{v_0}{\beta^2}
+
\sqrt2\sum_{k=1}^N\frac{v_k}{k^2+\beta^2}=0
\]
annihilates the pole square and gives \(g_v(i/2)=0\).

2. The moment row
\[
M_0(v)=v_0+\sqrt2\sum_{k=1}^N v_k=0
\]
annihilates the rank-one prime-power singular-curvature direction.

The second condition does **not** by itself remove the archimedean contribution. In particular, the displayed representation shows an explicit negative anchor
\[
\frac{h_+(0)}2K_v(1),
\qquad h_+(0)<0,
\]
which must be compensated by the remaining resolvent terms and the prime sampling term.

For real-even \(T_v\),
\[
K_v(1)=2\int_0^1|T_v(t)|^2dt>0
\]
for nonzero v. Thus this negative anchor is genuine and cannot be discarded as a sign-convention artifact.

## 6. New load-bearing subproblem

The restricted positivity problem can now be sharpened to an explicit kernel comparison:

\[
-\sum_{q\le c}
\frac{\Lambda(q)}{\sqrt q}K_v(\omega_q)
+
\frac{h_+(0)}2K_v(1)
+
\sum_{n=0}^{\infty}
\left[
\frac{K_v(1)}{2a_n}
-
L\int_0^1K_v(\omega)e^{-2La_n(1-\omega)}d\omega
\right]
\ge0
\]
for every nonzero admissible v in the exact pole-neutral family.

This is still **OPEN**.

A successful proof must either:

- convert the entire right-hand side into a positive Gram/Schur form;
- prove a sharp lower bound for the resolvent series against the prime sampling functional; or
- produce a certified negative direction, which would falsify finite positivity for that parameter pair and terminate this route there.

No step above proves RH or assumes RH.

## 7. Verification boundary

The derivation uses only:

- the external finite Guinand--Weil dictionary;
- the standard digamma partial-fraction expansion;
- the Fourier transform of a Lorentzian kernel;
- the already audited normalization \(\Delta=L/(2\pi)\).

The representation is therefore a **derived identity**, not a numerical fit and not a positivity theorem.

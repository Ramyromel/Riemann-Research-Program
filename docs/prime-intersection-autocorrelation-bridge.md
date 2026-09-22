# Prime-Intersection → Prime–Weil Autocorrelation Bridge

**Status:** DERIVED STRUCTURAL BRIDGE — NO RH CLAIM

## 1. Purpose

The earlier \(2x-1\) investigation showed that the affine transform
\[
y=2x-1
\]
does not create new pairwise geometry: \(|y_q-y_r|=2|q-r|\).

The useful next question is whether the user's "intersection points and distance" intuition is already present in the exact Prime–Weil kernel.

It is, at the level of a one-source overlap/correlation functional. A pairwise source Gram interpretation remains open.

## 2. Exact object already present in the finite Weil dictionary

For cutoff \(c>1\), put
\[
L=\log c,\qquad
\omega_q=1-\frac{\log q}{L}.
\]

For a real-even Galerkin vector \(v\), the finite dictionary uses
\[
K_v(\omega)
=
2\int_0^\omega T_v(t)T_v(\omega-t)\,dt,
\qquad 0\le\omega\le1.
\]

The prime contribution is
\[
Q_{\mathrm{prime}}(v;c)
=
-\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}K_v(\omega_q).
\]

This is exact under the repository's audited normalization.

## 3. Exact intersection/correlation interpretation

Define
\[
(R_\omega T_v)(t)=T_v(\omega-t)
\]
on \([0,\omega]\). Then
\[
K_v(\omega)
=
2\langle T_v,R_\omega T_v\rangle_{L^2(0,\omega)}.
\]

Thus \(K_v(\omega)\) is exactly an overlap/correlation between a function and its reflected copy over the common interval where both factors are evaluated.

This is materially different from the generic kernels tested in the first prime-intersection experiment:

- it uses the exact Weil coordinate \(\omega_q\);
- it uses the exact prime-power weight \(\Lambda(q)/\sqrt q\);
- it depends on the same Galerkin vector \(v\) that defines the Weil test function;
- it enters the exact finite explicit-formula quadratic form.

The "intersection" is therefore an analytic overlap already encoded by the finite Weil dictionary, rather than an arbitrary auxiliary kernel.

## 4. Distance variable

The source location is not the raw distance between primes. It is the logarithmic distance from the cutoff:
\[
d_c(q)=1-\omega_q=\frac{\log q}{\log c}.
\]

Hence two prime-power sources have the exact cutoff-normalized separation
\[
|d_c(q)-d_c(r)|
=
\frac{|\log q-\log r|}{\log c}.
\]

The affine map \(2q-1\) does not enter this identity. It remains an auxiliary coordinate experiment, not the source of the Weil geometry.

## 5. Pairwise source geometry: exact boundary

A natural pairwise correlation for translated copies is
\[
C_v(a,b)
=
\int_{\mathbb R}T_v(t-a)T_v(t-b)\,dt,
\]
whenever the chosen extension/domain makes the integral well-defined.

For compactly supported \(T_v\), this is an overlap integral whose value depends on the relative displacement \(|a-b|\).

However, **no equality is asserted between \(C_v(a,b)\) and \(K_v(\omega)\)**. The two objects have different constructions: \(K_v\) is a self-correlation with a cutoff-dependent reflection on \([0,\omega]\), whereas \(C_v\) is a translated whole-domain correlation. An exact identification would require an explicit support/extension theorem.

This distinction is now recorded as a hard proof boundary.

## 6. What is established

The following statements are exact:

1. \(2x-1\) is affine, so raw transformed distance contains no new prime geometry.
2. The finite Prime–Weil construction contains the overlap/correlation functional \(K_v\).
3. Prime-power arithmetic enters through the exact weights \(\Lambda(q)/\sqrt q\).
4. Multiplicative arithmetic enters the source coordinate through \(\log q\).
5. The cutoff maps the source locations into \(0\le\omega_q<1\).
6. Therefore the promising version of the user's intersection idea is the **weighted, logarithmic, cutoff-normalized overlap geometry**, not the \(2x-1\) transform itself.

None of these statements implies Weil positivity or RH.

## 7. New load-bearing question

The next mathematical target is now precise:

> Can the restricted Prime–Weil quadratic form be rewritten as a positive Gram/overlap object whose source vectors are generated directly from the prime-power locations \(\omega_q\) and weights \(\Lambda(q)/\sqrt q\), with the archimedean term providing the required completion?

A successful derivation requires an exact identity of quadratic forms, not numerical fitting.

A failed derivation should be retained as a no-go result.

## 8. Relation to the existing positivity frontier

On the pole-neutral family,
\[
Q_{\mathrm{PN}}(v;c)
=
-\sum_{q\le c}\frac{\Lambda(q)}{\sqrt q}K_v(\omega_q)
+
Q_{\mathrm{arch},\infty}(v;c).
\]

Therefore the new route does not replace the existing positivity problem. It gives a precise geometric interpretation of the arithmetic term and identifies what a Gram/Schur closure would have to capture.

## 9. Non-circularity

No zeta zero ordinates are used in this construction.

No parameter is selected by spectral matching.

Known zeros may only appear later in a separately frozen reconstruction-control experiment.

## 10. Classification

- \(2x-1\) raw-distance novelty: **REFUTED AS A NEW GEOMETRY / TRIVIAL AFFINE TRANSFORM**.
- Prime-power weighted logarithmic source geometry: **DERIVED**.
- \(K_v\) as an exact finite-Weil overlap/correlation functional: **DERIVED**.
- Pairwise source-to-source Gram equality with \(K_v\): **OPEN**.
- Positive Gram/Schur representation of \(Q_{\mathrm{PN}}\): **OPEN / LOAD-BEARING**.
- Global Weil positivity: **OPEN**.
- RH: **OPEN**.

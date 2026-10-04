# Odd sine-basis arithmetic derivation

**Status: DERIVED / CI-VERIFIED ARITHMETIC BLOCK; NORMALIZATION BRIDGE OPEN**

## 1. Basis and parity

For the localized coordinate (w\in[0,1]), define
\[
\psi_k(w)=\sqrt2\sin(2\pi k w),\qquad k\ge1.
\]

With
\[
y=L(w-1/2),\qquad a=L/2,
\]
physical reflection (y\mapsto-y) is (w\mapsto1-w). Therefore
\[
\psi_k(1-w)=-\psi_k(w),
\]
so the basis is genuinely odd in the physical coordinate.

This is not a change of basis inside the old cosine sector: it is a new parity sector derived directly from the localized coordinate.

## 2. Exact arithmetic translation block

For a prime power (q=p^r), let
\[
w_q=1-\frac{\log q}{\log c}.
\]

Using the localized translation primitive
\[
B_{ij}(w)=\int_0^w\psi_i(t)\psi_j(t)\,dt,
\]
the finite arithmetic block is
\[
P_{ij}(c,N)
=
\sum_{q\le c}
-\frac{2\log p}{\sqrt q}\,
B_{ij}(w_q),
\]
with (q=p^r).

The implementation derives (B_{ij}) from the exponential representation
\[
\sqrt2\sin(2\pi k w)
=
\frac{e^{2\pi i k w}-e^{-2\pi i k w}}{\sqrt2,i},
\]
so no cosine-sector matrix is transformed or assumed equivalent.

## 3. Automatic zero-mean moment

Every sine basis function satisfies
\[
\int_0^1\psi_k(w)\,dw=0.
\]

Hence every finite odd sine combination has zero mean:
\[
M_0(v)=0
\]
identically.

This is a genuine structural difference from the even cosine sector, where (M_0) is an active pole-neutral constraint.

It does **not** establish the second pole-neutral condition associated with the full Weil normalization. That condition remains to be derived from the physical odd transform.

## 4. CI verification

The diagnostic was executed in GitHub Actions with Python 3.12 and mpmath 1.4.1.

For (c=20,N=6):
- (M_0) numerical residual: (1.14\times10^{-66});
- prime matrix asymmetry: exactly (0) at reported precision;
- minimum eigenvalue of the prime block: (-2.52981845180254112).

The negative eigenvalue is **not a counterexample to RH**. It is the arithmetic block alone; the archimedean/normalization terms have not yet been attached.

## 5. Remaining load-bearing derivation

The next step is to derive, from the physical odd Weil form rather than analogy:

1. the odd archimedean/resolvent block;
2. the exact pole functional(s) in the odd sector;
3. the polar (sinh(y/2)) rank-one term in the sine basis;
4. the normalization factors connecting physical (y) to the finite (w)-representation;
5. the exact equality between the resulting odd finite form and the compressed physical operator.

Only after those identities are proved can the zero-extension compression theorem be applied to the finite matrices.

**No RH claim is made.**

# Exact zero-extension compression audit

**Status: DERIVED CONDITIONALLY / NORMALIZATION AUDIT REQUIRED**

This note isolates the structural identity that can replace the finite-dimensional Galerkin limit:

$$E_{a,b}^{*}A_bE_{a,b}=A_a,\qquad 0<a<b.$$

Here E_{a,b} is extension by zero from (-a,a) to (-b,b).

## 1. Exterior harmonic calculation

Define

$$\mathfrak H_a[f]=\frac14\int_{-a}^a\int_{-a}^a\frac{|f(x)-f(y)|^2}{|x-y|}\,dx\,dy.$$

For f supported in (-a,a), extend it by zero to (-b,b). Only the two exterior strips contribute:

$$\mathfrak H_b[Ef]-\mathfrak H_a[f]=\frac12\int_{-a}^a |f(x)|^2\log\frac{b^2-x^2}{a^2-x^2}\,dx.$$

This is exact; no limiting argument is used.

## 2. Endpoint-potential cancellation

With the physical endpoint potential

$$V_a(x)=-\frac12\log(a^2-x^2),$$

we have

$$V_b(x)-V_a(x)=-\frac12\log\frac{b^2-x^2}{a^2-x^2}.$$

Therefore the endpoint-potential change is exactly the negative of the exterior harmonic change.

## 3. Regular and polar terms

Any regular localized kernel that only samples old-old pairs is unchanged by zero extension. The physical polar profile must be radius-independent:

$$s^{\rm ph}(y)=\sinh(y/2).$$

Thus its restriction is compatible with zero extension, and the polar rank-one term is preserved. The compression argument must therefore be performed before rescaling to x=y/a.

## 4. Prime-power translations

A localized translation of logarithmic length ell=log q has old-old overlap of the form

$$\int f(y)\,\overline{f(y-\ell)}\,dy.$$

If q<e^{2a}, the branch is already active at radius a and is unchanged after extension. If e^{2a} <= q < e^{2b}, then ell >= 2a, so two points in (-a,a) cannot differ by ell except at a measure-zero boundary. The newly activated branch therefore has zero old-old overlap.

This proves the arithmetic compression step provided the repository's localized arithmetic form uses exactly this translation-support convention.

## 5. Conditional full compression theorem

Suppose the repository physical operator decomposes into harmonic, endpoint, regular gamma, polar, and prime-power translation blocks with the exact normalization above. Then the preceding identities give

$$\boxed{E_{a,b}^*A_bE_{a,b}=A_a.}$$

No Galerkin limit is involved.

## 6. Cofinal-support reduction

If a_j tends to infinity and A_{a_j} is positive semidefinite for every j, then for any finite a choose j with a<a_j:

$$\langle f,A_af\rangle=\langle E_{a,a_j}f,A_{a_j}E_{a,a_j}f\rangle\ge0.$$

Hence positivity on a cofinal sequence implies positivity at every finite support radius.

## 7. Remaining obligations

The physical calculation is not yet an RH proof. We must still:

- reconcile the physical blocks with the repository's exact Weil normalization;
- prove that the finite Prime-Weil/Hankel representation is exactly the compression of the physical operator;
- prove the prime activation convention without a hidden boundary term;
- prove positivity at a cofinal sequence of support radii;
- pass from the odd compactly supported core to the full Weil criterion.

## Verification status

| Component | Status |
|---|---|
| Exterior harmonic identity | DERIVED |
| Endpoint cancellation | DERIVED |
| Physical polar restriction | DERIVED |
| Translation support argument | DERIVED CONDITIONALLY |
| Full compression in repository normalization | OPEN |
| Cofinal reduction | DERIVED CONDITIONALLY |
| Cofinal positivity | OPEN |
| Global Weil positivity | OPEN |
| Riemann Hypothesis | OPEN |

The decisive next task is the normalization bridge between the repository's finite Prime-Weil/Hankel formulation and this physical localized operator. No theorem is promoted until that bridge is independently verified.
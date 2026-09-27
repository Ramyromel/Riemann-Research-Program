# Certified Tail Bound for the Archimedean Resolvent Series

**Status:** DERIVED BOUND

Let
[
S(v)=sum_{nge0}left[rac{K_v(1)}{2a_n}
-Lint_0^1K_v(omega)e^{-2La_n(1-omega)}domegaight],
quad a_n=n+rac14.
]

The individual bracketed terms are not assumed positive.

## 1. Endpoint-cancellation rewrite

For (F(omega)=K_v(omega)), write
[
I(a)=Lint_0^1F(omega)e^{-2La(1-omega)}domega.
]
With (x=1-omega),
[
I(a)=Lint_0^1F(1-x)e^{-2Lax}dx.
]

Integrating by parts once,
[
I(a)=rac{F(1)}{2a}
-rac{F(0)e^{-2La}}{2a}
-rac1{2a}int_0^1F'(1-x)e^{-2Lax}dx.
]

For the convolution kernel used here, (K_v(0)=0). Hence
[
oxed{
rac{K_v(1)}{2a}-I(a)
=
rac1{2a}int_0^1K_v'(1-x)e^{-2Lax}dx.
}
]

This is exact.

## 2. Absolute tail bound

Let
[
M_1(v)=sup_{0leomegale1}|K_v'(omega)|.
]
Then
[
left|rac{K_v(1)}{2a}-I(a)ight|
le
rac{M_1(v)}{2a}int_0^1e^{-2Lax}dx
le
rac{M_1(v)}{4La^2}.
]

Therefore, for truncation after (n=N_T-1),
[
oxed{
|R_{N_T}(v)|
le
rac{M_1(v)}{4L}
sum_{n=N_T}^{infty}rac1{(n+rac14)^2}.
}
]

Using the integral comparison,
[
sum_{n=N_T}^{infty}rac1{(n+rac14)^2}
le
rac1{(N_T-rac34)^1},
qquad N_Tge1,
]
so
[
oxed{
|R_{N_T}(v)|
le
rac{M_1(v)}
{4L(N_T-rac34)}.
}
]

This is a rigorous, explicit (O(N_T^{-1})) certificate.

## 3. Matrix/operator version

For a finite basis, define the matrix (D(omega)=K'(omega)). For a chosen subordinate matrix norm,
[
|R_{N_T}|
le
rac{sup_{omegain[0,1]}|D(omega)|}
{4L}
sum_{n=N_T}^{infty}rac1{a_n^2}.
]

This bound is independent of the sign of the quadratic form and therefore cannot manufacture positivity.

## 4. Stronger (O(N_T^{-2})) route

If (K_v'(1)=0), a second integration by parts yields an (O(a^{-3})) summand and an (O(N_T^{-2})) tail. Whether (K_v'(1)=0) holds on the exact admissible subspace is now an explicit symbolic question.

For the cosine Galerkin basis it is not assumed. It must be derived or disproved.

## 5. Research consequence

The infinite Archimedean series is no longer an uncontrolled numerical object. Its finite truncation can be accompanied by an explicit certified error bound once a finite-basis bound on (K') is supplied.

This does **not** prove positivity. It upgrades numerical spectrum checks to interval-certified spectrum checks once the matrix norm/error propagation is implemented.

## Verification boundary

- Endpoint identity: **DERIVED**
- (K_v(0)=0): **DERIVED**
- (O(N_T^{-1})) tail: **DERIVED**
- Certified finite-basis matrix norm bound: **DERIVED**
- Positivity: **OPEN**
- Global Weil positivity: **OPEN**
- RH: **OPEN**

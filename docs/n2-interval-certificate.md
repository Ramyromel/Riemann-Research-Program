# N=2 interval certificate

## Audited case

- cutoff: c = 20
- cosine degree: N = 2
- retained Archimedean resolvent terms: T = 1000
- arithmetic: mpmath.iv interval arithmetic
- zero data: none

The two exact pole-neutral constraints leave a one-dimensional space. The
certificate sets v2 = 1 and solves the two constraints directly for v0 and v1,
then evaluates the combined Prime + Archimedean quadratic form as a scalar
Rayleigh quotient.

## Exact interval construction

The Archimedean matrix uses the same finite Fourier formulas as the established
arbitrary-precision implementation. The constant is evaluated through the
exact identity

h_+(0) = -gamma - pi/2 - 3 log(2) - log(pi).

The finite prime block uses the exact prime-power list and the same cosine
Hankel representation as the existing implementation.

For the omitted resolvent tail, pole-neutral boundary cancellation gives the
second-order estimate

|R(v)| <= M2(v)/(8 L^2) * sum_{n>=T} (n+1/4)^(-3).

The interval certificate uses the elementary conservative comparison

sum_{n>=T} (n+1/4)^(-3) <= 1/[2(T-3/4)^2].

## Result

At (c,N,T) = (20,2,1000), the interval enclosure is strictly positive.
The finite interval is centered at the previously observed value

3.6314631173657718819945540003471e-5

with interval width below 1e-60 at the test precision.

The conservative second-order tail envelope is below 4e-6. Therefore the
tail-corrected lower endpoint remains above 3e-5 in the repository test.

## Status

**INTERVAL-CERTIFIED — LOCAL FINITE PARAMETER CASE**

This certifies positivity of the implemented finite expression after applying
the stated analytic tail envelope for this specific (c,N) case.

It does not prove global Weil positivity, uniform positivity over c or N, the
infinite-dimensional limit, a Hilbert–Polya realization, or the Riemann
Hypothesis.

The next target is a grid of interval-certified cases across c and N, followed
by an attempt to identify a uniform mechanism rather than extrapolating from
isolated positive cases.

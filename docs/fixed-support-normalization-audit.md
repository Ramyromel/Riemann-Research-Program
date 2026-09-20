# Fixed-Support Normalization Audit

**Status:** OPEN — exact normalization bridge under construction

## Purpose

The previous research step correctly reduced the globalization problem to a fixed-support factor problem, but it used schematic notation. This document prevents that notation from being mistaken for an established identification.

## 1. Two formulations that must be connected

A standard Weil formulation can be written on the multiplicative group \(\mathbb R_+^*\), with a smooth compactly supported factor \(f\) and autocorrelation

\[
g=f*f^*,\qquad f^*(x)=\overline{f(x^{-1})}.
\]

In logarithmic coordinates \(x=e^u\), multiplicative convolution becomes additive convolution after the appropriate Haar-measure normalization.

A Fourier/Mellin transform then converts the multiplicative test object into the zero-side quantity.

Separately, the finite Groskin construction starts with a finite real-even Galerkin coefficient vector, constructs a finite factor/kernel through a Volterra-type convolution, and obtains a band-limited Guinand–Weil function.

These are structurally similar, but **similarity is not identity**.

## 2. Exact bridge required

The project must explicitly construct maps

\[
f
\xrightarrow{\;\mathcal L\;}
T
\xrightarrow{\;P_N\;}
T_N
\xrightarrow{\;V\;}
K_N
\xrightarrow{\;\mathcal F^{-1}/\mathcal M^{-1}\;}
g_N,
\]

and prove that the resulting \(g_N\) is the same normalized test object used by the finite theorem.

The proof must specify:

- multiplicative Haar measure versus logarithmic Lebesgue measure;
- Fourier transform sign and \(2\pi\) convention;
- Mellin transform convention;
- location of the \(1/2\) shift;
- involution \(f^*\);
- even-sector normalization;
- the exact support rescaling;
- prime cutoff convention;
- pole-neutral constraints;
- sign convention for the Weil quadratic form.

## 3. Pole constraints

The standard positivity formulation imposes vanishing at the two pole directions. In logarithmic coordinates these become two explicit linear functionals of the factor.

For a finite approximation, the project must not merely show approximate vanishing. It must either:

1. construct \(T_N\) inside the exact finite nullspace; or
2. apply a finite-rank projection \(P_N^{\mathrm{constr}}\) and prove

\[
\|P_N^{\mathrm{constr}}T-T_N\|\to0.
\]

The second route requires lower bounds on the relevant finite constraint matrix. If those bounds fail, the correction may not vanish.

## 4. Fixed support and prime terms

For a compactly supported multiplicative test function, the explicit-formula prime-power contribution is finite because only prime powers whose logarithms lie in the transformed support can contribute. This is an external structural fact, not a numerical observation.

Therefore, for a **fixed target support**, the arithmetic part does not require a separate infinite-prime limit.

The remaining analytic limit is the approximation of the target factor and the archimedean contribution.

## 5. Form-continuity target

Let \(Q\) denote the exact Weil quadratic form in one fixed normalization.

The required theorem is:

\[
T_N\to T\text{ in }\tau
\quad\Longrightarrow\quad
Q(g_{T_N})\to Q(g_T).
\]

A sufficient route is:

- finite prime terms converge directly;
- Fourier/Mellin transforms converge in a norm giving an integrable majorant;
- the archimedean term converges by dominated convergence;
- all pole/moment constraints hold exactly.

No uniform spectral gap is required for the final sign-closure step if the same target test object is approached pointwise by positive quadratic forms.

## 6. Current finding

The finite factor approximation argument is **not yet a proof of the Weil criterion** because the exact map from the standard Weil factor to Groskin's normalized finite factor has not been instantiated line by line.

This is now the next mathematical target.

## Classification

- Fixed-support finite-prime reduction: **DERIVED FROM EXTERNAL WEIL FORMULATION**
- Finite cosine approximation: **STANDARD ANALYTIC FACT, SUBJECT TO THE CORRECT FUNCTION SPACE**
- Volterra continuity: **DERIVED**
- Constraint-preserving projection: **OPEN**
- Exact Groskin/Weil normalization bridge: **OPEN**
- Weil-form continuity under the exact bridge: **OPEN**
- Global RH implication: **OPEN**

No RH claim is made.

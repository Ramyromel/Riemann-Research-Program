# Finite-Factor Approximation: Fixed-Support Core

**Status:** DERIVED ANALYTIC SUBTARGET — NORMALIZATION BRIDGE STILL OPEN

## 1. Fixed support changes the globalization problem

The external Weil formulation can be restricted to smooth compactly supported auxiliary factors. For a fixed compact support window, the explicit formula contains only finitely many prime-power contributions. Thus a global RH proof does not require taking the prime cutoff to infinity for one fixed test function; the support window itself determines the finite arithmetic cutoff.

This is an important simplification of T-006A.

## 2. Finite coefficient space

Groskin's finite construction uses, for fixed c and N,

$$T_v(t)=\\sum_{m=-N}^{N}u_m e^{2\\pi i m t},\\qquad u_{-m}=u_m\\in\\mathbb R.$$

Hence the real-even coefficient space is exactly the cosine-polynomial space of degree at most N on the normalized interval.

The induced kernel is

$$K_v(\\omega)=2\\int_0^\\omega T_v(t)T_v(\\omega-t)\\,dt.$$

The associated test function is obtained by a fixed linear Fourier transform of the compactly supported weight built from K_v.

## 3. Analytic approximation fact

Let T be a sufficiently smooth real-even target factor on the normalized interval, with boundary behavior compatible with the compact-support extension.

Its cosine series gives finite cosine polynomials T_N with

$$T_N\\to T$$

in C^m for every fixed m when the target is chosen from the corresponding smooth compact-support core.

This statement is ordinary Fourier approximation; it does not by itself identify T with the factor required by the Weil criterion.

## 4. Convolution continuity

For T_N,T in L^2([0,1]), Volterra convolution satisfies a Young-type bound

$$\\|T_N*T_N-T*T\\|_{L^2}
\\le
\\|T_N-T\\|_{L^1}\\|T_N\\|_{L^2}
+
\\|T\\|_{L^2}\\|T_N-T\\|_{L^1}.$$

Using ||h||_1 <= ||h||_2 on a unit interval,

$$T_N\\to T\\text{ in }L^2
\\Longrightarrow K_{v_N}\\to K_T\\text{ in }L^2.$$

For a C^m core, the same argument can be differentiated and strengthened to the norms required for the Fourier transform and explicit-formula estimates.

This is a genuine reduction: the nonlinear Volterra map is continuous on the natural finite-support factor space.

## 5. Constraint preservation

The finite construction already contains exact finite-dimensional pole-neutral subspaces. Therefore the approximation problem is not approximate a constrained function and hope the constraints converge.

Instead:

1. approximate the target factor by a finite cosine polynomial;
2. impose the finite pole/moment constraints by an exact finite-rank correction;
3. prove that the correction tends to zero as N→∞.

The last step requires explicit conditioning estimates for the constraint functionals. No uniform conditioning theorem is currently claimed.

## 6. Weil-form continuity target

For a fixed support window, the prime-power part is finite. The remaining archimedean term is an integral against the standard archimedean density.

A sufficient theorem would therefore be:

$$K_N\\to K\\quad\\text{in a norm implying}\\quad g_N\\to g\\text{ with an integrable uniform majorant}$$

and then

$$Q(g_N)\\to Q(g)$$

by finite-term convergence plus dominated convergence for the archimedean contribution.

This is substantially more concrete than an abstract density statement.

## 7. Remaining exact bridge

The unresolved point is now sharply isolated:

> Prove that the compact-support factors used in the Weil criterion can be represented, after the exact normalization/rescaling, by the same T-space that generates Groskin's g_v, and that the finite constraint correction preserves admissibility.

Until this is established, the preceding approximation facts remain a candidate route rather than a proof of RH.

## 8. Research classification

- **DERIVED:** fixed support implies finite prime contribution.
- **DERIVED:** real-even Galerkin vectors are finite cosine polynomials.
- **DERIVED:** Volterra convolution is continuous in the stated finite-support norms.
- **TARGET:** constraint-preserving approximation with vanishing correction.
- **OPEN:** exact identification with the full Weil admissible factor class.
- **OPEN:** complete normalization/sign bridge.
- **OPEN:** final implication to Weil positivity and RH.

No RH conclusion is drawn.

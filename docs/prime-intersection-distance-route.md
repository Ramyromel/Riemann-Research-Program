# Prime-Intersection / Distance Route

**Status:** EXPERIMENTAL RESEARCH ROUTE — NO RH CLAIM

## Motivation

A proposed arithmetic coordinate transform is

F(x)=2x-1.

Every odd integer is represented by this map, so the transform alone cannot distinguish primes from odd composites. In particular, F(p_j)-F(p_i)=2(p_j-p_i), so raw transformed distances contain no new information beyond prime gaps.

The research question is therefore whether the transform becomes nontrivial when combined with prime-power weights and an independently defined intersection/kernel construction.

## 1. Arithmetic source

Use the von Mangoldt weight Lambda(n), equal to log(p) for n=p^k and zero otherwise. For cutoff c>1 define A_c={q=p^k <= c}. Set x_q=log(q), y_q=2q-1, and w_q=Lambda(q)/sqrt(q).

The logarithmic coordinate is retained because multiplicative prime-power structure becomes additive there.

## 2. Trivial affine component

For any two inputs, |y_q-y_r|=2|q-r|. Therefore a construction depending only on Euclidean distances in the y-coordinate is equivalent, up to scale, to the original integer-coordinate construction. Such a construction is classified as TRIVIAL TRANSFORM.

## 3. Nontrivial candidate: weighted intersection kernel

Define a family of source curves C_q(t)=w_q K(t,x_q,y_q), where K is fixed independently of observed zeta zeros. For an explicitly specified intersection/distance functional D, define D_qr=D(C_q,C_r).

The first admissibility requirement is that D cannot be obtained from an unweighted prime-gap matrix by affine rescaling.

## 4. Preferred analytic reduction

Test whether the construction reduces to D_qr=w_q w_r Phi(x_q-x_r), or to a Gram form D_qr=<phi_q,phi_r>. Determine whether the resulting matrix is positive/negative semidefinite, conditionally definite, Hankel, Toeplitz after logarithmic reparameterization, Loewner/divided-difference, or a Schur complement of a positive block matrix.

## 5. Intersection observables

Candidate observables must be defined before numerical comparison: zero-crossing locations of C_q-C_r; signed intersection multiplicities; pairwise logarithmic separations |log q-log r|; weighted intersection sums w_q w_r Phi(|log q-log r|); and curvature/divided-difference quantities from the same fixed kernel. Raw transformed gaps 2|p-q| are excluded as non-novel.

## 6. Relation to the existing Prime–Weil route

The existing finite Weil normalization contains the exact prime contribution Q_prime(v;c)=-sum_{q=p^k<=c} Lambda(q)/sqrt(q) K_v(1-log(q)/log(c)). The new route will test whether an independently constructed intersection kernel can be reduced to, or structurally explain, a kernel with the same prime-power weighting and logarithmic geometry. Equality must be derived, not fitted.

## 7. Non-circularity

Known zero ordinates are prohibited from constructing or tuning the arithmetic kernel. They may be introduced only in a separate reconstruction-control experiment after the arithmetic object has been frozen. No parameter may be selected by optimizing agreement with known zeta zeros.

## 8. Acceptance gates

A: exact definition of curves, kernels, weights, domains, and intersection functional.

B: proof that the construction is not merely an affine rescaling of prime gaps.

C: arithmetic provenance from prime/prime-power data and declared analytic constants only.

D: at least one exact structural property or a rigorous obstruction.

E: symbolic cross-route comparison with the finite Weil/Prime–Weil route, or rejection.

F: only after A–E, a separate numerical spectral experiment.

## 9. Failure is a valid result

If every admissible intersection construction reduces to a trivial affine transform, close this route as non-novel. If a nontrivial kernel has no relation to Weil structure, retain it only as an independent arithmetic experiment. If an exact relation to the Prime–Weil kernel is derived, promote it to the theorem ledger with precise hypotheses.

**No RH proof is claimed by this document.**
# Research Status

Date: 2026-09-21

## Global status

- Riemann Hypothesis: **OPEN**
- Complete proof in repository: **NONE**
- Weil positivity route: **ACTIVE RESEARCH**
- Spectral/operator route: **ACTIVE RESEARCH — BRIDGE AUDIT ADDED**
- Finite Guinand–Weil dictionary: **EXTERNAL THEOREM UNDER PROJECT AUDIT**
- Fixed-support normalization: **SUBSTANTIALLY RESOLVED**
- Even-sector fixed-support factor approximation: **DERIVED**
- External finite positivity at (c,N)=(100,200): **REPRODUCIBILITY INPUT / NOT GLOBAL**
- Even-sector finite positivity for all parameters: **OPEN / LOAD-BEARING**
- Odd-sector dictionary/positivity: **OPEN**
- Full Weil positivity: **OPEN**
- Numerical computation: **SUPPORTING EVIDENCE ONLY**
- Independent verification: **REQUIRED**

## New external anchor

The Groskin reproducibility package contains a cutoff-free interval-LDL^T inertia certificate at c=100, N=200, dimension 401, reporting n_pos=401 and n_neg=0. The package documents the 9000-bit Arb run, self-test, and independent mpmath recomputation.

This is strong finite evidence and a useful calibration point, but it is not a theorem for all c,N and does not imply RH. The upstream paper explicitly makes no RH or global Weil-positivity claim.

## Structural direction now prioritized

A companion Groskin result identifies the prime-power derivative jumps of the finite matrix path exactly as negative rank-one von Mangoldt events. The first-derivative jump at each prime-power threshold is a negative-semidefinite rank-one event; equivalently, the singular part of the second derivative is a negative-semidefinite matrix-valued von Mangoldt measure. This gives Loewner concavity of the prime block, not positivity of the full matrix. The sign is now corrected and audited against the external structural result.

The next target is now the exact restricted regular-prime plus archimedean sign problem after pole-neutral cancellation. The pole block and the singular prime-power curvature both vanish on the exact constrained family.

## New spectral bridge target

A dedicated audit now separates operator convergence, arithmetic identification, spectral-measure identification, boundary control, and infinite-dimensional domain control. This is complementary to the finite positivity route and carries no RH inference by itself.

## Active execution order

1. Reproduce and independently audit the external finite positivity certificate.
2. Extract the exact finite matrix formula and its prime-power path derivative structure.
3. Test candidate positive-kernel / Gram / Loewner representations symbolically.
4. Derive the regular prime kernel after exact pole-neutral restriction.
5. Use the exact restricted prime–archimedean kernel formula to seek a common positive-kernel, Gram/Schur, or uniform lower-bound representation.
6. Extend the analysis to the odd sector.
7. Audit the sine-Loewner/operator bridge against the exact finite Weil construction.
8. Assemble the full Weil criterion only after the sign theorem and limiting argument are closed.

## Hard stop

No finite certificate, zero matching, spectral convergence, or numerical stability result may be promoted to a proof of RH without an analytic theorem covering all required parameters and the final limit.

## Current mathematical frontier

The exact pole-neutral reduction is now sharpened one step further. The pole row removes the pole square, while \(M_0=0\) removes the singular rank-one prime-power curvature. The remaining even-sector problem is a regular prime sampling functional plus the cutoff-free archimedean functional.

The archimedean term has now been rewritten exactly as a Volterra-kernel resolvent series. This exposes a negative scalar anchor
\[
\frac{h_+(0)}2K_v(1),
\]
with \(h_+(0)<0\) and \(K_v(1)=2\|T_v\|_2^2>0\) for nonzero real-even \(v\). Therefore positivity of \(h_+\) at large frequency cannot by itself establish quadratic-form positivity.

The next load-bearing target is a joint prime–archimedean kernel identity or inequality that compensates this anchor on the exact constrained space.

## New exact operator result — 2026-09-22

The next subproblem from Issue #22 has been executed. The finite prime block now has an exact real-even Galerkin matrix representation as a weighted discrete Hankel/sum-level operator:
\[
H^{\mathrm{prime}}_{N,c}
=
-2\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}B(\omega_q),
\qquad
B_{ij}(\omega)=\int_0^\omega\phi_i(t)\phi_j(\omega-t)\,dt.
\]
Equivalently its distributional kernel is supported on \(t+s=\omega_q\).

An independent 60-digit quadrature audit agrees with the matrix quadratic form to approximately \(6.8\times10^{-62}\) at \(c=30,N=3\). No zeta-zero data are used.

**Classification:** exact finite representation = DERIVED; independent identity audit = VERIFIED; positivity = OPEN; joint prime–archimedean closure = OPEN; RH = OPEN.


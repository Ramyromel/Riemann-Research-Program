# Research Status

Date: 2026-09-20

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

A companion Groskin result identifies the prime-power derivative jumps of the finite matrix path exactly as negative rank-one von Mangoldt events, while the second-derivative jump is positive semidefinite. This arithmetic structure is now treated as a potential route to a global positivity decomposition, not as positivity itself.

The next target is therefore a structural factorization or monotonicity theorem for the complete cutoff-free matrix path, with the archimedean and pole pieces included.

## New spectral bridge target

A dedicated audit now separates operator convergence, arithmetic identification, spectral-measure identification, boundary control, and infinite-dimensional domain control. This is complementary to the finite positivity route and carries no RH inference by itself.

## Active execution order

1. Reproduce and independently audit the external finite positivity certificate.
2. Extract the exact finite matrix formula and its prime-power path derivative structure.
3. Test candidate positive-kernel / Gram / Loewner representations symbolically.
4. Determine whether the negative rank-one prime jumps can be compensated by an analytically positive archimedean/pole structure on the pole-neutral subspace.
5. Search for a uniform-in-(c,N) inequality, not isolated eigenvalue positivity.
6. Extend the analysis to the odd sector.
7. Audit the sine-Loewner/operator bridge against the exact finite Weil construction.
8. Assemble the full Weil criterion only after the sign theorem and limiting argument are closed.

## Hard stop

No finite certificate, zero matching, spectral convergence, or numerical stability result may be promoted to a proof of RH without an analytic theorem covering all required parameters and the final limit.

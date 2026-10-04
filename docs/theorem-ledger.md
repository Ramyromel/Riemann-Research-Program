# Theorem Ledger

## T-001 — Riemann Hypothesis
**Status:** EXTERNAL / OPEN PROBLEM.

## T-002 — Weil explicit formula
**Status:** EXTERNAL THEOREM.

## T-003 — Weil criterion
**Status:** EXTERNAL THEOREM. RH-equivalent sign condition on the required convolution/autocorrelation class with pole constraints.

## T-004 — Finite Guinand–Weil dictionary and archimedean tail theorem
**Source:** Groskin, arXiv:2607.02828v3 (2026).

For fixed finite parameters, the real-even Galerkin construction has an exact map to admissible band-limited Guinand–Weil test functions, and the cutoff-free finite quadratic value equals the corresponding zero-side sum. The omitted archimedean tail is a positive Cauchy–Stieltjes increment with an explicit certification budget.

**Status:** EXTERNAL THEOREM UNDER PROJECT AUDIT.

No global positivity or RH inference is imported.

## T-005 — Compact-window certified positivity
Recent work gives rigorous positivity certificates for selected compact-support windows.

**Status:** EXTERNAL RESEARCH INPUT. Not a global theorem.

## T-006 — Global finite-to-infinite transfer
**Status:** OPEN.

### T-006A — Even-sector fixed-support factor approximation
For fixed \(L\), smooth compactly supported real-even admissible factors can be approximated in every \(C^m\) norm by finite cosine/Galerkin factors, with the two pole moments imposed exactly by a fixed two-dimensional correction. The induced autocorrelations converge and the fixed-support Weil form is continuous along the sequence.

**Status:** DERIVED. Proof recorded in docs/fixed-support-density-lemma.md.

**Limitation:** approximation does not supply the missing sign.

### T-006B — Even-sector finite positivity
\[
\langle v,Q_\infty(c,N)v\rangle\ge0
\]
for every admissible real-even finite vector and every \(c>1,N\).

**Status:** OPEN / LOAD-BEARING.

### T-006C — Odd-sector dictionary and positivity
A matching finite dictionary, constraint-preserving approximation theorem, and positivity mechanism for the odd sector.

**Status:** OPEN.

### T-006D — Full Weil assembly
Combine parity sectors, form continuity, support exhaustion, and the external Weil criterion.

**Status:** OPEN.

### T-006E — Fixed-support positivity closure
For a fixed admissible core, if finite generated admissible objects have nonnegative cutoff-free quadratic values and their quadratic values converge to the target Weil form, then target positivity follows by closedness of \([0,\infty)\). No positive spectral gap is required.

**Status:** DERIVED. Proof recorded in docs/fixed-support-positivity-transfer-theorem.md.

**Limitation:** this closes only the logical limit step. It does not prove finite positivity, finite-family density, normalization, odd-sector coverage, or RH.

### T-006F — Prime-path Loewner concavity
At fixed Galerkin level, the cutoff-free finite prime block has negative-semidefinite rank-one derivative jumps at every prime-power threshold. Equivalently, its singular second derivative is a negative-semidefinite matrix-valued von Mangoldt measure. This is an external structural theorem under audit; the Loewner-concavity consequence is derived from it.

**Status:** EXTERNAL THEOREM UNDER PROJECT AUDIT + DERIVED CONSEQUENCE.

**Limitation:** concavity of the prime block does not imply positivity of the complete matrix. The remaining load-bearing problem is domination by the pole/archimedean block on the exact pole-neutral subspace, uniformly in (c,N).

## Status rule
No numerical spectral match, finite positive-definiteness result, or external claim may be promoted to PROVED without an analytic theorem covering all parameters and the final limiting argument.

### T-006G — Pole-neutral cancellation of prime singular curvature
On the exact real-even pole-neutral family, the all-ones rank-one direction in the prime-power derivative jump acts through the (M_0) moment. Since (M_0=0) on that family, the singular prime-power curvature vanishes identically after restriction. The independent pole quadratic is also an exact square in the pole-neutral row and therefore vanishes on the same family.

**Status:** DERIVED — VERIFIED AGAINST EXTERNAL PRIMARY FORMULAS.

**Limitation:** this removes only the singular prime curvature and pole block on the restricted family. The regular prime contribution and archimedean contribution remain load-bearing.

### T-006H — Exact restricted prime–archimedean kernel reduction
After imposing the exact even-sector pole-neutral constraints, the pole term vanishes and the prime-power singular rank-one curvature vanishes through (M_0=0). The remaining restricted quadratic form is exactly the regular prime sampling functional plus the archimedean functional.

**Status:** DERIVED EXACT REDUCTION.

**Limitation:** the sign of the combined restricted form remains open. No positive-kernel representation or uniform lower bound has yet been proved.

### T-006I — Archimedean resolvent reduction

For the finite dictionary, the archimedean density admits the exact expansion
\[
h_+(r)=h_+(0)+\sum_{n\ge0}\left(\frac1{a_n}-\frac{a_n}{a_n^2+r^2/4}\right),
\qquad a_n=n+\tfrac14.
\]
Fourier transformation of the Lorentzian terms gives
\[
Q_{\mathrm{arch},\infty}(v;c)
=
\frac{h_+(0)}2K_v(1)
+
\sum_{n\ge0}\left[
\frac{K_v(1)}{2a_n}
-
L\int_0^1K_v(\omega)e^{-2La_n(1-\omega)}d\omega
\right].
\]
**Status:** DERIVED EXACT REPRESENTATION.

**Limitation:** this is not a positivity theorem. The explicit anchor \(h_+(0)K_v(1)/2\) is negative for every nonzero real-even vector because \(h_+(0)<0\) and \(K_v(1)=2\|T_v\|_2^2>0\). Any proof must account for compensation by the remaining resolvent terms and prime sampling.


### T-006J — Exact finite sum-level/Hankel representation of the Prime–Weil block

For the real-even cosine basis
\[
\phi_0(t)=1,\qquad \phi_k(t)=\sqrt2\cos(2\pi kt),
\]
define
\[
B_{ij}(\omega)=\int_0^\omega \phi_i(t)\phi_j(\omega-t)\,dt.
\]
Then the audited prime functional has the exact finite matrix representation
\[
Q_{\mathrm{prime}}(v;c)
=
v^{\mathsf T}
\left[
-2\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}B(\omega_q)
\right]v.
\]
Equivalently, the distributional kernel is
\[
H_c(t,s)
=
-2\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}\,
\delta(t+s-\omega_q),
\]
a weighted discrete Hankel/sum-level operator.

**Status:** DERIVED EXACT FINITE REPRESENTATION; INDEPENDENT NUMERICAL AUDIT VERIFIED.

**Limitation:** this is an exact representation of the prime block, not a positivity theorem. The joint prime–archimedean sign problem and infinite-dimensional operator identification remain open.


### T-HP-001 — Finite Hilbert–Pólya Prime–Weil pencil

A 2026 external construction (Yaoming Shi, arXiv:2609.04908) defines finite real-symmetric Prime–Weil matrices from pole, archimedean, and prime-power data and formulates a Hermitian definite generalized eigenproblem on a fixed zero-mean contrast space. The project adopts this as an **external candidate architecture under independent reconstruction**, not as an imported theorem proving RH.

The repository's candidate finite Hamiltonian is represented abstractly by
\[
S_{N,c}x=\lambda G_Nx,\qquad G_N\succ0,
\]
with standard-form operator \(H_{N,c}=G_N^{-1/2}S_{N,c}G_N^{-1/2}\).

**Status:** EXTERNAL RESEARCH INPUT + DERIVED PROJECT DESIGN.

**Limitations:** exact reconstruction from this repository's normalization, arithmetic trace identity, infinite-dimensional operator convergence, spectral identification with zeta zeros, and exclusion of spurious spectrum remain OPEN. Zero-side interpolation using known ordinates is classified as reconstruction only.

### T-006K — Shared-basis Archimedean Hankel matrix

On the real-even cosine basis, the exact cutoff-free archimedean resolvent identity induces the finite matrix
\[
A^{\\mathrm{arch}}_{ij}=h_+(0)\\delta_{ij}+\\sum_{n\\ge0}\left[\\frac{\\delta_{ij}}{a_n}-2L\\int_0^1B_{ij}(\\omega)e^{-2La_n(1-\\omega)}d\\omega\right],
\\qquad a_n=n+\\tfrac14.
\]
The inner Laplace integrals have an exact finite Fourier evaluation. Numerical implementation truncates only the outer series. **DERIVED EXACT FINITE FORM; NUMERICAL SERIES EVALUATION.** This does not establish positivity or RH.

### T-006L — Certified Archimedean resolvent tail bound

Integration by parts gives an exact endpoint-cancelled expression for each resolvent summand and an explicit (O(N_T^{-1})) tail bound. A finite Fourier coefficient (L^1) bound yields a rigorous Frobenius-norm envelope for the omitted finite-basis matrix tail. This certifies numerical truncation error but does not establish positivity. **DERIVED.**


### T-006M — Pole-neutral second-order Archimedean tail bound

For a real-even finite vector on the exact pole-neutral family,
[
M_0(v)=v_0+sqrt2sum_{k=1}^N v_k=0,
]
the associated trigonometric polynomial satisfies (T_v(0)=T_v(1)=0). Hence
[
K_v'(0)=K_v'(1)=0.
]
Applying integration by parts twice to the omitted Archimedean resolvent series gives
[
|R_{N_T}(v)|
le
rac{M_2(v)}{8L^2}
sum_{n=N_T}^{infty}(n+	frac14)^{-3},
]
where (M_2(v)) bounds (sup_{omegain[0,1]}|K_v''(omega)|). A finite-Fourier coefficient envelope provides an explicit conservative Frobenius bound for (M_2).

**Status:** DERIVED — POLE-NEUTRAL RESTRICTION ONLY.

**Consequence:** the restricted truncation envelope improves from (O(N_T^{-1})) to (O(N_T^{-2})). At (c=20,N=2,N_T=1000), the conservative second-order envelope is approximately (2.99	imes10^{-6}), versus approximately (2.99	imes10^{-3}) from the unrestricted first-order bound.

**Limitation:** this does not by itself certify the sign of the finite restricted matrix; the computed finite spectral value still requires a separate numerical/interval certification if it is to be called a rigorous eigenvalue bound.


### T-006N — N=2 pole-neutral scalar reduction and truncation-corrected positive margin

For (N=2), the two exact pole-neutral constraints leave a one-dimensional admissible subspace. The restricted combined Prime–Weil form therefore reduces exactly to a scalar Rayleigh quotient.

At (c=20), high-precision evaluation gives a positive truncated value at (N_T=1000) and (N_T=10000). Combining this with the derived second-order Archimedean tail bound leaves a positive **numerical** residual margin.

**Status:** INTERVAL-CERTIFIED — LOCAL FINITE PARAMETER CASE.

A dedicated `mpmath.iv` enclosure plus the derived second-order Archimedean tail bound certifies the corrected lower endpoint for the specific case (c=20,N=2,T=1000). CI execution is green.

**Not proved:** this covers only one cutoff and one Galerkin dimension. It does not imply finite positivity for general (N,c), global Weil positivity, the infinite-dimensional limit, or RH.


### T-006O — N=2 interval-certified cutoff grid

For N=2 and T=1000, the exact pole-neutral scalar reduction has been enclosed with interval arithmetic at 60 decimal digits for the explicit cutoff grid c ∈ {10, 20, 30, 50, 100}. The conservative second-order Archimedean tail upper bound is subtracted from the finite lower endpoint before certification. GitHub Actions executed the grid calculation and its two pytest checks successfully.

The corrected lower endpoints are approximately:
- c=10: 9.9830624573e-5
- c=20: 3.3323946467e-5
- c=30: 2.7126009449e-5
- c=50: 3.5127976196e-6
- c=100: 4.0722258204e-6

**Status:** INTERVAL-CERTIFIED — EXPLICIT LOCAL FINITE GRID.

**Limitations:** this certifies only the listed five cutoffs at N=2 and T=1000. It does not prove finite positivity for arbitrary c or N, does not address N>2 certified nullspace reduction, does not close the infinite-dimensional limit, and does not prove RH. A failed certificate outside this grid would be INCONCLUSIVE rather than a counterexample unless the enclosure itself is mathematically shown to exclude zero.


### T-006P — N=3 restricted matrix frontier

For N=3, the exact two-dimensional pole-neutral space has been constructed and the combined Prime + truncated Archimedean matrix has been evaluated at c = 10, 20, 50 and T = 1000, 4000. The smallest restricted eigenvalue approaches zero as the Archimedean cutoff is increased.

**Status:** DISCOVERY / OPEN / LOAD-BEARING.

The finite values are not interval-certified eigenvalue bounds and do not constitute a counterexample. The next obligation is a matrix-level enclosure or a structural explanation of the near-null direction.

### T-006Q — Support-compression theorem target

Let (A_a) denote the localized Weil operator in the repository normalization on the real pole-neutral test core with physical logarithmic support radius (a=L/2). The target theorem is
[
E_{a,b}^{*}A_bE_{a,b}=A_a,qquad 0<a<b.
]

If this identity is proved, then positivity on any cofinal sequence (a_j\to\infty) implies positivity for every finite support radius by direct compression.

**Status:** TARGET / UNVERIFIED.

The proof obligation is to derive, without importing an external theorem:
1. exact archimedean/potential cancellation under zero extension;
2. polar-term compatibility in physical coordinates;
3. exact prime-power activation and zero old-old overlap for newly activated translations;
4. assembly into the full compression identity.

This target is intended to replace, not merely supplement, the current finite-dimensional spectral-limit bottleneck.

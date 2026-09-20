# Fixed-Support Even-Sector Density Lemma

**Status:** DERIVED — even-sector approximation result; does not prove positivity or RH

Fix \(L>0\). Let \(f\in C_c^\infty(0,L)\) be real and invariant under \(x\mapsto L-x\), with the two pole-neutral moment constraints of the chosen Weil normalization.

Because \(f\) vanishes near both endpoints, its periodic extension to \(\mathbb R/L\mathbb Z\) is \(C^\infty\). Its Fourier series converges in every \(C^m([0,L])\) norm. Parity removes the sine coefficients, so the partial sums have the form
\[
S_Nf(x)=a_0+\sum_{k=1}^{N}a_k\cos(2\pi kx/L).
\]
After the unitary rescaling used by the finite dictionary, these are exactly real-even Galerkin factors.

Let \(M_+\) and \(M_-\) be the two pole moments. Choose two real-even trigonometric polynomials \(p,q\) for which
\[
\det\begin{pmatrix}M_+(p)&M_+(q)\\M_-(p)&M_-(q)\end{pmatrix}\ne0.
\]
Such a pair exists because otherwise the two distinct exponential moment functionals would be linearly dependent on a dense trigonometric algebra and hence on the whole smooth even space.

For sufficiently large \(N\), choose \(\alpha_N,\beta_N\) so that
\[
f_N=S_Nf-\alpha_Np-\beta_Nq
\]
satisfies \(M_+(f_N)=M_-(f_N)=0\) exactly. Since the unconstrained Fourier approximants converge and the target moments vanish, \(\alpha_N,\beta_N\to0\). Hence \(f_N\to f\) in every \(C^m\) norm while preserving both constraints exactly.

For
\[
g_N=f_N*\widetilde{f_N},\qquad g=f*\widetilde f,
\]
Young's inequality gives
\[
\|g_N-g\|_\infty\le(\|f_N\|_2+\|f\|_2)\|f_N-f\|_2.
\]
Thus \(g_N\to g\) uniformly. Higher \(C^m\) convergence supplies uniform high-order derivative control, so repeated integration by parts gives an integrable majorant against the archimedean density \(O(\log(2+|r|))\). The archimedean contribution therefore converges by dominated convergence. For fixed support only finitely many prime powers contribute, so the prime contribution also converges.

**Result:** the even-sector fixed-support approximation/continuity mechanism is derived.

**Limitation:** this does not prove positivity. The load-bearing unresolved issue is positivity of the cutoff-free finite matrices for the whole admissible finite family. The current finite dictionary is explicitly stated for the real-even sector, so an odd-sector dictionary and positivity mechanism are still required for the full Weil criterion.


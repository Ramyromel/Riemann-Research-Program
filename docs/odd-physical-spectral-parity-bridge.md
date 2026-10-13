# Odd physical/spectral parity bridge

## Status

**NUMERICALLY SUPPORTED; ANALYTIC IDENTIFICATION STILL OPEN.**

The physical odd basis on (-1,1) is

\[
\phi_k(x)=\sin(k\pi x).
\]

The repository Volterra coordinate is \(w=(x+1)/2\), so the basis relation is exact:

\[
\phi_k(2w-1)
=\sin(2\pi k w-k\pi)
=(-1)^k\sin(2\pi k w).
\]

Define \(D_N=\operatorname{diag}((-1)^1,\ldots,(-1)^N)\). Then \(D_N^2=I\), and the matrix of one and the same bilinear operator in the two bases must obey

\[
A_{\rm phys}=D_N A_{\rm odd}D_N.
\]

This is a finite-basis coordinate-conjugation identity. It does not by itself prove that the candidate Volterra operator equals the physical Weil operator.

## Independent numerical check

The direct critical-line spectral integral and the corrected odd Volterra matrix were compared after applying \(D_N\). At \(c=20,N=6\), using \(R=500\), 100001 spectral samples, and 3000 resolvent terms, the recorded residual was:

- Frobenius norm: \(2.5567112\times10^{-6}\)
- Maximum entrywise residual: \(1.3526933\times10^{-6}\)

The CI test also checks \(c=8,N=2\) and \(c=20,N=6\) under a \(2\times10^{-4}\) tolerance. These are numerical consistency checks, not a proof of the infinite resolvent identity.

## What the parity audit corrected

Before conjugation, the discrepancy had an alternating-sign pattern in off-diagonal entries. The exact basis identity explains why comparing the two matrices entry-by-entry without \(D_N\) was the wrong comparison. This supersedes the earlier interpretation that the raw mismatch alone demonstrated a failure of the odd resolvent.

## Remaining analytic obligations

1. Derive the Fourier/Mellin normalization from the repository's explicit-formula convention.
2. Derive the autocorrelation sign and all scale factors analytically.
3. Prove the infinite resolvent expansion, including its tail and endpoint terms.
4. Establish equality of the complete Archimedean operators, not only truncated matrices.
5. Assemble the prime-power shifts and polar rank-one term under the same normalization.
6. Only then resume compression and positivity arguments.

Current classification: **NUMERICALLY SUPPORTED / ANALYTIC BRIDGE OPEN**. No positivity result or Riemann Hypothesis proof follows from this audit.

## Analytic tail control for the anchored resolvent series

This section closes one convergence obligation for the *finite-basis scalar resolvent series*; it does not identify that series with the complete physical Weil operator.

For fixed basis indices (i,j), let (K_{ij}:[0,1]\to\mathbb R) be the finite convolution kernel used by the corrected odd-sine construction. It is a finite trigonometric-polynomial expression plus polynomial factors, hence is continuously differentiable. Put (L=\log c>0), (a_n=n+\tfrac14), and
\[
B_n=\frac{K_{ij}(1)}{2a_n}
-L\int_0^1 K_{ij}(w)e^{-2La_n(1-w)}\,dw.
\]
With \(\lambda_n=2La_n\), direct integration of the constant endpoint value gives the exact identity
\[
B_n=\frac{K_{ij}(1)e^{-\lambda_n}}{2a_n}
+L\int_0^1\bigl(K_{ij}(1)-K_{ij}(1-t)\bigr)e^{-\lambda_n t}\,dt.
\]
If \(M_{ij}=\sup_{0\le w\le1}|K'_{ij}(w)|\), the mean-value theorem yields
\[
|K_{ij}(1)-K_{ij}(1-t)|\le M_{ij}t.
\]
Consequently,
\[
|B_n|\le \frac{|K_{ij}(1)|e^{-2La_n}}{2a_n}
+\frac{L M_{ij}}{(2La_n)^2}
=\frac{|K_{ij}(1)|e^{-2La_n}}{2a_n}
+\frac{M_{ij}}{4L a_n^2}.
\]
For every fixed \(c>1\), the right-hand side is summable in \(n\). Thus the anchored resolvent series converges absolutely entrywise for each fixed finite basis, and its tail after index \(T-1\) obeys the explicit bound
\[
\sum_{n=T}^{\infty}|B_n|
\le \frac{|K_{ij}(1)|}{2}
\sum_{n=T}^{\infty}\frac{e^{-2La_n}}{a_n}
+\frac{M_{ij}}{4L}\sum_{n=T}^{\infty}\frac1{a_n^2}.
\]
A simpler fully elementary bound follows from \(a_n\ge n\) for \(n\ge1\):
\[
\sum_{n=T}^{\infty}|B_n|
\le \frac{|K_{ij}(1)|}{2}\frac{e^{-2L(T+1/4)}}{(T+1/4)(1-e^{-2L})}
+\frac{M_{ij}}{4L}\frac1{T-1/4},\qquad T\ge1,
\]
where the first term uses \(a_n\ge T+1/4\) and a geometric-series bound, and the second uses a safe integral comparison
\(\sum_{n=T}^{\infty}(n+1/4)^{-2}\le (T+1/4)^{-2}+(T+1/4)^{-1}\).

**Scope warning.** This proves convergence and gives a conservative finite-basis tail estimate for the displayed anchored series. It does not prove positivity, uniformity as \(N\to\infty\) or \(c\downarrow1\), nor equality with the full physical Archimedean operator. The constants \(M_{ij}\) must be bounded or computed with certified arithmetic before the estimate can serve as a numerical certificate.


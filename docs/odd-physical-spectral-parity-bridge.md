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

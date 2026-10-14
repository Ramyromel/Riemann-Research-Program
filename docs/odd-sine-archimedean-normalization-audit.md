# Odd sine Archimedean normalization audit

**Status: DERIVED FORM; DIRECT PHYSICAL MATCH OPEN**

The odd basis is psi_k(w)=sqrt(2) sin(2 pi k w), k>=1, equivalently phi_k(x)=sin(k pi x) under x=2w-1.

For the repository Volterra convention K=2B, the raw endpoint convolution satisfies B_ij(1)=-delta_ij and K_ij(1)=-2 delta_ij. Therefore the exact odd-parity analogue of the existing cutoff-free Archimedean resolvent representation has anchor -h_+(0) I, where h_+(0)=digamma(1/4)-log(pi), followed by the same resolvent terms with a_n=n+1/4 and L=log(c).

The implementation in experiments/odd_sine_archimedean_diagnostic.py evaluates all finite Fourier/Volterra entries analytically and uses no RH-zero data.

## Critical boundary

This establishes only the parity-correct resolvent representation relative to the repository's existing normalization. It does NOT yet prove that this matrix equals the direct physical matrix H_Leg + c0(a)I + V - K_gamma,a entry-by-entry. That direct physical normalization bridge remains load-bearing and open.

The external Sept-2026 preprint arXiv:2609.20367 independently states the same normalized localized target, including the H_Leg, c0(a), V, K_gamma,a, polar, and translated-prime blocks. It is treated here only as a benchmark; no theorem from it is imported.

**No RH claim.**

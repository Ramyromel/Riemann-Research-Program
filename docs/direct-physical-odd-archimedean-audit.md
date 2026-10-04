# Direct physical odd Archimedean audit

**Status: NUMERICAL MISMATCH — NORMALIZATION BRIDGE NOT CLOSED**

A direct independent discretization was added in `experiments/direct_physical_odd_archimedean_audit.py` for the physical normalized form

`H_Leg + c0(a) I + V - K_gamma,a`

on `(-1,1)` using `phi_k(x)=sin(k*pi*x)` and Gauss-Legendre quadrature. It is compared against the repository's odd resolvent implementation.

For the first load-bearing test point `c=20`, `N=6`, `a=0.5*log(20)`, the direct matrix converges under increasing quadrature order, but it does **not** agree entry-by-entry with the current odd resolvent matrix. With order 160 the direct smallest eigenvalue is approximately `-1.46068993485`, while the resolvent diagnostic gives approximately `-0.66954181886` at the shortened 300-term local reproduction. The Frobenius discrepancy is about `3.4592`.

This is not being interpreted as a counterexample to RH. It means the physical-to-resolvent normalization/coordinate bridge is still incomplete (and may contain a sign, kernel, or transform convention error). The mismatch is useful: it prevents the current resolvent object from being promoted to the physical Weil operator without proof.

The external benchmark defines the normalized localized target as `H_Leg + c0(a)I + V - K_gamma,a` plus the polar rank-one and translated-prime terms, with `rho(z)=e^{-z/2}/(1-e^{-2z})-1/(2z)` and `c0(a)=-log(a)-log(2*pi)-gamma`. It is used only as a benchmark, not imported as proof.

## Next mandatory repair

1. Re-derive the Fourier-side transform of the physical odd sine basis directly from the repo's Weil normalization.
2. Track every factor of 2 from `x=2w-1`, `r=log(n)/a`, and `Delta=L/(2*pi)`.
3. Derive the physical Archimedean kernel from the explicit formula before using the existing cosine-sector resolvent identity.
4. Only after entrywise equality is established may the resolvent series be used in the compression/positivity chain.

**No RH claim.**

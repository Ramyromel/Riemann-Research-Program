# Parity and normalization audit

**Status: LOAD-BEARING / OPEN**

## Finding

The current finite Prime-Weil/Hankel implementation uses the orthonormal cosine basis

$$1,\ \sqrt2\cos(2\pi k w),\qquad 0\le w\le1.$$

Under the physical coordinate

$$y=L(w-1/2),\qquad a=L/2,$$

this basis becomes an even basis in y because reflection y -> -y is w -> 1-w and

$$\cos(2\pi k(1-w))=\cos(2\pi k w).$$

Therefore the existing N=2/N=3 finite matrices are not automatically the real odd logarithmic channel used by the support-compression route.

## Consequence

The exact compression identity derived in the physical odd channel cannot simply be attached to the existing cosine-basis matrices. A parity-preserving normalization bridge is required first.

The natural odd basis would use functions proportional to

$$\sin(2\pi k w),$$

which become odd under y -> -y. However, the pole-neutral constraints and the exact finite Prime-Weil matrix must be re-derived for that basis rather than copied from the cosine sector.

## Required derivation

1. Start from the physical Weil quadratic form in y.
2. Derive its odd restriction under y -> -y.
3. Map y=L(w-1/2) and derive the sine-basis matrix from the same explicit formula.
4. Derive the polar rank-one term in that basis.
5. Derive the exact pole-neutral constraints in the odd sector.
6. Compare the resulting odd matrix with the existing Hankel/resolvent representation.
7. Only after this bridge is proven, apply the exact zero-extension compression identity.

## Research implication

This is preferable to silently assuming that the current finite matrices already represent the odd localized operator. If the bridge succeeds, the support-monotone route can attack the actual RH-equivalent channel. If it fails, the discrepancy itself is a mathematically useful obstruction.

## Status ledger

| Item | Status |
|---|---|
| Existing cosine basis is even in physical y | DERIVED |
| Existing finite matrices = odd localized operator | NOT ESTABLISHED |
| Odd sine-basis finite formulation | OPEN |
| Odd pole-neutral constraints | OPEN |
| Compression identity for physical odd operator | DERIVED CONDITIONALLY |
| Compression identity for existing finite matrices | OPEN |
| RH | OPEN |
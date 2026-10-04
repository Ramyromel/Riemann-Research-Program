# Odd sine-basis physical normalization audit

**Status: PHYSICAL ARITHMETIC BLOCK DERIVED; FULL NORMALIZATION OPEN**

## 1. Physical odd basis

Use the physical logarithmic coordinate (x=y/ain(-1,1)), where
[
a=rac12log c.
]
The orthonormal real odd basis is
[
phi_k(x)=sin(kpi x),qquad kge1.
]

Under (x=2w-1),
[
phi_k(2w-1)=(-1)^ksin(2pi kw),
]
so this is the same parity sector as the sine basis in (w), with the unitary normalization made explicit.

## 2. Correct prime-power translation block

For (q=p^m<c=e^{2a}), the physical localized translation is
[
(S_{r_q}f)(x)=mathbf 1_{(-1,1)}(x+r_q)f(x+r_q),
qquad
r_q=rac{log q}{a}.
]

The exact arithmetic contribution is
[
A_{m prime}
=
-sum_{q=p^m<c}
rac{Lambda(q)}{sqrt q}
left(S_{r_q}+S_{r_q}^{*}ight).
]

Therefore its finite odd-basis matrix is
[
(P_{m odd})_{ij}
=
-sum_{q=p^m<c}rac{Lambda(q)}{sqrt q}
left(
int_{-1}^{1-r_q}phi_i(x)phi_j(x+r_q),dx+
int_{-1}^{1-r_q}phi_j(x)phi_i(x+r_q),dx
ight).
]

The integral is evaluated exactly by the product-to-sum identity for sines; no quadrature approximation is needed.

### Important correction

The first odd-sector prototype used
[
int_0^{omega_q}psi_i(t)psi_j(t),dt.
]
That is a same-point truncated Gram integral, not the physical translated operator. It has therefore been **retired as the arithmetic representation**.

This correction is itself a successful normalization audit: we detected that the old prototype could not be identified with the physical shift before allowing it into the proof chain.

## 3. CI result

The corrected physical translation implementation is now the source of the odd arithmetic diagnostic.

At (c=20,N=6), the physical arithmetic block has
[
lambda_{min}approx -0.5538245571
]
in the finite odd basis.

This value is a property of the arithmetic block alone. It is neither a proof nor a counterexample to RH.

## 4. Archimedean parity check

For the localized convolution
[
K_{ij}(omega)=
int_0^omega
psi_i(t)psi_j(omega-t),dt,
]
the odd basis satisfies
[
K_{ij}(1)=-2delta_{ij}.
]

Consequently the anchor term in the existing resolvent identity changes sign relative to the even cosine sector. This has been isolated in a separate diagnostic and is **not yet identified with the complete physical odd operator**.

## 5. Remaining load-bearing bridge

The complete physical odd operator must be assembled from, and normalized against,
[
H_{m Leg}+c_0(a)I+V-K_{gamma,a}
-2|s_aanglelangle s_a|
-sum_{q<c}rac{Lambda(q)}{sqrt q}(S_{r_q}+S_{r_q}^*),
]
where
[
s_a(x)=sqrt a,sinh(ax/2).
]

The remaining obligations are:

1. independently derive this complete physical form from the repository's Weil normalization;
2. derive the (H_{m Leg}), endpoint potential, gamma, and polar matrices in the same sine basis;
3. prove the normalization equivalence to the repository's existing finite formulation;
4. then prove exact zero-extension compression.

Until those identities are established, no finite odd matrix is promoted to a proof object.

**No RH claim is made.**

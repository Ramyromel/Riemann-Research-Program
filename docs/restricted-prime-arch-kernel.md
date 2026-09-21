# Restricted Prime–Archimedean Kernel Target

**Status:** DERIVED EXACT REDUCTION  
**Scope:** real-even pole-neutral finite family  
**Does not prove:** positivity or RH

## 1. Exact prime contribution

With
\[
L=\log c,\qquad
\omega_q=1-\frac{\log q}{L},
\]
and
\[
K_v(\omega)=2\int_0^\omega T_v(t)T_v(\omega-t)\,dt,
\]
the exact finite dictionary gives
\[
\widehat g_v\!\left(\frac{\log q}{2\pi}\right)
=
\pi K_v(\omega_q).
\]

Hence the prime contribution is exactly
\[
Q_{\mathrm{prime}}(v;c)
=
-\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}\,
K_v(\omega_q).
\]

No numerical approximation is present in this identity.

## 2. Pole-neutral restriction

On the exact pole-neutral family,
\[
g_v(i/2)=0,
\]
so the pole contribution vanishes:
\[
Q_{\mathrm{pole}}(v;c)=0.
\]

The prime-power singular derivative measure also vanishes after restriction because its quadratic action is proportional to \(M_0(v)^2\), with \(M_0(v)=0\).

Therefore the finite sign problem on this family reduces to the exact scalar functional
\[
Q_{\mathrm{PN}}(v;c)
=
-\sum_{q\le c}
\frac{\Lambda(q)}{\sqrt q}\,
K_v(\omega_q)
+
Q_{\mathrm{arch},\infty}(v;c).
\]

## 3. Archimedean term

Using the standard archimedean density \(h_+(r)\),
\[
Q_{\mathrm{arch},\infty}(v;c)
=
\frac{1}{2\pi}
\int_{\mathbb R}
h_+(r)\,g_v(r)\,dr
\]
under the normalization already audited in the repository.

Thus
\[
\boxed{
Q_{\mathrm{PN}}(v;c)
=
-\sum_{q\le c}
\frac{\Lambda(q)}{\sqrt q}K_v(\omega_q)
+
\frac{1}{2\pi}\int_{\mathbb R}h_+(r)g_v(r)\,dr
}
\]
is the exact restricted target.

## 4. What a proof must now establish

The required theorem is
\[
Q_{\mathrm{PN}}(v;c)\ge0
\]
for every admissible pole-neutral finite vector \(v\), with the appropriate \(c,N\) range.

There are now no hidden pole terms and no singular prime-power rank-one curvature terms in this restricted quadratic form.

The remaining difficulty is the sign of the **regular prime sampling functional versus the archimedean functional**.

## 5. Three possible closure mechanisms

### A. Common positive kernel

Find a positive measure \(\mu_{c,N}\) and an explicit transform \(\Phi_v\) such that
\[
Q_{\mathrm{PN}}(v;c)=\int |\Phi_v(x)|^2\,d\mu_{c,N}(x).
\]

### B. Reproducing-kernel/Gram representation

Show that the restricted matrix equals
\[
Q_{\mathrm{PN}}^{\mathrm{PN}}(c,N)=G(c,N)^*G(c,N)
\]
or a Schur complement of a positive block matrix.

### C. Exact lower bound

Derive
\[
Q_{\mathrm{arch},\infty}(v;c)
\ge
\sum_{q\le c}
\frac{\Lambda(q)}{\sqrt q}K_v(\omega_q)
\]
on the pole-neutral space.

The third form is a direct inequality; the first two would explain its structural origin.

## 6. Adversarial branch

The same exact formula gives a rigorous counterexample strategy. If a pole-neutral \(v\) produces
\[
Q_{\mathrm{PN}}(v;c)<0,
\]
then universal finite positivity for that parameter pair fails.

Such a counterexample would not disprove RH by itself; it would instead falsify this finite route or the chosen restricted family.

## 7. Classification

- Exact restricted prime formula: **DERIVED / EXTERNAL THEOREM UNDER AUDIT**.
- Pole cancellation: **VERIFIED / DERIVED**.
- Singular-curvature cancellation: **DERIVED**.
- Restricted positivity: **OPEN / LOAD-BEARING**.
- Common positive-kernel representation: **OPEN**.
- Odd sector: **OPEN**.
- Global Weil positivity: **OPEN**.
- RH: **OPEN**.

No RH inference is made.

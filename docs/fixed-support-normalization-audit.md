# Fixed-Support Normalization Audit

**Status:** SUBSTANTIALLY RESOLVED AT THE FINITE FACTOR LEVEL; GLOBAL POSITIVITY REMAINS OPEN

Fix \(c>1\), \(L=\log c\), \(\Delta=L/(2\pi)\), and \(\rho=2\pi/L\). On \([0,L]\) use \(U_n(x)=L^{-1/2}e^{2\pi i n x/L}\). For the real-even sector,
\[
u_0=v_0,\qquad u_k=u_{-k}=v_k/\sqrt2,
\]
and
\[
T_v(t)=\sum_{m=-N}^{N}u_me^{2\pi imt},\qquad
f_v(x)=L^{-1/2}T_v(x/L).
\]

The exact Volterra map is
\[
K_v(\omega)=2\int_0^\omega T_v(t)T_v(\omega-t)\,dt,
\]
\[
\widehat g_v(\xi)=\pi K_v(1-|\xi|/\Delta)\quad(|\xi|\le\Delta),
\]
with zero extension outside the band, and
\[
g_v(z)=\int_{-\Delta}^{\Delta}\widehat g_v(\xi)e^{2\pi iz\xi}\,d\xi.
\]

The corresponding multiplicative object is \(F_v(x)=q(f_v,f_v)(\log x)\). Thus the earlier schematic bridge is now explicit:
\[
v\to T_v\to f_v\to q(f_v,f_v)\to\widehat g_v\to g_v.
\]

For the divided-difference matrix
\[
(Q_\psi)_{mn}=
\begin{cases}
(\psi(m)-\psi(n))/(m-n),&m\ne n,\\
\psi'(m),&m=n,
\end{cases}
\]
the prime, pole and archimedean blocks assemble to
\[
Q_\infty=Q_{\rm prime}^{(c)}+Q_{\rm pole}+Q_{\rm arch,\infty}.
\]

Groskin's finite dictionary gives, for real-even \(v\),
\[
\langle v,Q_\infty v\rangle
=
\sum_{\rho\in Z_\zeta^*}g_v(z_\rho),
\]
equivalently
\[
\langle v,Q_\infty v\rangle
=
-\frac1\pi\sum_{q=p^a\le c}\frac{\Lambda(q)}{\sqrt q}
\widehat g_v\!\left(\frac{\log q}{2\pi}\right)
+2g_v(i/2)
+\frac1{2\pi}\int_{\mathbb R}h_+(r)g_v(r)\,dr.
\]

This is an exact finite-level identity, not a numerical approximation. The primary normalization ambiguities—\(L=\log c\), Haar/log scaling, Fourier \(2\pi\) convention, the \(1/2\) shift, basis normalization, Volterra normalization, prime cutoff, and sign convention—are therefore no longer the principal blocker.

The standard Weil formulation has two pole-neutral moment constraints. The finite construction contains an exact pole-neutral subspace, and the even-sector density lemma now supplies a fixed-window constrained approximation mechanism.

**Revised classification**
- Finite normalization bridge: VERIFIED AGAINST PRIMARY FORMULAS / EXTERNAL THEOREM
- Finite dictionary: EXTERNAL THEOREM UNDER PROJECT AUDIT
- Even constrained density: DERIVED
- Volterra/convolution continuity: DERIVED
- Fixed-support finite-prime reduction: DERIVED
- Odd-sector finite dictionary/density: OPEN
- Even finite positivity: OPEN
- Global Weil positivity: OPEN
- RH: OPEN

# Fixed-Support Positivity Transfer Theorem

**Status:** DERIVED — CONDITIONAL CLOSURE RESULT  
**Scope:** fixed admissible test function / fixed-support approximation  
**Does not prove:** finite positivity, global positivity, or RH

## 1. Statement

Let \(D_0\) be an admissible core of Weil test functions. Let \(Q:D_0\to\mathbb R\) be the target Weil quadratic form.

Suppose that for every \(f\in D_0\) there exists a sequence \(f_n\) such that:

1. \(f_n\) belongs to a finite generated admissible family;
2. every \(f_n\) satisfies the exact pole/moment constraints required by the chosen Weil criterion;
3. the finite construction has a cutoff-free quadratic value \(Q_n(f_n)\);
4. \(Q_n(f_n)\ge 0\) for every \(n\);
5. \(Q_n(f_n)-Q(f_n)\to0\);
6. \(Q(f_n)\to Q(f)\).

Then \(Q(f)\ge0\) for every \(f\in D_0\).

If, in addition, \(D_0\) is dense in the full Weil test-function domain for a topology in which \(Q\) is continuous, then \(Q\ge0\) on the full domain.

## 2. Proof

Fix \(f\in D_0\). By assumptions 5 and 6,
\[
Q_n(f_n)\longrightarrow Q(f).
\]
Every term of the sequence is nonnegative by assumption 4. The nonnegative half-line is closed in \(\mathbb R\). Therefore
\[
Q(f)=\lim_{n\to\infty}Q_n(f_n)\ge0.
\]

For the final extension, let \(f\) be any element of the full domain and choose \(f^{(k)}\in D_0\) converging to \(f\) in the topology for which \(Q\) is continuous. Since \(Q(f^{(k)})\ge0\) for every \(k\),
\[
Q(f)=\lim_{k\to\infty}Q(f^{(k)})\ge0.
\]
This proves the claimed closure.

## 3. Error decomposition

The convergence hypothesis should be established through an explicit decomposition
\[
Q_n(f_n)-Q(f)
=
\underbrace{Q_n(f_n)-Q(f_n)}_{\text{finite-to-exact error}}
+
\underbrace{Q(f_n)-Q(f)}_{\text{approximation error}}.
\]

A sufficient quantitative condition is
\[
|Q_n(f_n)-Q(f_n)|\le \varepsilon_n(f),
\qquad
|Q(f_n)-Q(f)|\le \eta_n(f),
\]
with
\[
\varepsilon_n(f)\to0,\qquad \eta_n(f)\to0.
\]
Then
\[
|Q_n(f_n)-Q(f)|\le\varepsilon_n(f)+\eta_n(f)\to0.
\]

No positive spectral gap is required. In particular, the argument remains valid when \(Q(f)=0\) or when the finite values approach zero.

## 4. Fixed-support specialization

For a fixed compact-support core, the arithmetic prime contribution has only finitely many terms once the support convention is fixed. Thus its convergence reduces to convergence of the associated test functions.

For the archimedean contribution, the required task is an integrable majorant or another explicit continuity estimate strong enough to justify
\[
Q_{\rm arch}(f_n)\to Q_{\rm arch}(f).
\]

For autocorrelation factors \(g_n=f_n*\widetilde f_n\), an \(L^2\)-convergent factor sequence gives
\[
\|g_n-g\|_\infty
\le
(\|f_n\|_2+\|f\|_2)\|f_n-f\|_2
\]
on a fixed finite-support interval. Higher regularity can then be used to obtain the decay/majorant required by the archimedean term.

## 5. What this closes

This theorem closes the **logical closure step** once the finite-to-exact error and approximation continuity have actually been proved for the concrete finite dictionary.

It eliminates the need for a uniform positive lower bound. A margin-free limit is sufficient.

## 6. What remains load-bearing

This result does **not** establish any of the following:

- nonnegativity of the cutoff-free finite matrices;
- compatibility of the concrete finite Volterra image with every required admissible factor;
- vanishing constraint-correction bounds;
- a complete normalization bridge to the project's chosen Weil convention;
- odd-sector coverage;
- density/closure of the resulting family in the full Weil criterion;
- the external Weil criterion itself.

Therefore no RH conclusion follows from this theorem alone.

## 7. Research status

**DERIVED.** The proof is elementary, but its hypotheses are deliberately explicit so that future work cannot silently replace them with numerical convergence or pointwise spectral matching.

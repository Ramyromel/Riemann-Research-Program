# Proven Auxiliary Lemma — Pointwise Closure of Positivity

## Statement

Let \(D\) be a vector space and let \(Q_n:D\to\mathbb R\) and \(Q:D\to\mathbb R\) be quadratic forms.

Assume:

1. \(Q_n(f)\ge 0\) for every \(f\in D\) and every \(n\);
2. for every fixed \(f\in D\),
   \[
   \lim_{n\to\infty}Q_n(f)=Q(f).
   \]

Then

\[
Q(f)\ge0
\qquad\text{for every }f\in D.
\]

## Proof

Fix any \(f\in D\). By assumption, \(Q_n(f)\ge0\) for every \(n\). A convergent sequence of real numbers contained in the closed set \([0,\infty)\) has its limit in \([0,\infty)\). Therefore

\[
Q(f)=\lim_{n\to\infty}Q_n(f)\ge0.
\]

Since \(f\) was arbitrary, \(Q\) is positive semidefinite on \(D\). \(\square\)

## Why this matters

This elementary lemma identifies a precise sufficient route for positivity transfer.

A **uniform positive spectral gap is not required** if:

- the same test function \(f\) is admissible for every cutoff;
- positivity holds for that fixed \(f\) at every cutoff;
- the quadratic-form values converge pointwise to the exact limiting form.

The difficult part is therefore not the closure step itself. The difficult part is constructing finite forms with a compatible common domain, or proving a valid approximation/extension theorem when the finite domains vary.

## Variable-domain version

Suppose \(D_1\subseteq D_2\subseteq\cdots\) and \(D_\infty=\bigcup_nD_n\). If each \(Q_n\) is defined on \(D_\infty\) by an exact extension and

\[
Q_n(f)\ge0\quad\forall f\in D_\infty,
\]

then the lemma applies directly.

If \(Q_n\) is defined only on \(D_n\), positivity of \(Q_n\) alone is insufficient. One additionally needs, for each target \(f\), approximants \(f_n\in D_n\) and enough continuity/control to establish

\[
Q(f)=\lim_n Q_n(f_n)\ge0.
\]

That second implication is **not automatic**.

## Relevance to the Weil program

The exact Weil criterion uses a specified test-function class. Therefore the research question should be sharpened to:

> Can the recent finite truncated Weil constructions be placed on a common admissible test-function domain, or can their changing Galerkin domains be coupled to a density-and-continuity theorem strong enough to invoke this closure principle?

This is a narrower and more testable question than generic “eigenvalue convergence.”

## Status

**PROVED AUXILIARY LEMMA.**

This lemma is elementary and does **not** prove the Riemann Hypothesis.


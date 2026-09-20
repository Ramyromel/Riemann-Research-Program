# Critical Lemma Candidate — Positivity Transfer

## Proposed statement

Let \(Q_c\) be a family of finite/cutoff quadratic forms defined on a common test-function class or on compatible subspaces, and let \(Q\) be the exact Weil quadratic form.

A route to the global Weil criterion would require a theorem of the following general shape:

> If the domains of \(Q_c\) exhaust a dense subspace of the target domain, \(Q_c\to Q\) with an explicitly controlled error, and the finite positivity inequalities are uniform enough to survive that convergence, then \(Q\) has the required semidefinite sign on the full Weil test class.

This is deliberately a **candidate lemma**, not a theorem.

## Why the naive argument fails

The implication

\[
Q_c(f)\ge 0\quad\forall f,\;c<\infty
\quad\Longrightarrow\quad
Q(f)\ge0
\]

is invalid without a convergence statement. In particular:

- the domain may change with \(c\);
- the error \(|Q_c(f)-Q(f)|\) may dominate a vanishing finite spectral gap;
- positivity may hold only after projection to a finite-dimensional sector;
- a sequence of positive forms can converge to a form with a different sign if convergence is not established in a form topology controlling the relevant vectors.

## Immediate research task

Find the weakest practical hypotheses under which the candidate implication is valid.

### Preferred proof pattern

For fixed admissible \(f\):

\[
Q(f)=Q_c(f)+E_c(f),
\]

with an explicit bound

\[
|E_c(f)|\le \varepsilon_c\,N(f),
\qquad \varepsilon_c\to0.
\]

Then determine whether the finite inequality supplies a margin

\[
Q_c(f)\ge \varepsilon_c N(f),
\]

or whether semidefinite closure can be obtained by approximation from a dense subspace.

The key issue is that a **uniform positive lower bound is not expected globally**. Therefore a margin-free closure argument may be necessary.

## Falsification target

Search for explicit sequences \(f_c\) for which:

- \(Q_c(f_c)\ge0\),
- \(Q(f_c)<0\), or
- \(Q_c(f_c)-Q(f_c)\not\to0\) in the required topology.

A single rigorously constructed counterexample would invalidate the corresponding transfer lemma and force a new route.

## Status

OPEN / HIGH PRIORITY.

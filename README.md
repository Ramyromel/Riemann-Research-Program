# Riemann Research Program

An open research program investigating the Riemann Hypothesis through rigorous mathematical analysis, spectral methods, positivity criteria, and reproducible computational verification.

## Status

ACTIVE RESEARCH — NO PROOF CLAIMED.

The Riemann Hypothesis remains an open problem. This repository is a research program, not a claim of a solution.

Governing rule: No gap closed, no proof claim.

Results are classified as CONJECTURAL, DERIVED, NUMERICALLY_SUPPORTED, VERIFIED, PROVED, REFUTED, or BLOCKED.

## Initial focus

1. Completed zeta function and equivalent formulations of RH.
2. Weil explicit-formula quadratic form and positivity.
3. Spectral/operator formulations and the Hilbert-Polya direction.
4. Finite-dimensional approximations and the finite-to-infinite limit problem.
5. Reproducible numerical experiments for discovery and falsification.
6. Independent verification and adversarial attempts to break proposed arguments.

## Principle

A mathematically attractive construction is not a theorem. Numerical agreement is not a proof. A proof is not complete until every dependency and limiting argument is explicit.

## Initial target

Investigate whether a rigorously controlled finite spectral/positivity construction can be connected to the full Weil object in a limit that preserves the required positivity and identifies the resulting spectrum with the non-trivial zeros of the Riemann zeta function.

This is an open research question, not an asserted result.

## Public research status

**PUBLIC EXPERIMENTAL RESEARCH REPOSITORY — NO RH PROOF CLAIMED**

This repository is intentionally open for:

- reproducible experiments;
- mathematical derivations and lemma audits;
- adversarial attempts to find counterexamples or proof gaps;
- independent verification of computational and analytic results;
- discussion of alternative routes to the Riemann Hypothesis.

The project distinguishes external theorems, repository-derived results, numerical evidence, verified results, and complete proofs. See [RESEARCH_INTEGRITY.md](RESEARCH_INTEGRITY.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [RESEARCH_STATUS.md](RESEARCH_STATUS.md).

**Important:** finite numerical verification, spectral matching, finite-dimensional positivity, or an operator construction is not by itself a proof of the Riemann Hypothesis.

## Independent-review framework

The repository now includes a dedicated review layer:

- [Formal Proof Guidelines](docs/formal-proof-guidelines.md) — exact proof-boundary and function-space requirements.
- [Reproducibility Suite](verification/reproducibility/README.md) — computational reproducibility and independent-recomputation requirements.
- [Adversarial Counterexample Challenges](verification/adversarial/counterexample-challenges.md) — explicit attempts to falsify the finite-to-global, coverage, sector, spectral, and numerical claims.

These documents are deliberately designed to make the program easier to audit and harder to overclaim.

### Release audit

The 2026-09-20 public-release audit is recorded in [research-log/2026-09-20-public-release-audit.md](research-log/2026-09-20-public-release-audit.md).

Current active research branch: `main`.

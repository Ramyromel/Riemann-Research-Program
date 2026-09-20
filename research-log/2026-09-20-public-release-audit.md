# Public Release Audit — 2026-09-20

## Decision

**PUBLIC EXPERIMENTAL RESEARCH REPOSITORY — RELEASE APPROVED WITH DISCLOSED LIMITATIONS**

The repository is suitable for public research sharing because it explicitly states that no proof of the Riemann Hypothesis is claimed and records the unresolved mathematical dependencies.

## Audit scope

The release audit checked:

- public repository visibility and repository identity;
- README status language;
- global research status;
- theorem ledger;
- methodology and evidence hierarchy;
- verification requirements;
- external-source registry;
- open-gap documentation;
- searches for proof/solved language;
- presence of reproducibility and contribution guidance.

## Findings

### F-001 — No RH proof claim

The README states that the repository is active research and that no proof is claimed. The research status records RH as OPEN and a complete proof in the repository as NONE.

**Disposition:** PASS.

### F-002 — Explicit unresolved load-bearing gaps

The theorem ledger and active frontier explicitly keep global finite-to-infinite transfer, even-sector finite positivity, odd-sector coverage, full Weil assembly, and exact spectral identification open.

**Disposition:** PASS.

### F-003 — Numerical evidence is correctly bounded

The repository explicitly prevents finite certificates, numerical zero matching, and spectral convergence from being promoted to an RH proof without the required analytic theorem and final limit.

**Disposition:** PASS.

### F-004 — External work is separated from repository results

The source registry and theorem ledger identify external research inputs and state that they are not silently imported as repository-proved results.

**Disposition:** PASS.

### F-005 — Public research governance

Contribution and research-integrity policies have been added for mathematical claims, computational evidence, adversarial review, and corrections.

**Disposition:** PASS.

### F-006 — Citation and licensing surface

A CITATION.cff, MIT license, and external-source notice have been added.

**Disposition:** PASS, with the limitation that external material remains governed by its own terms.

## Known limitation

The GitHub repository is public, but its configured default branch is still Hello-worled; the active research branch is main. This audit does not claim that the GitHub default branch has been changed.

## Release classification

The correct public description is:

> An open, reproducible research program investigating the Riemann Hypothesis through analytical, positivity, spectral, and computational approaches.

It is not:

> A proof of the Riemann Hypothesis.

## Final audit rule

No future commit, experiment, issue, or release may change the public status to a proof claim unless the complete mathematical argument has been independently checked and every load-bearing dependency is closed.

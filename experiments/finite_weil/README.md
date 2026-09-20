# Finite Weil Experiment Track

## Objective

Build a reproducible numerical layer for finite Weil-type quadratic forms.

## Required outputs

For each cutoff configuration record:

- prime cutoff c;
- Galerkin/band dimension N;
- arithmetic precision;
- matrix construction method;
- symmetry sector;
- eigenvalue spectrum;
- smallest positive/negative eigenvalues;
- conditioning diagnostics;
- independent recomputation result.

## Interpretation

A positive finite matrix is evidence about the finite object only.

A negative finite eigenvalue is evidence about the finite approximation only unless an explicit tail theorem transfers it to the cutoff-free form.

A near-zero eigenvalue is especially dangerous: numerical sign is not reliable without rigorous error control.

## Planned adversarial tests

1. precision escalation;
2. basis-size escalation;
3. independent matrix construction;
4. symmetry-sector comparison;
5. interval/ball arithmetic where practical;
6. comparison against exact finite identities;
7. explicit tail-budget accounting.

## No-RH rule

The experiment must not import the known Riemann zeros as a fitting target when testing whether a construction itself establishes positivity.

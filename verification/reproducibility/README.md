# Reproducibility Suite

## Purpose

This directory defines the reproducibility standard for computational claims in the Riemann Research Program.

The target is not merely "the code runs". A reproducible result must expose the mathematical input, parameterization, numerical method, precision, and certification boundary.

## Required record

Every numerical experiment intended for independent reproduction should record:

- commit SHA;
- source files used;
- mathematical parameter values;
- cutoff parameters (for example $c$, $N$, and any frequency/archimedean cutoff);
- matrix dimension and symmetry sector;
- arithmetic precision;
- software/runtime versions;
- deterministic seed, where applicable;
- construction formula;
- eigenvalue/inertia or other certificate;
- conditioning/error budget;
- independent recomputation method;
- exact interpretation of the result;
- limitations and non-inferences.

## Independent reproduction

A strong reproduction should use a second implementation or an independently derived calculation whenever practical.

A second implementation is not required to produce identical floating-point representations. It must independently validate the mathematical quantity and the claimed certification boundary.

## Environment pinning

The project may add Docker/SageMath/Julia environments where they materially improve reproducibility. Such packaging is infrastructure, not a mathematical proof requirement.

No container image or software version can elevate a numerical result from NUMERICALLY_SUPPORTED to PROVED.

## Required conclusion format

Each experiment should end with an explicit status:

- VERIFIED — independently checked within its stated computational scope;
- NUMERICALLY_SUPPORTED — computational evidence without a theorem covering the global claim;
- REFUTED — a claimed statement fails under a valid counterexample;
- BLOCKED — the computation cannot certify the requested claim.

Never infer RH from a finite computational certificate.

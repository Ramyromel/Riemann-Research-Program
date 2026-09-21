# Research Log — Fixed-Support Positivity Closure — 2026-09-21

## Result

A previously informal logical step in the finite-to-global program has now been written as an explicit derived theorem:

**finite admissible nonnegative values + convergence to the target Weil form ⇒ target Weil positivity.**

The proof uses only closedness of the nonnegative half-line. No uniform positive spectral gap is required.

## Exact theorem

For an admissible core \(D_0\), if for every \(f\in D_0\) there are finite admissible \(f_n\) with cutoff-free finite values \(Q_n(f_n)\) such that

\[
Q_n(f_n)\ge0,\qquad Q_n(f_n)-Q(f_n)\to0,\qquad Q(f_n)\to Q(f),
\]

then \(Q(f)\ge0\).

If \(D_0\) is dense in the full Weil domain and \(Q\) is continuous in the chosen topology, positivity extends to the full domain.

## What this closes

This closes the **logical limit/closure substep** once the concrete approximation and finite-positivity hypotheses are established.

It removes an unnecessary requirement for a positive spectral margin. The limiting value may be exactly zero.

## What it does not close

The load-bearing mathematical problems remain:

1. prove positivity of the cutoff-free finite matrices for the required admissible family;
2. prove that the concrete finite Volterra/Galerkin image approximates the required admissible factor core;
3. prove the exact normalization bridge;
4. control constraint corrections;
5. establish odd-sector coverage if required by the chosen Weil formulation;
6. establish the final global domain/density statement.

## External consistency check

Groskin's 2026 finite-dictionary paper establishes exact finite transport and archimedean tail control, but explicitly does not claim global positivity or RH. Independent compact-window work likewise provides selected finite-window certificates rather than a global theorem. Therefore the repository continues to treat finite positivity as the next load-bearing target.

## Status

**DERIVED — VERIFIED LOGIC, CONDITIONAL HYPOTHESES NOT YET ESTABLISHED.**

No RH claim.

# Prime Intersection / Distance Experiment

This experiment tests whether canonical intersection/distance kernels built from prime-power data produce structure beyond the affine transform \(2x-1\).

## Inputs

For prime powers \(q=p^k\le c\):

- \(y_q=2q-1\) — proposed odd-coordinate transform;
- \(x_q=\log q\) — multiplicative/logarithmic coordinate;
- \(w_q=\Lambda(q)/\sqrt q\) — explicit-formula weight.

## Kernels tested

1. **Raw transformed distance:** \(|y_q-y_r|\). This is a control and must reduce exactly to \(2|q-r|\).
2. **Logarithmic distance:** \(|x_q-x_r|\). This tests whether multiplicative geometry adds structure.
3. **Overlap/intersection kernel:** \(\min(x_q,x_r)\). It is a Gram kernel because \(\min(x,y)=\int_0^\infty 1_{t\le x}1_{t\le y}\,dt\).
4. **Exponential distance kernel:** \(e^{-\alpha|x_q-x_r|}\), a canonical positive kernel on the real line.
5. **Weighted forms:** \(w_qw_rK(q,r)\).

These are discovery controls, not claims that any kernel is related to the Riemann explicit formula.

## Acceptance rule

A candidate becomes mathematically interesting only if its structure is exact and it survives a symbolic comparison with the project's finite Prime–Weil kernel. A numerical resemblance to zeta zeros is not an acceptance criterion.

Known zeta zeros are not used by the experiment.

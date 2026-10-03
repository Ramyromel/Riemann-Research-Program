# Low-dimensional interval grid

This experiment extends the local interval certificate over several cutoffs
while keeping the exact pole-neutral reduction at N=2.

Grid:

- c = 10
- c = 20
- c = 30
- c = 50
- c = 100
- N = 2
- T = 1000 resolvent terms
- 60-digit interval arithmetic

The grid is intentionally small and falsifiable. It does not extrapolate a
finite result to arbitrary c or N.

A case is **CERTIFIED** only when the interval lower endpoint after subtracting
the conservative second-order tail upper bound is strictly positive.

A case that fails this condition is **INCONCLUSIVE**, not a counterexample,
because the interval enclosure or tail budget may simply be too wide.

The current N=2 exact scalar reduction does not silently support N>2.
Higher dimensions require an explicit certified treatment of the full
pole-neutral nullspace and a matrix-level positivity enclosure.

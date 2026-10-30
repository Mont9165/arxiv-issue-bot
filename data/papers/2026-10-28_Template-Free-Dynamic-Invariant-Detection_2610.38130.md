# Template-Free Dynamic Invariant Detection

- arXiv ID: `2610.38130v1`
- Authors: Erfan Arvan, Michael D. Ernst, Martin Kellogg
- Published: 2026-10-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.38130v1) | [pdf](https://arxiv.org/pdf/2610.38130v1)

## Abstract

A dynamic invariant detector proposes invariants, such as method pre- and postconditions, and rules out those that do not hold at run time. Traditional detectors propose invariants from a fixed library of templates, which limits their expressiveness. A large language model (LLM) can propose invariants instead of, or in addition to, template-derived ones. With the right prompt and context choices, we found that this idea can both improve the invariants' expressiveness and reduce the cost of inferring the invariants.
  Greater expressiveness brings complications: an LLM-proposed invariant can execute arbitrary code during invariant evaluation, causing side effects or infinite loops. Our novel instrumentation strategies mitigate these problems. We wrap each candidate and evaluate only one invariant per thread at a time, so nested invariant evaluations cannot trigger one another indefinitely. To recover from non-nested hangs, we monitor each run for stalls and retry it under a growing time budget. Because we cannot prove a candidate side-effect-free in advance, we use delta debugging over the invariants evaluated during a failing test to isolate and disable a side-effecting candidate without discarding the rest of the run.
  We compared our implementation, Oca, to the popular template-based Daikon invariant detector on real open-source Java projects. Oca produces more expressive invariants: on average, 28% of its held invariants call a project-specific method, which Daikon's templates cannot express. Its invariants are more often valid, with a false-positive rate of 18% in a manual inspection, vs. 76% for Daikon, and more useful: as properties for property-based testing, they exposed 9 of 25 real bugs, compared with 4 for Daikon. Oca also costs less, using 566 minutes and 27 GB of disk, compared with 2,817 minutes and 827 GB for Daikon.

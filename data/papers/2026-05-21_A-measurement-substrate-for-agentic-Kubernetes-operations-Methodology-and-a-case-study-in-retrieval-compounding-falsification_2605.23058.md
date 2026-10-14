# A measurement substrate for agentic Kubernetes operations: Methodology and a case study in retrieval-compounding falsification

- arXiv ID: `2605.23058v1`
- Authors: Joshua Odmark, Gideon Rubin, Deon van der Vyver
- Published: 2026-05-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.23058v1) | [pdf](https://arxiv.org/pdf/2605.23058v1)

## Abstract

Empirical claims about autonomous Kubernetes operations agents are largely unfalsifiable. Published work reports observational results without controlled comparisons against an agent-disabled baseline, selection bias is endemic, pre-registered decision matrices are absent, and samples are typically too small for the noise level of the underlying scoring system. The cause is the same gap that limits the agents themselves: code agents have a verification substrate that turns "did it work" into a fast, falsifiable, ground-truth signal, and operations has nothing equivalent. We present agent-breakage, a closed-loop measurement framework that injects faults into a target Kubernetes cluster, observes how an autonomous agent responds, scores the response on four axes against ground truth, and accumulates outcome-labeled (state, action, outcome) tuples. The framework distinguishes framework error from reasoning error, supports a true off-condition control via a deterministic-embedder mechanism, and enforces pre-registered decision matrices. We use it as a case study to test whether retrieval over past postmortems compounds an agent's capability. The methodological payload is three confounds the substrate caught during that case study, each of which would have produced a wrong published claim on a less instrumented version of the same work: a pgvector index bug, a +19% selection-bias artifact, and small-sample estimates that overstated effects by roughly 3x. The retrieval result itself is a partial falsification: 1 of 3 dense-corpus scenarios significant at p<0.05, pooled effect +3.9 percentage points, not significant at n=60. A within-scenario corpus-density sweep at 360 runs shows that mechanistic alignment of near-neighbors dominates raw count. The framework is released open source.

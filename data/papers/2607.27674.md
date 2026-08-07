# Can Large Language Models Resolve Real Java Merge Conflicts? An Evaluation with a Calibrated LLM-as-Judge

- arXiv ID: `2607.27674v1`
- Authors: Bowen Shen
- Published: 2026-07-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.27674v1) | [pdf](https://arxiv.org/pdf/2607.27674v1)

## Abstract

Merge conflicts are a recurring cost of collaborative software development, and the traditional structured and semi-structured merge tools that address them frequently abstain: when their heuristics do not apply, they leave the conflict unresolved. Large language models (LLMs) can instead produce a candidate resolution for almost any conflict, but measuring whether those resolutions are actually good at scale is hard, because obtaining human desirability judgments for every model output does not scale. We study both problems together on real Java merge conflicts from ConflictBench. We first build an LLM solver as a generate-validate-retry agent that uses only inference-time signals (conflict markers, a Java parser, and duplicate-declaration checks) and never sees the developer's answer. We then evaluate its resolutions with a two-metric suite: (1) a developer-match LLM-as-judge implemented as a G-Eval metric and, crucially, calibrated against ConflictBench's human labels before use, and (2) a deterministic structural-validity check that uses no LLM. On a meta-evaluation of 292 human-labeled cases, the judge reaches 100% precision (zero false accepts) at 64.6% recall, so every acceptance is trustworthy and every downstream rate is a conservative lower bound. Under this validated judge, LLM solvers match the developer's own resolution on about 55% of true conflicts (conservative floor), and under a coverage-fair comparison the LLMs (55-59%) beat the strongest traditional tool (AutoMerge, 36.7%) by roughly 18-22 points; the edge comes almost entirely from coverage, not raw accuracy, since the tools abstain on 20-90% of conflicts while the LLM under forced resolution abstains on none. Finally, the LLM judge accepted 4 of the 5 resolutions that fail the deterministic structural check, evidence that structural correctness must not be delegated to an LLM.

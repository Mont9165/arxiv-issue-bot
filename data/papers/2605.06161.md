# Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges

- arXiv ID: `2605.06161v1`
- Authors: Shihao Weng, Yang Feng, Xiaofei Xie
- Published: 2026-05-07
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.06161v1) | [pdf](https://arxiv.org/pdf/2605.06161v1)

## Abstract

LLM-as-a-Judge pipelines have become the de facto evaluator for agent safety, yet existing benchmarks treat their verdicts as ground-truth proxies without checking whether the verdicts depend on the agent's behavior or merely on how the evaluation policy happens to be worded. We argue that any trustworthy safety judge must satisfy a basic property we call policy invariance, and we operationalize it as three testable principles: rubric-semantics invariance under certified-equivalent rewrites, rubric-threshold invariance under intentional strict-to-lenient shifts, and ambiguity-aware calibration so that verdict instability concentrates on genuinely ambiguous cases. Instantiating these principles as a stress-test protocol with four agent-class judges on trajectories drawn from ASSEBench and R-Judge, we surface a previously unmeasured failure mode: today's judges respond to meaningful normative shifts and to meaningless structural rewrites with comparable strength, and cannot tell the two apart. Content-preserving policy rewrites flip up to 9.1% of verdicts above baseline jitter, and 18-43% of all observed flips occur on unambiguous cases under such rewrites, so existing safety scores conflate what the agent did with how the evaluator was prompted. Beyond the diagnosis, we contribute the Policy Invariance Score and the Judge Card reporting protocol, which expose an order-of-magnitude spread in judge reliability that is invisible to accuracy-only leaderboards. We release the protocol and code so that future agent-safety benchmarks can audit their own evaluators rather than trust them by default.

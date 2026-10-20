# VerusEval: Evaluating LLM-Generated Verus Specifications Beyond Verifier Acceptance

- arXiv ID: `2610.26464v1`
- Authors: Ding Wang, Chao Jiang, Dugang Liu, Zhiwu Xu, Cheng Wen, Zhong Ming, Yuwei Liu, Xinyi Wan, Lin Huang
- Published: 2026-10-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.26464v1) | [pdf](https://arxiv.org/pdf/2610.26464v1)

## Abstract

Large language models (LLMs) are increasingly used to generate Verus contracts for Rust programs together with the proofs that establish them. Yet verifier acceptance, the common measure of success, shows only that the implementation satisfies the generated contract, so it leaves open whether the contract captures the intended behavior. Assessing specification generation therefore requires an evaluation methodology, not a single metric. We present VerusEval, a framework that evaluates generated contracts along six dimensions, including Verus-native checks for semantic triviality, validated input-output (I/O) suites, and contract equivalence, and that relates them so that the strength and blind spots of each become measurable. Evaluating 13,716 artifacts from four workflows, five LLMs, and two prompting settings on 762 tasks, we find that acceptance overstates quality: only 42.3\% of the accepted artifacts complete all three semantic checks without a flag, and across workflows and models, higher acceptance does not consistently come with more correct contracts. I/O evaluation rejects 23.6\% of the accepted artifacts, yet only 63.2\% of those that pass it are proved equivalent. Of the accepted artifacts flagged by contract comparison, 84.1\% have a rejected completeness obligation, and the direction of a failure prioritizes inspection of the generated contract or the reference; it does not by itself establish which artifact is defective. Screening and review further identify 36 candidate defects among 61 selected reference contracts, and repairing one of them makes 10 of its 11 failing artifacts equivalent. Based on these findings, we derive four actionable lessons for evaluation, generation, and benchmark maintenance.

# Adversarial Pragmatics for AI Safety Evaluation: A Benchmark for Instruction Conflict, Embedded Commands, and Policy Ambiguity

- arXiv ID: `2607.01153v1`
- Authors: Brett Reynolds
- Published: 2026-07-01
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01153v1) | [pdf](https://arxiv.org/pdf/2607.01153v1)

## Abstract

Safety evaluations for language models increasingly depend on judgments about ambiguous natural-language behaviour: whether a model has followed an instruction, refused appropriately, complied with a policy, resisted an embedded command, or misreported progress in an agentic task. Existing benchmarks often compress these distinctions into pass/fail labels, obscuring whether failures arise from capability limits, policy ambiguity, instruction conflict, scaffold failure, or unstable evaluator judgments.
  This paper introduces adversarial pragmatics as a benchmark and annotation protocol for evaluating model behaviour under instruction conflict, embedded commands, quotation, scope ambiguity, deixis, indirect speech acts, and multi-turn agent transcripts. The contribution is empirical and methodological: a linguistically controlled taxonomy, an 18-item seed benchmark with validator-enforced metadata, a 54-row local seed pilot, an expert-evaluation protocol distinguishing task success, policy compliance, safety risk, refusal outcome, and evaluator confidence, and metrics for judge validity, diagnostic ambiguity, and taxonomy drift. The framework turns linguistic judgment methodology into a practical tool for validating safety evals, LLM judges, gold-set construction, prompt-injection tests, and safety documentation.

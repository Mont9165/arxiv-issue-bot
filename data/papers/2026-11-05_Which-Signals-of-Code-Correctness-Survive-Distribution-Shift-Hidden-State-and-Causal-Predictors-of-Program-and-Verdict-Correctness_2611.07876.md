# Which Signals of Code Correctness Survive Distribution Shift? Hidden-State and Causal Predictors of Program and Verdict Correctness

- arXiv ID: `2611.07876v1`
- Authors: Viola Campos, Thomas Klassert, Adrian Ulges
- Published: 2026-11-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2611.07876v1) | [pdf](https://arxiv.org/pdf/2611.07876v1)

## Abstract

Large language models increasingly judge code, yet without external feedback such judgments are unreliable, and verifying them by executing tests or by extended reasoning is costly. Instead, execution-free correctness predictors use signals from the model's output probabilities, sampled solutions, or hidden states to identify judgments that warrant further verification. However, these predictors may degrade under distribution shifts when generalizing across projects and languages.
  We compare six execution-free predictors from four families on Qwen3-Coder-30B and gpt-oss-20b under benchmark shift between LiveCodeBench and BigCodeBench and language shift across Python, C++ and Java. We evaluate two targets: whether the model's own verdict on a program can be trusted, and whether the program itself is correct. Besides established approaches, we adapt two novel causal localization methods to code, which have been shown to be more robust out-of-distribution on natural language tasks. For verdict correctness, causal localization improves robustness to language shift. For Qwen3-Coder a probe on the causally localized subspace stays 0.09 AUROC ahead of output confidence under language shift (0.11 in distribution), significantly outperforming the best non-causal predictor by 0.04 AUROC on average. This advantage, however, does not generalize consistently to gpt-oss or to benchmark shift. For program correctness, predictors transfer more successfully between benchmarks, largely by identifying problems on which the model tends to fail. However, their ability to rank candidates within the same problem is limited.

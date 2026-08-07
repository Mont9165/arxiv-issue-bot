# Do Code Language Models Use Tests? A Behavioral and Representational Study of Test-Driven Code Generation

- arXiv ID: `2607.26244v1`
- Authors: Yunhao Liang, Chengguang Gan, Ruixuan Ying, Hanjun Wei, Zhe Cui, Shiwen Ni
- Published: 2026-07-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.26244v1) | [pdf](https://arxiv.org/pdf/2607.26244v1)

## Abstract

Public tests are widely used to guide large language model code generation, but whether models treat them as executable specifications or merely as extra prompt context remains unclear. We study test-driven code generation on HumanEval+, MBPP+, and recent LiveCodeBench tasks using Qwen2.5-Coder-7B and Qwen3.6-27B. We compare natural-language-only prompts with relevant visible tests, shuffled outputs, irrelevant tests, assertion-only tests, and stronger-model-generated synthetic tests. Evaluation combines hidden or private test pass rates with task-level behavior flips, linear probes, and layer-wise hidden-state shifts. Visible tests substantially improve Qwen2.5 performance on MBPP+ but have little or unstable effect on HumanEval+ and LiveCodeBench. For Qwen3.6 on LiveCodeBench, the natural-language-only pass rate rises from 13.1% to 39.4%, yet relevant original tests add only 2.9 percentage points (p = .458), and synthetic high5 tests add 1.7 points over their matched baseline (p = .701). More tests produce larger representation shifts, but accuracy gains quickly saturate or disappear; assertion-only and irrelevant-test prompts can strongly alter hidden states without improving correctness. After controlling for prompt length, task-level shifts are associated with both beneficial and harmful flips, with a substantially stronger association for harms. These results show that tests influence code models through both semantic guidance and prompt-context perturbation, and that representational change alone does not demonstrate effective test utilization.

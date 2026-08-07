# Beyond Pass Rate: A Multilingual, Execution-Grounded Evaluation of Open Code LLMs

- arXiv ID: `2606.08840v1`
- Authors: Sayed Erfan Arefin
- Published: 2026-06-07
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.08840v1) | [pdf](https://arxiv.org/pdf/2606.08840v1)

## Abstract

Code generation models are typically compared using compact execution benchmarks and aggregate pass rates, but such summaries obscure how performance varies across programming languages, problem families, and failure modes. We present a large-scale, execution-grounded evaluation of 9 openly accessible LLMs specialized for coding on 2,707 free LeetCode problems across 12 programming languages. Our corpus contains 325,343 problem-model-language jobs, each linked to prompt metadata, extracted code, LeetCode execution outcomes, and static-analysis signals. The results show that current open models remain far from the human acceptance reference: the best model, Yi-Coder-9B-Chat, reaches 23.64% mean correctness, compared with a 57.2% human acceptance baseline. Rankings are also slice-dependent: Qwen2.5-Coder-14B-Instruct is strongest on hard problems and distinct-problem coverage, while Gemma-2-27B-IT achieves the highest all-language lint pass rate. Failure analysis shows that compile errors account for 63.25% of non-accepted best submissions, indicating that many failures occur before semantic correctness can be tested. Static quality further diverges from functional correctness. Together, these findings show that multilingual, artifact-preserving evaluation reveals tradeoffs hidden by single-language or single-metric leaderboards.

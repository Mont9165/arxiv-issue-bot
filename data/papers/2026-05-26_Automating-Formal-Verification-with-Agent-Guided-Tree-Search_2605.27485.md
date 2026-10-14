# Automating Formal Verification with Agent-Guided Tree Search

- arXiv ID: `2605.27485v1`
- Authors: Leo Yao
- Published: 2026-05-26
- Primary category: `cs.LO`
- Categories: `cs.LO`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.27485v1) | [pdf](https://arxiv.org/pdf/2605.27485v1)

## Abstract

Formal verification offers a path to provably correct software, but writing verified code remains expensive enough that the technique is rarely used in production. Recent large language models can accelerate this work, and recent benchmarks measure their ability to translate specifications into code and machine-checked proofs of correctness. This thesis evaluates the state of such LLM-driven verified-code generation ("vericoding") in Lean and develops search-based methods for improving verification performance. We first reproduce a subset of the vericoding-benchmark Lean leaderboard on a current cross-vendor model pool, finding that non-reasoning performance remains roughly steady on US closed-source models while open-weight models have slightly improved. We update the iterative methodology of vericoding-benchmark with an agentic loop equipped with mathlib search, finding that model performance greatly improves and scales with agent budget. GPT-5.4 nearly saturates the benchmark at 95.0% on 423 specs with $K=50$ LLM calls. We then design two agent-directed tree-search formulations: a state-based orchestrator that branches on partial-proof states, and a context-based orchestrator that branches on full subagent contexts. Compared against the agent baseline, the context-based design solves a wider range of intermediate-difficulty specs at lower token cost, while the agent baseline retains an advantage on the hardest specs, where uninterrupted iteration matters most. We conclude that search structure has selective advantages over a strong agent baseline, and that more challenging benchmarks drawn from modern code are important to measure and drive further progress in automated formal verification.
  Code available upon request by contacting the author at leoy@mit.edu.

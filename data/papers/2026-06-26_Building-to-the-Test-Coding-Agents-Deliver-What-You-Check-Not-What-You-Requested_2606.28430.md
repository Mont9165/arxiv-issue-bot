# Building to the Test: Coding Agents Deliver What You Check, Not What You Requested

- arXiv ID: `2606.28430v1`
- Authors: Yanuo Ma, Ben Kereopa-Yorke, Ben Schultz
- Published: 2026-06-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.28430v1) | [pdf](https://arxiv.org/pdf/2606.28430v1)

## Abstract

Benchmarks are widely used to evaluate task completion by Large Language Models (LLMs), but this approach has accumulated construction-validity problems, and a passing score may not show whether the requested task was delivered. We study both problems. In a controlled code-as-spec setup, two production Copilot CLI agents (claude-opus-4.7, gpt-5.5) re-implement a React Fluent-UI data table in Angular as a reusable library under a hidden 222-test Playwright oracle across 18 runs and three oracle-availability conditions. Alongside the score, we run a mechanical library audit and check each verdict with a no-op ablation. Without the oracle, the library is present but unfinished, revealed by scores. With the oracle in the loop, the score reaches near-perfect, but from a demo holding the tested behavior directly, the library left dead or absent. We call this building to the test; the broader disposition behind both we call validation self-awareness. The agent does not, on its own, validate what it ships as a user would. Prevalence remains an open question across other agents, signals, and model families. Beyond benchmark scores, dispositions like validation self-awareness merit research attention.

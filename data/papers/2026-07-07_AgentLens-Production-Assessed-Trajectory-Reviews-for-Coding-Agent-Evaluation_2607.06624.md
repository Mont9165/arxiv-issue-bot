# AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation

- arXiv ID: `2607.06624v1`
- Authors: Andrey Podivilov, Vadim Lomshakov, Sergey Savin, Matvei Startsev, Roman Pozharskiy, Maksim Parshin, Sergey Nikolenko
- Published: 2026-07-07
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.06624v1) | [pdf](https://arxiv.org/pdf/2607.06624v1)

## Abstract

We present AgentLens, a production-assessed benchmark for interactive code agents. Most code-agent benchmarks reduce a run to a single bit -- did the task pass? -- but the people who actually use these agents experience the entire trajectory: how the agent follows instructions, uses its tools, verifies its own work, recovers from mistakes, and talks to them along the way. AgentLens evaluates that whole trajectory. It pairs formal verification, where an objective check exists, with LLM-written trajectory reviews and side-by-side comparisons, so that each run yields a readable explanation of why the score is what it is. This makes AgentLens useful for more than ranking models: we use it to diagnose model behavior, compare successive versions of our own agent, and catch product regressions in a nightly evaluation pipeline. We release the benchmark as open source at https://github.com/agent-lens/agent-lens-bench.

# Meta-Reflective Evolution Effectively Improves Production AI Systems

- arXiv ID: `2610.12794v1`
- Authors: Seung Won Wilson Yoo, Chang Zeng, Aditi Somayajula, Sahithi Ankireddy, Rohan Kosalge, Avishree Khare, John Mitchell, Aditya G. Parameswaran, Rajhans Samdani, Anupam Datta
- Published: 2026-10-08
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.12794v1) | [pdf](https://arxiv.org/pdf/2610.12794v1)

## Abstract

Large Language Model (LLM)-guided evolutionary optimization has successfully improved prompts, programs, and even entire AI systems. Most optimization methods select a candidate from the search frontier, then mutate it in one LLM pass based only on its failures. This focus on the frontier can stall on production AI systems, where isolated failures reveal little about complex, hidden interactions. We introduce CoCoEvolve (Cortex Code Evolve), an evolutionary optimizer built around what we call meta-reflection, wherein an agentic mutator (Cortex Code) selectively retrieves evidence from the entire evolutionary history and probes the live system before verifying and proposing mutations. We apply CoCoEvolve to optimize three classes of production AI systems: data agents, LLM-powered data pipelines, and data engineering workflows. On DABStep, CoCoEvolve tops the public leaderboard, reaching 92.8% held-out hard accuracy compared to 78.4% for Meta-Harness and 30.4% for GEPA under matched conditions. Across six LLM data pipeline workloads, it outperforms every evaluated baseline. On data-eng-bench, CoCoEvolve lifts test-set solve rate from 59.1% to 77.4%, past the best baseline of 73.6%. It also has 11 percentage points higher accuracy than GEPA on HotpotQA while remaining competitive with specialized optimizers on established mathematical and systems benchmarks. Matched ablations confirm that each component of CoCoEvolve contributes to these gains, demonstrating the value of meta-reflection for optimizing production AI systems.

# When Code Becomes an LLM Call: An Empirical Study of Call-Site Contracts in Agentic Systems

- arXiv ID: `2610.24545v1`
- Authors: Shihao Weng, Longtian Wang, Yang Feng, Mingfei Cheng, Jia Liu, Chao Shen, He Ye, Federica Sarro, Xiaofei Xie
- Published: 2026-10-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2610.24545v1) | [pdf](https://arxiv.org/pdf/2610.24545v1)

## Abstract

Software quality has long rested on specifications that state what code must do, and on testing and verification that check that the code does it. Agentic systems change this foundation: they replace parts of their logic, such as choosing the next tool, judging whether an action is allowed, or writing code to run, with calls to a large language model (LLM). The program still relies on what this logic must guarantee, but the model's behavior is not fixed by code, varies across runs, and can be steered by its input. The guarantee must therefore come from the program around each LLM call site, as a contract of pre-conditions, prompt constraints, and post-conditions. We present an empirical study of these contracts in 496 LLM call sites of 40 popular open-source agentic systems (13.4 MLOC, four languages). Using a multi-agent pipeline validated by 17,428 human judgments, we trace where every model output flows, derive an expected contract for each call site without access to its code, and compare it with the contract that the code implements. We find that 48% of LLM outputs reach control flow or execution, and 73% of these never reach a person. Programs enforce 78% of their constraints in code, but in the prompt, 67% of the constraints are only requested from the model. Although 82% of call sites are checked before and after the call, 63% of the expected constraints are unmet and only 5.3% of call sites satisfy their whole contract; ten recurring patterns explain 99% of the gaps. 38 mechanisms behind these gaps trigger at runtime, and a small code fix that enforces the expected constraint stops all 38. Our results show that the presence of checks says little about their adequacy, and we derive implications for agent developers, framework maintainers, and researchers.

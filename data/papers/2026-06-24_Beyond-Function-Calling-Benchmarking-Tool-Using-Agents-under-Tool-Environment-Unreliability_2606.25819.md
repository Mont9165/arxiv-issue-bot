# Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability

- arXiv ID: `2606.25819v1`
- Authors: Yang Tian, Zhengpeng Shi, Bo Zhao
- Published: 2026-06-24
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.25819v1) | [pdf](https://arxiv.org/pdf/2606.25819v1)

## Abstract

Large language models are increasingly deployed as agents that solve tasks by interacting with external tool environments. Although recent tool-use benchmarks increasingly cover complex task settings, they still largely assume clean, stable, and trustworthy tool environments, leaving tool-environment unreliability insufficiently examined. We introduce ToolBench-X, a benchmark for evaluating agents under recoverable reliability hazards. ToolBench-X contains executable multi-step tasks across diverse domains and sequential, parallel, and mixed workflows, each paired with deterministic tools and a canonical final answer for automatic evaluation. Starting from clean tool environments, ToolBench-X injects five structured hazard types: Specification Drift, Invocation Error, Execution Failure, Output Drift, and Cross-source Conflict. Crucially, each injected instance remains solvable through at least one valid recovery path, such as retrying, fallback, verification, or cross-checking. Experiments reveal a substantial reliability gap: agents that perform well with reliable tools often fail under recoverable hazards. Further analysis shows that failures are driven less by tool-use volume or inference budget than by limited hazard diagnosis and ineffective recovery. Targeted recovery hints recover many failed tasks, while test-time scaling yields more limited gains. These results suggest that tool-use evaluation should move beyond function-call accuracy toward task completion under unreliable tool environments. The code and data is available at https://github.com/Foreverskyou/ToolBench-X.

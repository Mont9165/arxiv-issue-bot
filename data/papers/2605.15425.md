# Runtime-Structured Task Decomposition for Agentic Coding Systems

- arXiv ID: `2605.15425v1`
- Authors: Shubhi Asthana, Bing Zhang, Chad DeLuca, Hima Patel, Ruchi Mahindru
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.15425v1) | [pdf](https://arxiv.org/pdf/2605.15425v1)

## Abstract

Agentic coding systems increasingly use large language models (LLMs) for software engineering tasks such as debugging, root cause analysis, and code review. However, many existing systems encode task logic, execution flow, and output generation inside monolithic prompts. This design creates brittle behavior, limited debuggability, and high retry costs because failures often require rerunning the full workflow.
  We present runtime-structured task decomposition, an architectural approach in which task partitioning and execution flow are managed through executable control logic rather than prompt structure alone. LLMs are used only for focused judgment tasks, and outputs are validated against predefined schemas before downstream execution.
  We evaluate this approach on two software engineering workloads using three configurations: monolithic execution, static decomposition with fixed subtasks and no runtime branching, and runtime-structured decomposition. Each configuration was evaluated across 10 runs.
  Our results show that decomposition alone does not necessarily reduce retry cost. In the Kubernetes root cause analysis workload, the static decomposition baseline produced a retry cost of 1,632 +/- 145 tokens versus 904 +/- 17 tokens for the monolithic baseline because failures forced reruns of downstream subtasks. A similar pattern appeared in the multi-file debugging workload, where the static baseline consumed 933 tokens compared to 703 tokens for the monolithic system.
  The runtime-structured approach reran only failed subtasks, reducing retry costs to 436 +/- 132 tokens for root cause analysis and 460 tokens for debugging. Overall, the approach achieved up to 51.7% lower retry cost than monolithic systems and 73.2% lower retry cost than static decomposition baselines, improving efficiency, debuggability, and operational reliability in agentic coding systems.

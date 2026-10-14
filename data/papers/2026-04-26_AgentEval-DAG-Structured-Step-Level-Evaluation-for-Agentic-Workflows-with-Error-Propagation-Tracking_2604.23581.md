# AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking

- arXiv ID: `2604.23581v1`
- Authors: Dongxin Guo, Jikun Wu, Siu Ming Yiu
- Published: 2026-04-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2604.23581v1) | [pdf](https://arxiv.org/pdf/2604.23581v1)

## Abstract

Agentic systems that chain reasoning, tool use, and synthesis into multi-step workflows are entering production, yet prevailing evaluation practices like end-to-end outcome checks and ad-hoc trace inspection systematically mask the intermediate failures that dominate real-world error budgets. We present AgentEval, a framework that formalizes agent executions as evaluation directed acyclic graphs (DAGs), where each node carries typed quality metrics assessed by a calibrated LLM judge (GPT-4o), classified through a hierarchical failure taxonomy (3 levels, 21 subcategories), and linked to upstream dependencies for automated root cause attribution. An ablation study isolates the impact of DAG-based dependency modeling: it alone contributes +22 percentage points to failure detection recall and +34 pp to root cause accuracy over flat step-level evaluation with identical judges and rubrics.
  Across three production workflows (450 test cases, two agent model families, predominantly sequential architectures with a 12% non-DAG trace rate), AgentEval achieves 2.17x higher failure detection recall than end-to-end evaluation (0.89 vs. 0.41), Cohen's kappa = 0.84 agreement with human experts, and 72% root cause accuracy against an 81% human ceiling. Cross-system evaluation on tau-bench and SWE-bench traces confirms transferability (failure detection recall >= 0.78) without taxonomy or rubric modification. A 4-month pilot with 18 engineers detected 23 pre-release regressions through CI/CD-integrated regression testing, reducing median root-cause identification time from 4.2 hours to 22 minutes and driving measurable failure rate reductions in two workflows.

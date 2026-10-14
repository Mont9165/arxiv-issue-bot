# Reliable LLM-Generated Programs for High-Energy Physics Experiments through Graph-Grounded Software Knowledge

- arXiv ID: `2609.01095v1`
- Authors: Yue Sun, Tong Liu, Yipu Liao, Jingde Chen, Ke Li
- Published: 2026-09-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `hep-ex`
- Links: [abs](http://arxiv.org/abs/2609.01095v1) | [pdf](https://arxiv.org/pdf/2609.01095v1)

## Abstract

Extracting physics information from modern particle-physics experiments requires multistage analyses implemented on top of large and highly interconnected software ecosystems. General-purpose large language models (LLMs) often produce unreliable programs for such tasks because a user request alone rarely specifies the required APIs, dependencies, and usage conventions. We organize these software relations before generation and retrieve task-relevant knowledge at inference time. Using the open-source ROOT framework as a representative and reproducible testbed, we evaluate a complete grounding system that combines hybrid retrieval over a heterogeneous software knowledge graph, skill-selected workflow examples, and execution-guided repair. On a benchmark of 275 ROOT tasks, grounding improves first-attempt execution from 58.5% to 76.0% under Claude Code orchestration and from 51.3% to 64.0% under standalone orchestration. Final success increases from 90.5% to 96.0% and from 78.9% to 90.9%, respectively, while the average generation cost per successful task increases by only 1.3% and 3.2%. The gains persist under a strong coding agent, indicating that explicit software knowledge remains valuable even when agentic scaffolding is already in place. Because the method captures software relations common to large codebases rather than facts specific to ROOT or a particular model, it should transfer to other experiment frameworks and proprietary software, especially where documentation is sparse or internal dependencies are complex.

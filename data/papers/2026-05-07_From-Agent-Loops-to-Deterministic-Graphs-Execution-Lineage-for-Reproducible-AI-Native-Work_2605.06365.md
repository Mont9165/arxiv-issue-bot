# From Agent Loops to Deterministic Graphs: Execution Lineage for Reproducible AI-Native Work

- arXiv ID: `2605.06365v1`
- Authors: Josh Rosen, Seth Rosen
- Published: 2026-05-07
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.06365v1) | [pdf](https://arxiv.org/pdf/2605.06365v1)

## Abstract

Large language model systems are increasingly deployed as agentic workflows that interleave reasoning, tool use, memory, and iterative refinement. These systems are effective at producing answers, but they often rely on implicit conversational state, making it difficult to preserve stable work products, isolate irrelevant updates, or propagate changes through intermediate artifacts.
  We introduce execution lineage: an execution model in which AI-native work is represented as a directed acyclic graph (DAG) of artifact-producing computations with explicit dependencies, stable intermediate boundaries, and identity-based replay. The goal is not to make the model a better one-shot writer, but to make evolving AI-generated work maintainable under change.
  We compare execution-lineage replay against loop-centric update baselines on two controlled policy-memo update tasks. In an unrelated-branch update, DAG replay preserved the final memo exactly in all runs, with zero churn and zero unrelated-branch contamination, while loop baselines regenerated the memo and frequently imported unrelated context. In an intermediate-artifact edit, all systems reflected the new constraint in the final memo, but only DAG replay achieved perfect upstream preservation, downstream propagation, unaffected-artifact preservation, and cross-artifact consistency.
  These results show that final answer quality and maintained-state quality are distinct. Strong loop baselines can remain competitive at producing polished final outputs when the task is a bounded synthesis/update problem and all current sources fit in context, but immediate task success can mask partial state inconsistency that may compound over future revisions. Execution lineage provides stronger guarantees about what should change, what should remain stable, and how work evolves across revisions.

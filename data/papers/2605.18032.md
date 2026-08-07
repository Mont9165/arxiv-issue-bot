# PROTEA: Offline Evaluation and Iterative Refinement for Multi-Agent LLM Workflows

- arXiv ID: `2605.18032v1`
- Authors: Kazuki Kawamura, Satoshi Waki, Kei Tateno
- Published: 2026-05-18
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.HC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.18032v1) | [pdf](https://arxiv.org/pdf/2605.18032v1)

## Abstract

Multi-agent LLM workflows -- systems composed of multiple role-specific LLM calls -- often outperform single-prompt baselines, but they remain difficult to debug and refine. Failures can originate from subtle errors in intermediate outputs that propagate to downstream nodes, requiring developers to inspect long traces and infer which agent to modify. We present PROTEA, a unified interface for offline, test-driven improvement of multi-agent workflows. PROTEA executes a workflow, scores intermediate node outputs with configurable rubrics, and overlays per-node states and rationales on the workflow graph to localize likely bottlenecks. To support complex systems where final-answer references are the primary supervision, PROTEA performs backward node evaluation: it generates candidate node-level expectations from final-answer references and graph context, then compares them with observed node outputs. For selected nodes, PROTEA presents targeted prompt revisions as editable before/after comparisons, then automatically reruns and re-evaluates the workflow to show output changes and score trajectories within the same interface. In two production-adjacent workflows, PROTEA improved document-inspection accuracy from 64.3% to 83.9% and recommendation Hit@5 from 0.30 to 0.38. In a formative study with six experienced LLM developers, participants valued graph-level localization, per-node rationales, and editable before/after prompt revisions.

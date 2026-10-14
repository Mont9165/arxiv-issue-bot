# SkillOps: Managing LLM Agent Skill Libraries as Self-Maintaining Software Ecosystems

- arXiv ID: `2605.13716v1`
- Authors: Hongji Pu, Xinyuan Song, Liang Zhao
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2605.13716v1) | [pdf](https://arxiv.org/pdf/2605.13716v1)

## Abstract

Large language model agents increasingly rely on skill libraries for multi-step tasks, yet these libraries can accumulate persistent defects as skills are added, reused, patched, and linked to changing dependencies. We call this failure mode skill technical debt: library-level defects that may not break a single skill locally but can harm future retrieval, composition, and execution. Existing skill-based agents mainly focus on task-time retrieval, planning, and repair, while library-time maintenance remains underexplored. We propose SkillOps, a method-agnostic plug-in framework for maintaining skill libraries. SkillOps represents each skill as a typed Skill Contract (P, O, A, V, F), organizes skills with a Hierarchical Skill Ecosystem Graph, and diagnoses library health across utility, compatibility, risk, and validation dimensions. Given a raw skill library, SkillOps produces a maintained library that can be used by existing retrieval or planning agents without changing their internal code. On ALFWorld, SkillOps achieves 79.5 percent task success as a standalone agent, outperforming the strongest baseline by 8.8 percentage points with no additional task-time large language model calls. As a plug-in layer, it improves retrieval-heavy baselines by 0.68 to 2.90 percentage points. The current rule-based maintenance implementation uses nearly zero library-time large language model calls or tokens, showing that skill-library maintenance can be added as a low-overhead architectural layer.

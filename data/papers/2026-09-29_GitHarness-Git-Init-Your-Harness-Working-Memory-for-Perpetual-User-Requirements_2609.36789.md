# GitHarness: Git Init Your Harness Working Memory for Perpetual User Requirements

- arXiv ID: `2609.36789v1`
- Authors: Zhibang Yang, Xinke Jiang, Yuxuan Liu, Mingyu Zhang, Zhixin Zhang, Zhengxing Song, Yue Fang, Guohong Qiu, Ruiqing Li, Xu Chu, Junfeng Zhao, Yasha Wang
- Published: 2026-09-29
- Primary category: `cs.MA`
- Categories: `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.36789v1) | [pdf](https://arxiv.org/pdf/2609.36789v1)

## Abstract

LLM-based agents increasingly collaborate with users on long-horizon tasks, accumulating evidence, code, and drafts through extensive search, reasoning, and execution. As users inspect these results, they may supply missing information requirement completion, introduce new requirements requirement elicitation, or revise existing ones requirement shift. These changes often affect only part of the accumulated work, yet agents may carry forward obsolete information or turn local revisions into global rewrites. Existing approaches clarify current intent without determining how prior work should change, or reuse execution histories under a fixed objective. We address this gap by formulating dynamic-requirement collaboration as joint requirement tracking and local update. We introduce GitHarness, a pluggable Git-style framework that organizes requirement states and their corresponding harness work states into a branchable version history. A trainable Git Agent resolves requirement changes and selects a semantically compatible historical state. A unified version interface then restores that state and creates a new branch, enabling the underlying harness to exclude obsolete information, inherit compatible work, and focus execution on affected parts. The Git Agent is trained through interface-level black-box reinforcement learning, with downstream harnesses and task-execution models kept fixed. We also construct MTAgentBench, a verifier-preserving benchmark covering mathematical reasoning, text-to-SQL, agentic search, software engineering, and research synthesis. Experiments demonstrate strong task performance alongside effective requirement tracking, preservation of valid work, and efficient execution.

# AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation

- arXiv ID: `2605.12925v1`
- Authors: Priyam Sahoo, Gaurav Mittal, Xiaomin Li, Shengjie Ma, Benjamin Steenhoek, Pingping Lin, Yu Hu
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.12925v1) | [pdf](https://arxiv.org/pdf/2605.12925v1)

## Abstract

Evaluation of software engineering (SWE) agents is dominated by a binary signal: whether the final patch passes the tests. This outcome-only view treats a principled solution and a chaotic trial-and-error process as equivalent. We show that this equivalence is empirically false. We evaluate 2,614 OpenHands trajectories from eight model backends on 60 SWE-bench Verified tasks. Of these, 47 have enough passing trajectories to construct task-level process references, yielding a 1,815-trajectory evaluation subset. Among passing trajectories in this subset, 10.7% exhibit behavior we call a Lucky Pass: regression cycles, blind retries, missing verification, or temporally disordered exploration, implementation, and verification.
  We introduce AgentLens, a framework for process-level assessment of SWE-agent trajectories, and release AgentLens-Bench, a dataset of 1,815 trajectories annotated with quality scores, waste signals, divergence points, and 47 task-level Prefix Tree Acceptor (PTA) references. AgentLens builds PTA references by merging multiple passing solutions for the same task, and uses a context-sensitive intent labeler to assign actions to Exploration, Implementation, Verification, or Orchestration based on trajectory history rather than tool identity alone.
  On AgentLens-Bench, the quality score separates passing trajectories into Lucky, Solid, and Ideal tiers and further decomposes Lucky Passes into five recurring mechanisms. Across the eight model backends, Lucky rates range from 0.5% to 23.2%, and some models move by as many as five rank positions when ranked by quality score instead of pass rate. We release the anonymized project repository, including the AgentLens-Bench dataset and AgentLens SDK, at https://github.com/microsoft/code-agent-state-trajectories/.

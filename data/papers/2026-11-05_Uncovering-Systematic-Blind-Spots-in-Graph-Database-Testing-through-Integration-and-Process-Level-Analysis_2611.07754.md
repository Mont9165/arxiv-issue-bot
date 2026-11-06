# Uncovering Systematic Blind Spots in Graph Database Testing through Integration and Process-Level Analysis

- arXiv ID: `2611.07754v1`
- Authors: Tinghan Li, Aoyang Fang, Longbin Lai, Zifan Xie, Hongbo Zhao, Yu Shao, Ying Zhang, Pinjia He
- Published: 2026-11-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.07754v1) | [pdf](https://arxiv.org/pdf/2611.07754v1)

## Abstract

Graph databases are becoming foundational infrastructure for connected data, and a growing body of automated testing techniques has uncovered many bugs across mature graph database systems. Each technique checks a different aspect of correctness and exposes a different class of defect. Combining them is the natural next step, but each technique is judged by the real bugs it finds, not by useless reports or tests that can never fail, and that is what decides whether a developer can afford to fix the problems. To identify the remaining gaps, we integrated test capabilities from 8 testing methods and conducted an empirical study of their behavior, during which we found two blind spots. First, 12 hours of testing produce thousands of bug reports, far more than the number of genuine defects a mature database is likely to contain. Most reports are false positives caused by dialect or pattern-matching differences, and many of the remaining reports are duplicates. Second, analysis of process-level data reveals that many equivalence-based metamorphic test cases lose their ability to detect defects because of the optimization mechanism. Based on these findings, we summarize and realize these guidelines in GraphWeave, an integrated testing platform for graph databases. This includes a multi-agent system that analyzes the flood of bug reports to produce gating rules for issue filtering and adapter rules for dialect adaptation, and a plan-aware triage routes metamorphic pairs by plan, skipping those that share a plan on the same graph state and therefore cannot detect defects. We apply GraphWeave to NeuG, a recently open-sourced industrial graph database that has not been covered by prior graph database testing work. With modest manual effort, GraphWeave uncovers 19 previously unknown bugs, all of which have since been confirmed.

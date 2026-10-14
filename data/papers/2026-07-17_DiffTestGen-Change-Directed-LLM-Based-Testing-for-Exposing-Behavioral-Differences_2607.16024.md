# DiffTestGen: Change-Directed LLM-Based Testing for Exposing Behavioral Differences

- arXiv ID: `2607.16024v1`
- Authors: Huimin Hu, Cristian Cadar, Michael Pradel
- Published: 2026-07-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.16024v1) | [pdf](https://arxiv.org/pdf/2607.16024v1)

## Abstract

As software evolves over time, it is important to ensure that any behavioral changes occur as intended by developers. A promising approach for this goal is to generate tests that expose behavioral differences between the old and new versions of a program. However, current approaches fail to trigger behavioral differences for many code changes. This paper presents~DiffTestGen, a novel change-directed, LLM-based differential testing approach specifically designed to expose behavioral differences introduced by a code change. The approach is enabled by two key contributions: First, DiffTestGen leverages static call graph analysis and project documentation to identify valid entry points for test generation and to guide the LLM toward reaching the changed code. Second, DiffTestGen iteratively improves our newly introduced union coverage metric, which combines coverage of modified code in the old and the new version, by providing targeted coverage feedback to the LLM. We evaluate DiffTestGen on two datasets comprising a total of 463 PRs. DiffTestGen exposes behavioral differences in 78.2% of the PRs while achieving an average union coverage of 90.7%. Compared with the baselines, DiffTestGen exposes 99 more PRs overall and increases code coverage by 12.5% and 15.6% percentage points, respectively. By integrating DiffTestGen with the Testora regression detector, we show that the identified behavioral differences can be used to detect regression bugs missed by the best existing approaches.

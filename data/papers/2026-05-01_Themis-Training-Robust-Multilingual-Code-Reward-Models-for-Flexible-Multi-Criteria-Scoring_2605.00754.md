# Themis: Training Robust Multilingual Code Reward Models for Flexible Multi-Criteria Scoring

- arXiv ID: `2605.00754v1`
- Authors: Indraneil Paul, Glavaš Glavas, Iryna Gurevych
- Published: 2026-05-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2605.00754v1) | [pdf](https://arxiv.org/pdf/2605.00754v1)

## Abstract

Reward models (RMs) have become an indispensable fixture of the language model (LM) post-training playbook, enabling policy alignment and test-time scaling. Research on the application of RMs in code generation, however, has been comparatively sparse, with existing work largely focusing on execution feedback. This choice constrains post-training to optimizing functional correctness over self-contained executable code. In this work, we examine the training and evaluation of multilingual, multi-criteria code RMs. To this end, we first compile Themis-CodeRewardBench, a benchmark to evaluate code RMs across five preference dimensions (i.e., criteria) and eight programming languages, on which we profile 50+ code, math, and general-purpose RMs. Observing the limited proficiency of current RMs beyond scoring for functional correctness, we develop Themis-CodePreference, the largest open-source collection of code preferences to date (more than 350k preference pairs), and use it to train Themis-RM, a suite of multilingual code reward models for flexible multi-criteria scoring, ranging in size from 600M to 32B parameters. Our experiments and ablations demonstrate positive scaling trends, strong cross-lingual transfer when training on diverse preferences, and the importance of multi-criteria training for reliable code reward modeling.

# NeuroFlake: A Neuro-Symbolic LLM Framework for Flaky Test Classification

- arXiv ID: `2605.11482v1`
- Authors: Khondaker Tasnia Hoque, Toukir Ahammed
- Published: 2026-05-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.11482v1) | [pdf](https://arxiv.org/pdf/2605.11482v1)

## Abstract

Flaky tests, which exhibit non-deterministic pass/fail behavior for the same version of code, pose significant challenges to reliable regression testing. While large language models (LLMs) promise for automated flaky test classification, they often fail to comprehend the actual logic behind test flakiness, instead overfitting to superficial textual artifacts (e.g., specific variable names). This semantic fragility leads to poor generalization on real-world imbalance dataset and vulnerability to perturbations. In this paper, we introduce NeuroFlake, a novel neuro-Symbolic framework for classifying flaky tests on highly imbalanced, real-world datasets (FlakeBench). Unlike prior approaches that rely on brittle manual rule and black box learning, NeuroFlake integrates a Discriminative Token Mining (DTM) module to automate the discovery of high-fidelity, statistically significant source code tokens (e.g., specific concurrency primitives or async waits). By injecting these strong latent signals directly into LLM's attention mechanism, we bridge the gap between neural intuition and symbolic precision. Our experiments demonstrate that neuro-symbolic fusion significantly improves classification performance by leveraging classification F1-score to 69.34% while prior state-of-art shows best F1-score 65.79%. However, we rigorously evaluate NeuroFlake's robustness through adversarial stress testing, introducing semantic preserving augmentations (e.g., dead code injection, variable renaming). While baseline models exhibit performance degradation of 8-18 percentage points (pp) on perturbed tests, NeuroFlake maintains performance stability on unseen augmentations dropping only 4-7 pp.

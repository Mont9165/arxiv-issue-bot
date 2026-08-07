# How Far Are We from Detecting Flaky Tests? On the Limits of Code-Based Detection

- arXiv ID: `2607.09345v1`
- Authors: Ömer Oktay Gültekin, Alexander Berndt, Jonathan Bell, Thomas Bach, Sebastian Baltes
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.09345v1) | [pdf](https://arxiv.org/pdf/2607.09345v1)

## Abstract

Flaky tests pass and fail on the same code version, weakening the signal of test results and disrupting continuous integration (CI) pipelines. Code-based flakiness detectors report strong benchmark results, yet their use in practice remains limited. We argue that the field is studying the wrong problem: Flakiness is not a static property of test code, which often lacks the information needed to decide whether a test is flaky. Analyzing three code-based detectors operating on test code, we found that widely used benchmarks contain shortcuts that inflate reported F1 scores and that evaluation protocols overstate generalizability. To control for these shortcuts, we curated two datasets. The first, C-IDoFT (54,468 unit tests from 57 GitHub projects), keeps a developer-confirmed subset of IDoFT's flaky tests and rebuilds only the non-flaky class from repeated executions instead of fixed versions of flaky tests. C-IDoFT is a controlled counterfactual, not a benchmark for reuse. Our CodeBERT reimplementations of two published detectors scored far above its constant baselines under the published cross-validation protocol but no better than them once projects were separated. The high scores rested on the labeling shortcut and the evaluation protocol, not on the test code. On FlakeBench, a benchmark restricted to flakiness types typically recognizable from test code, and the same project-disjoint protocol, the models identified nearly all flaky tests. The second dataset, mined from CI logs, contains 86 flaky end-to-end tests that passed and failed on the same commit. The test code and CI log yielded a cause for 42% of them; the other 58% required further execution evidence. Rather than abandoning flakiness prediction, we reframe it around whether an observed failure is flaky and how likely a test is to fail given its execution environment. Our datasets and CI-mining method support this direction.

# A Dataset of Reproducible Flaky-Test Failures

- arXiv ID: `2605.21677v1`
- Authors: Suzzana Rafi, Mahbub-Ul-Hoque Sumon, Md Erfan, Maruf Morshed Khan, August Shi, Wing Lam
- Published: 2026-05-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.21677v1) | [pdf](https://arxiv.org/pdf/2605.21677v1)

## Abstract

Flaky tests pass and fail non-deterministically when run on the same version of code. Although many techniques have been proposed to detect, debug, and repair flaky tests, reproducing their failures remains a major challenge due to their inherent nondeterminism. Many flaky test datasets exist to help researchers study them, but these datasets are often composed of disjoint sets of flaky tests, where each dataset provides unique information, such as flaky tests of different categories, failure logs of flaky tests, or flaky tests reported by developers vs. flaky tests found by automated tools. In this work, we aim to create a reproducible dataset of flaky tests, curated from both developer issue reports and a popular dataset of flaky tests. Compared to prior flaky test datasets, our dataset is the first to provide (1) a reproducible environment to compile flaky tests, (2) scripts to reproduce failures, (3) scripts to automatically apply flaky test fixes and ensure that the tests are no longer flaky, and (4) execution logs of flaky test passing and failing. We present ReproFlake, a dataset of 1115 reproducible flaky tests across four flaky test categories. We create guidelines to help others contribute to this reproducible dataset, and demonstrate how to use our dataset to understand challenges in reproducing flaky test failures (e.g., challenges researchers may face when using prior flaky test datasets), the characteristics (e.g., location of the fix and its correlation with the flaky test category), and difficulties researchers may face in using our dataset to collect additional information (e.g., code coverage) about flaky tests. Our findings show that error information helps identify flaky test categories and guide repairs, that unresolved compilation failures highlight challenges in building legacy projects, and knowing typical fix locations can help prioritize repair efforts.

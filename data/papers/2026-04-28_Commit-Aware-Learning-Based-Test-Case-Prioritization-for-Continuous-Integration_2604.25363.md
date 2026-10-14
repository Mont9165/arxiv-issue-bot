# Commit-Aware Learning-Based Test Case Prioritization for Continuous Integration

- arXiv ID: `2604.25363v1`
- Authors: Lorenzo Abbondante, Gerardo Canfora
- Published: 2026-04-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.25363v1) | [pdf](https://arxiv.org/pdf/2604.25363v1)

## Abstract

Regression testing in Continuous Integration (CI) pipelines is increasingly costly due to the growing size and execution frequency of test suites. Test Case Prioritization (TCP) mitigates this problem by reordering tests to expose faults earlier. However, most existing techniques rely primarily on historical execution data and coverage metrics, neglecting the rich structural information contained in code changes. This paper proposes a commit-aware, learning-based TCP method that combines structural properties of version-control diffs, test coverage relations, and historical execution behavior into a unified predictive model. Given a new commit, the method estimates the probability that each test suite will reveal at least one failure and prioritizes test execution accordingly. We evaluate our method on five Defects4J projects using a leave-one-project-out cross-project validation setting. Results show that the commit-aware TCP significantly outperform non-commit-aware-baselines in both classification and prioritization effectiveness. Our findings show that including commit structural semantics substantially enhances regression fault detection and enables robust, generalizable learning-based TCP in CI environments.

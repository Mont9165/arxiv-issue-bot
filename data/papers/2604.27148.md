# CI-Repair-Bench: A Repository-Aware Benchmark for Automated Patch Validation via CI Workflows

- arXiv ID: `2604.27148v1`
- Authors: Rabeya Khatun Muna, Md Nakhla Rafi, Tse-Hsun, Chen
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.27148v1) | [pdf](https://arxiv.org/pdf/2604.27148v1)

## Abstract

Continuous Integration (CI) enforces repository-level correctness through multi-stage workflows and is central to modern software development, yet diagnosing and repairing CI failures remains challenging. Unlike traditional program repair, CI failures frequently involve non-code artifacts, environment and dependency issues, noisy execution logs, and workflow-level constraints. Existing program repair benchmarks fall short in this setting: they are largely test-centric, restrict repairs to source code, assume fixed execution environments, and evaluate under simplified CI workflows that do not reflect real repository-level validation. We introduce CI-Repair-Bench, a benchmark for CI-verified, repository-level program repair constructed from real GitHub Actions executions. It contains 567 CI failure instances from 103 repositories and evaluates repair correctness exclusively through full CI re-execution under original workflows. Failures are categorized into 12 CI error types, enabling fine-grained, error-type-aware evaluation. To demonstrate benchmark usage, we include a reference CI repair workflow that analyzes CI logs to localize faults and generate candidate patches. Empirical results show that automated repair is most effective for localized, tool-enforced failures such as formatting and linting, while environment, dependency, and configuration-related failures remain challenging; the best-performing LLM achieves an 18.9% repair success rate. CI-Repair-Bench provides a realistic evaluation foundation for advancing research on CI-native automated program repair.

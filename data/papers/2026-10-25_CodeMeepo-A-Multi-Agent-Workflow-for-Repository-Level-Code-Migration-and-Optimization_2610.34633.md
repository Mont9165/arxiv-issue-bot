# CodeMeepo: A Multi-Agent Workflow for Repository-Level Code Migration and Optimization

- arXiv ID: `2610.34633v1`
- Authors: Farzad Habibi, Changrong Wu, Jinzhou Jiang, Guohan Lu
- Published: 2026-10-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.34633v1) | [pdf](https://arxiv.org/pdf/2610.34633v1)

## Abstract

Repository-level code migration rewrites an entire project in a new programming language while preserving its observable behavior. It is challenging because behavior spans interdependent modules, dependencies and build infrastructure must be adapted to the target ecosystem, and the source code is often the only specification.
  Large language model agents can now attempt these migrations end to end, but three challenges remain. First, an agent that writes both the translation and its acceptance tests may overlook the same requirements in both, leaving missing or incorrect behavior undetected. Second, large repositories can exceed a model's context window, and dividing the work into smaller tasks does not ensure that all required behavior is migrated. Third, even behaviorally correct translations may be slower than the original implementation.
  We present CodeMeepo, a multi-agent pipeline for complete and efficient migration of large repositories. Each milestone is evaluated against a fixed external oracle that the agents neither author nor modify. A separate parity assessment compares source and target components in scope and adds identified gaps back into the plan as required work. Ordered milestones limit the scope of each task, while cumulative regression checks guard against breaking already-migrated behavior. A benchmark-guided optimization phase addresses performance, followed by full-suite conformance testing and repair. Eight specialized agent roles communicate through file artifacts, and a deterministic state machine governs repair, deferral, scope changes, and termination.
  On nine subjects in three language pairs, CodeMeepo achieves the best pass rate on every subject and passes 18% more tests than a state-of-the-art multi-agent baseline using the same model. On a production daemon, its optimization phase improves half of the benchmarks, by 25% on average.

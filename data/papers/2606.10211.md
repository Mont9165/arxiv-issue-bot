# TestMap: Evidence Infrastructure for Foundation-Model-Assisted Test Generation

- arXiv ID: `2606.10211v1`
- Authors: Hunter Leary, Luke Hanuska, Chris Brown
- Published: 2026-06-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.10211v1) | [pdf](https://arxiv.org/pdf/2606.10211v1)

## Abstract

Foundation models (FMs) can generate plausible unit tests, but determining whether those tests are correct, useful, maintainable, and worth integrating remains difficult. Generated tests must be mapped to the code they target, inserted into real projects, built, executed, measured against the baseline suite, repaired when necessary, and compared across models and generation strategies. This validation process is fragmented across build systems, test runners, coverage tools, mutation tools, static analyzers, and experiment scripts. The problem is especially important because generated tests are both code artifacts and validation artifacts: they must themselves be validated before they can be trusted as evidence about the system under test. This paper presents TestMap, an open-source infrastructure prototype that automates evidence-backed foundation-model-assisted test generation for C#/.NET repositories. TestMap supports repository analysis, source-test mapping, baseline execution, code metric collection, test smell detection, coverage measurement, mutation testing, model-guided test generation, validation, repair, and repository-specific experiment tracking. Rather than reporting only final passing tests, TestMap records the lifecycle of each generated candidate, including failed, repaired, low-impact, and evidence positive outcomes. These intermediate outcomes can reveal model limitations, missing context, repair cost, toolchain inefficiencies, or possible faults in the system under test. Using TestMap as a design case, we describe the architecture and evidence model needed to make generated tests observable, repeatable, and comparable across repositories, models, prompts, and generation strategies. We conclude with lessons learned and open challenges, including oracle and assertion quality, metric attribution, test maintainability, flakiness, execution cost, and developer acceptance.

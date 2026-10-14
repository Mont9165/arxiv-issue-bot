# DepRepair: LLM-Based Source-Code Repair for Dependency Breaking Changes

- arXiv ID: `2607.17957v1`
- Authors: Shenghao Yang, Bo Lu, Yaochen Liu, Yu Kang, Qiongfang Zhang, Chetan Bansal, Saravan Rajmohan, Minghua Ma
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.17957v1) | [pdf](https://arxiv.org/pdf/2607.17957v1)

## Abstract

Modern software projects depend on numerous third-party libraries, whose updates often introduce breaking changes. Adapting consumer code to such changes remains labor-intensive and error-prone. Existing work either characterizes dependency breaking changes without producing a verified consumer-side patch, or studies automated repair only in settings where the failure and repair context are contained within the target repository. However, dependency breaking changes violate this assumption: the decisive repair evidence lies upstream in release notes and API diffs, and no failing test localizes where the consumer breaks, leaving the repair under-informed. To study this cross-repository problem on real data, we introduce DepBench, a benchmark of 95 real-world dependency-update instances across four ecosystems, each paired with a Docker-based executable oracle that runs the consumer's own tests. To address these challenges, we propose DepRepair, a single-call LLM approach that grounds repair in structured upstream evidence through three components: an evidence filter that distills relevant upstream changes, a usage locator that identifies affected consumer sites, and a subcategory-aware guide that tailors repairs to the breaking-change type. Evaluated on DepBench, DepRepair attains the highest executable pass rate on each backbone, achieving 89.5% with GPT-5.5 and 82.1% with Claude Opus 4.6. We further find that raw upstream evidence reduces LLM and agent pass rates by 7--23 percentage points, whereas structured evidence consistently improves them.

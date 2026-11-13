# CrossPloit: A Benchmark for Cross-Version PoC Migration in Python Web Applications

- arXiv ID: `2611.16588v1`
- Authors: Hung Nguyen-Huu, Nguyen Anh Tuan, Ting Zhang, Yue Liu, Chengran Yang, Lwin Khin Shar, Eng Lieh Ouh, David Lo
- Published: 2026-11-12
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.16588v1) | [pdf](https://arxiv.org/pdf/2611.16588v1)

## Abstract

Affected-version ranges in vulnerability databases decide which deployments scanners, patching pipelines, and incident responders treat as vulnerable, yet these ranges are often incomplete, so vulnerable releases are silently treated as safe. Auditing them requires executable evidence: given a proof-of-concept (PoC) exploit for a listed version, show that the same vulnerability can be triggered on an earlier, unlisted version. This cross-version PoC migration combines source-code analysis, environment repair, and execution-based verification. We introduce CrossPloit, a benchmark of 127 migration instances across 45 CVEs in the Python web ecosystem. Each instance includes a version-pinned container, a reference PoC, and a vulnerability-specific oracle; two validators check that the observed effect arises from the disclosed vulnerability. Benchmark construction confirms 149 vulnerable prior versions absent from the affected-version lists of four databases, 127 of which require migration. Across 18 agent configurations (nine models and two harnesses), the best configuration resolves 58.3% of instances, compared with 8.7% for an adapted trace-guided baseline. Attack-vector shifts are particularly difficult: no configuration resolves more than 37.9% of these instances. Higher resolve rates are associated with a smaller share of missed-API failures and a larger share of incomplete executions among the remaining failures. In one configuration, withholding the reference PoC and its environment specification reduces resolve rate from 50.4% to 15.0%, highlighting the value of the supplied reference package. CrossPloit provides an execution-based measurement of under-reported exposure and of how far its enumeration can be automated.

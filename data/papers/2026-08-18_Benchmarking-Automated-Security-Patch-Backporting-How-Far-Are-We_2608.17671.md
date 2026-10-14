# Benchmarking Automated Security Patch Backporting: How Far Are We?

- arXiv ID: `2608.17671v1`
- Authors: Jincheng Yang, Yulong Fu, Chengwei Liu, Lyuye Zhang, Fangyuan Zhang, Bingyang Ren, Yang Liu, Hui Li
- Published: 2026-08-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2608.17671v1) | [pdf](https://arxiv.org/pdf/2608.17671v1)

## Abstract

Automated security patch backporting is critical for mitigating N-day vulnerabilities. Recent tools report success rates above 80% on their respective datasets. However, these evaluations are often confined to homogeneous environments, such as one repository or specific project versions. Consequently, it remains unclear how well these tools generalize beyond their originally targeted scenarios. We present Porting Benchmark, a curated dataset of 1,234 security patch backporting cases spanning cross-version, cross-branch, and cross-repository scenarios, paired with a common evaluation framework. Using this benchmark, we evaluate five tools spanning program analysis, LLM prompting, and LLM agents under aligned settings. Our results show that aligned evaluation changes the apparent performance landscape: PortGPT and TSBPort remain comparatively strong on the Replication Dataset, while FixMorph and Mystique degrade substantially under the common protocol. Performance degrades sharply on structurally complex patches: the best commit-level success rate falls from 85.2% on Type-I patches to 24.0% on Type-IV. We identify four root-cause categories (missing target API awareness, cross-version semantic mismatch, non-local dependency propagation failure, and patch construction or localization failure) and derive concrete directions for next-generation tool design. On a 45-case dynamically validated subset with verified test cases and constructed POCs, we further observe that reference-based benchmark scores do not fully capture real-world remediation: exact match sharply under-credits harder target adaptations, while executable validation reveals residual integration failures in the target that static reference agreement misses. Executable-feedback refinement provides limited but measurable recovery on the hardest executable cases.

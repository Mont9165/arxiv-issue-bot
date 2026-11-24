# ReproShift: Cross-Version Adaptation of Linux Kernel Fuzzing Crash Reproducers

- arXiv ID: `2611.30655v1`
- Authors: Changjian Liu, Zhiwen Tang, Xianying Wang, Fan Ding, Zhengshu Wang, Chao Hu, Yuheng Shen, Ying Fu, Heyuan Shi
- Published: 2026-11-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.30655v1) | [pdf](https://arxiv.org/pdf/2611.30655v1)

## Abstract

Reliable crash reproduction is essential for diagnosing and repairing kernel crashes. Historical crash reproducers preserve concrete bug-triggering knowledge and can be reused for regression testing, bug revalidation, and impact analysis across kernel versions. However, kernel evolution can invalidate these reproducers by changing kernel interfaces, configurations, and execution paths. Migrating them is therefore challenging: the adapted reproducer must identify and modify version-sensitive behavior while preserving the bug-triggering operations and resource dependencies that define the original crash. To address this challenge, we propose ReproShift, an automated framework for cross-version crash reproducer migration by preserving bug-triggering semantics while adapting only version-sensitive behavior. Given source crash artifacts, a source crash reproducer, and a target kernel, ReproShift produces a migrated crash reproducer with same-bug validation evidence. Specifically, ReproShift first constructs a structured source-to-target context to identify migration-relevant kernel changes. It then performs constrained target-aware adaptation to revise version-sensitive reproducer operations while preserving the original trigger logic. Finally, it executes the adapted candidates on the target kernel and uses execution feedback and case-specific crash evidence to iteratively validate candidates and refine subsequent migrations. In a real-world deployment on an evolving upstream kernel, ReproShift further produces 22 upstream crash reports generated from adapted candidates, of which 7 have been fixed and 5 have received explicit maintainer confirmation. To systematically quantify its migration effectiveness, we construct a benchmark of 107 real-world source-target migration cases. ReproShift achieves confirmed same-bug migration in 57 cases, compared with 19 cases using direct replay.

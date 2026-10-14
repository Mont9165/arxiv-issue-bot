# SWE-Cycle: Benchmarking Code Agents across the Complete Issue Resolution Cycle

- arXiv ID: `2605.13139v1`
- Authors: Hao Guan, Lingyue Fu, Shao Zhang, Yaoming Zhu, Kangning Zhang, Lin Qiu, Xunliang Cai, Xuezhi Cao, Weiwen Liu, Weinan Zhang, Yong Yu
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.13139v1) | [pdf](https://arxiv.org/pdf/2605.13139v1)

## Abstract

As autonomous code agents move toward end-to-end software development, evaluating their practical autonomy becomes critical. Current benchmarks hide friction by testing agents in pre-configured environments, and their static evaluation pipelines frequently fail when parsing fully autonomous trajectories. We address these limitations with SWE-Cycle, a benchmark of 489 rigorously filtered instances. SWE-Cycle evaluates agents across three isolated tasks, including environment reconstruction, code implementation, and verification test generation, as well as an end-to-end FullCycle task that integrates all three. The FullCycle task requires agents to work autonomously in a bare repository without human scaffolding. To reliably assess these complex execution paths, we developed SWE-Judge. By combining static code review with dynamic testing, this execution-capable evaluation agent accurately verifies functional correctness and eliminates the systematic measurement errors of traditional static parsers. We evaluate code agents powered by six state-of-the-art LLMs across these four tasks. The results reveal a sharp drop in solve rates when transitioning from isolated tasks to FullCycle execution, exposing critical bottlenecks in handling cross-phase dependencies and maintaining code quality. Together, SWE-Cycle and SWE-Judge provide a comprehensive framework for accurately measuring the end-to-end capabilities of autonomous software agents.

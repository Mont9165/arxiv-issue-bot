# Active-SWE: Benchmarking Coding Agents for Proactive Bug Fixing without Issue Reports

- arXiv ID: `2608.04682v1`
- Authors: Haobin Li, Ping Deng, Weizhong Qian, Liang Jiang, Zhenyu Huang, Mouxing Yang, Xi Peng
- Published: 2026-08-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.04682v1) | [pdf](https://arxiv.org/pdf/2608.04682v1)

## Abstract

Coding agents powered by large language models (LLMs) are increasingly adopted in software engineering (SWE) scenarios, capable of fixing a specific bug in large-scale codebase. However, existing SWE benchmarks typically assume that high-quality issue reports with detailed information are always available, which is easily violated in practice due to the complexity of report acquisition and curation. To address this, we introduce Active-SWE, a benchmark for evaluating coding agents on proactively discovering and fixing multiple bugs without report guidance, covering 1,663 tasks across six bug categories and eight languages. Beyond shifting the focus from existing reactive bug fixing to proactive bug fixing, Active-SWE enables a more in-depth evaluation by expanding the scope from fixing a specific recorded bug to multiple-bug fixing and potential bug discovery scenarios. To construct Active-SWE, we propose a novel difficulty-aware task formulation pipeline with a dual-track evaluation framework, facilitating comprehensive evaluation of proactive bug-fixing capability. Extensive experiments reveal that most state-of-the-art coding agents struggle with proactive bug-fixing tasks, demonstrating limited performance in locating and resolving recorded bugs, handling multiple bug fixing scenarios, and discovering valid potential bugs.

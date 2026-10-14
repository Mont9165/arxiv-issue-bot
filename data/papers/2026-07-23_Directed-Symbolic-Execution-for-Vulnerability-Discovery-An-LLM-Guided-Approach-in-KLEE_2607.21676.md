# Directed Symbolic Execution for Vulnerability Discovery: An LLM-Guided Approach in KLEE

- arXiv ID: `2607.21676v1`
- Authors: Lingfeng Chen, Tao Xiao, Masanari Kondo, Yasutaka Kamei
- Published: 2026-07-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.21676v1) | [pdf](https://arxiv.org/pdf/2607.21676v1)

## Abstract

Symbolic execution effectively discovers security violations but suffers from path explosion. Engines like KLEE therefore use path prioritization heuristics to order state exploration, typically optimizing code coverage. However, path prioritization can become trapped in cyclic control-flow regions, where repeated branching consumes the exploration budget before exploration reaches vulnerable code beyond these cyclic regions. We propose KLEECopilot, a Large Language Model (LLM)-guided directed symbolic execution approach built on KLEE. KLEECopilot uses LLMs to mark potentially vulnerable code and guide path prioritization. It also integrates loop-exit prioritization to escape potentially non-vulnerable cycles and progress toward deeper vulnerabilities. Compared with baselines such as Empc, KLEECopilot improves basic block coverage by 42.24% and line coverage by 125.82%. It discovers 1,335 total violations and 87 unique violations, outperforming the second-best baseline by 32.2% in total violations and Empc by 24.3% in unique violations. Although KLEECopilot is sensitive to model family, it exhibits only marginal sensitivity to model scale, supporting the efficacy of integrating security semantics and loop-exit prioritization. Ablation studies further show that individual components contribute to effectiveness: alternative configurations involving searchers, internal components, marking sources, and prompt variants yield only 54--61 unique violations, while KLEECopilot maintains competitive code coverage.

# ASAD: Adaptive Software Agents for Debugging

- arXiv ID: `2610.00629v1`
- Authors: Yacine Majdoub, Eya Ben Charrada, Haifa Touati
- Published: 2026-09-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.00629v1) | [pdf](https://arxiv.org/pdf/2610.00629v1)

## Abstract

The integration of Large Language Models (LLMs) into multi-agent systems has shown great potential for automated debugging. Yet nearly all current frameworks rely on rigid, predefined architectures: the number of agents, their roles, and their interaction patterns are fixed before any analysis of the bug occurs. This one-size-fits-all approach is fundamentally mismatched to the heterogeneous nature of software defects. Simple bugs waste resources on unnecessary coordination, while complex ones suffer from insufficient or poorly aligned expertise. This paper introduces ASAD, an adaptive agentic system for debugging that configures its team according to the nature and complexity of each bug. ASAD initiates the debugging process by analyzing the faulty code and dynamically determines the number of agents to deploy, the specialized roles they should have, and the collaboration strategy they should follow. A central coordinator orchestrates this process through iterative planning, reflection, and execution; applying fast single-pass repairs for simple issues while assembling purpose-built teams to tackle more complex failures. We evaluate ASAD on three established benchmarks: Defects4J, DebugBench, and CodeFlaws, using multiple LLMs, such as DeepSeek-V3, Qwen-3 and GPT-5. ASAD consistently improves bug-fix rates by 12--20% over chain-of-thought(CoT) prompting and consistently outperforms static multi-agent systems by 4--9% in fix precision while reducing average agent usage by 32%. Crucially, our system dynamically adjusts the number and roles of agents: it resolves simple bugs with minimal coordination and scales agent involvement only for more complex cases.

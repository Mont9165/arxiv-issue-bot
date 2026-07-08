# LogicHunter: Testing LLM Agent Frameworks with an Agentic Oracle

- arXiv ID: `2607.06195v1`
- Authors: Minghui Long, Yanjie Zhao, Haoyu Wang
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.06195v1) | [pdf](https://arxiv.org/pdf/2607.06195v1)

## Abstract

Large Language Model (LLM) agent frameworks such as LangChain, LlamaIndex, and CrewAI have become critical infrastructure powering production AI systems, yet they remain severely under-tested due to fundamental challenges in automated testing. Unlike traditional software, where crashes serve as reliable oracles, defects in these pure Python frameworks manifest as ordinary exceptions or silent semantic failures, creating profound oracle ambiguity. This problem is exacerbated by strict type governance through Pydantic schemas and complex protocol requirements that cause existing fuzzers to generate overwhelming invalid inputs, while traditional test generators produce only trivial cases with weak regression assertions.
  We present LogicHunter, a fuzzing framework that addresses both the generation and oracle challenges through active specification-aware testing. LogicHunter employs specification-driven generation that systematically fuses formal type constraints with authentic usage patterns from real-world repositories, synthesizing inputs that are valid by construction yet semantically extreme, equipped with behavioral probes to expose silent failures. To resolve oracle ambiguity, we introduce the Agentic Oracle, which transcends passive classification by actively retrieving documentation, navigating source code, and inspecting runtime states through a ReAct-based architecture with Dual-Layer State Management and Dual-Stream Memory. Evaluated on three widely deployed frameworks, LogicHunter discovered 40 previously unknown bugs with 30 confirmed and 26 fixed by developers, while state-of-the-art baselines reported no bugs as final findings. The Agentic Oracle achieves 91.17% precision, surpassing the best passive approach at 29.27% by 61 percentage points.

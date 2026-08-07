# MemRepair: Hierarchical Memory for Agentic Repository-Level Vulnerability Repair

- arXiv ID: `2605.17444v1`
- Authors: Simiao Liu, Li Zhang, Fang Liu, Xiaoli Lian, Yang Liu, Yinghao Zhu
- Published: 2026-05-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2605.17444v1) | [pdf](https://arxiv.org/pdf/2605.17444v1)

## Abstract

Modern software ecosystems face a rapidly growing number of disclosed vulnerabilities, increasing the need for automated repair techniques that can operate reliably at repository scale. Although Large Language Model (LLM)-based agents have recently shown promise for automated vulnerability repair (AVR), most existing systems still treat repair as a single generation step over the currently visible code context. As a result, they lack a persistent mechanism for reusing prior fixes or learning from failed validation attempts, which limits their effectiveness on complex, multi-file repair tasks. We present MemRepair, a memory-augmented agentic framework that formulates vulnerability repair as an iterative, experience-driven process. MemRepair combines three complementary memory layers, i.e., History-Fix, Security-Pattern, and Refinement-Trajectory memories, with a dynamic feedback-driven refinement loop. This design allows the agent to retrieve repository-specific repair conventions, apply reusable security defenses, and exploit prior "failure-to-success" trajectories to revise semantically invalid patches based on runtime evidence. We evaluate MemRepair on three representative repository-level vulnerability repair benchmarks: SEC-Bench, PatchEval (Python, Go, JavaScript), and the C++ subset of Multi-SWE-bench. MemRepair achieves state-of-the-art resolution rates of 58.0%, 58.2%, and 30.58%, respectively, outperforming strong general-purpose agents such as OpenHands and SWE-agent, as well as the specialized AVR tool InfCode-C++, while maintaining competitive repair cost. These results show that persistent, hierarchical repair memory can substantially improve the reliability of agentic vulnerability repair across diverse languages and repository settings.

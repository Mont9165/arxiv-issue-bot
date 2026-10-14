# Empowering Autonomous Debugging Agents with Efficient Dynamic Analysis

- arXiv ID: `2604.24212v1`
- Authors: Jiahong Xiang, Xiaoyang Xu, Xiaopan Chu, Hongliang Tian, Yuqun Zhang
- Published: 2026-04-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.24212v1) | [pdf](https://arxiv.org/pdf/2604.24212v1)

## Abstract

Autonomous agents for automated program repair represent a promising frontier in software engineering, yet their effectiveness is often hindered by reliance on post-mortem, coarse-grained execution feedback. While integrating traditional interactive debuggers seems a natural solution, their low-level, line-by-line interaction paradigm turns out to be cost-inefficient for LLM-based agents, leading to exhausted budgets and unproductive loops. To mitigate this, we introduce Agent-centric Debugging Interface (ADI), a novel agent-centric debugging interface designed for cost-efficient, end-to-end autonomous interaction. Specifically, Agent-centric Debugging Interface realizes a function-level interaction paradigm, powered by our Frame Lifetime Trace, a comprehensive data structure encapsulating a function's stateful execution trace, and a set of high-level navigational commands. Our extensive evaluation on the SWE-bench benchmark demonstrates the effectiveness and efficiency of ADI. By simply equipping a basic agent with ADI, it successfully resolves 63.8\% of the tasks on the SWE-bench Verified set, even slightly outperforming the highly optimized and high-investment Claude-Tools agent, at an average cost of USD 1.28 per task with Claude-Sonnet-3.7. Furthermore, we demonstrate ADI's generality by integrating it as a plug-and-play component into existing SOTA agents, delivering consistent gains ranging from 6.2\% to 18.5\% on the resolved tasks. These results indicate that Agent-centric Debugging Interface can provide a general and efficient enhancement for existing autonomous agents.

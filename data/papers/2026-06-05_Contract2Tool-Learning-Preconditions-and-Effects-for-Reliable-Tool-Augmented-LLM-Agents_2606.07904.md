# Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents

- arXiv ID: `2606.07904v1`
- Authors: Rahul Suresh Babu, Laxmipriya Ganesh Iyer
- Published: 2026-06-05
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.07904v1) | [pdf](https://arxiv.org/pdf/2606.07904v1)

## Abstract

Tool-augmented large language model agents increasingly rely on external APIs, but standard tool schemas describe how to call a tool, not when the tool is causally appropriate or what task state it produces. Causal tool filtering addresses this gap by using lightweight contracts that specify each tool's preconditions, effects, risk level, and cost. However, manually writing and maintaining such contracts does not scale to large or changing tool ecosystems. We introduce Contract2Tool, a framework for inferring tool contracts from metadata, schemas, documentation, and execution traces. Contract2Tool converts observable tool evidence into normalized symbolic contracts that can be evaluated intrinsically and deployed inside downstream causal tool filtering. We evaluate learned contracts against gold preconditions, effects, and risk labels, and measure their downstream utility on multi-step agent tasks. Our results show that hybrid documentation-and-trace evidence produces contracts accurate enough to preserve most of the reliability and efficiency benefits of gold contracts. Learned-contract CMTF achieves 0.980 downstream success, close to 0.990 for gold-contract CMTF, while reducing visible tools from 100 to 1 and reducing average token usage from 26,172 to 2,528 relative to all-tools exposure. These results suggest that learned contracts can provide a scalable contract layer between tool schemas and reliable agent execution.

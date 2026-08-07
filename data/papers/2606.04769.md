# Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications

- arXiv ID: `2606.04769v1`
- Authors: Yutao Shi, Xiaohan Zhang, Xiangjing Zhang, Xihua Shen, Hui Ouyang, Huming Qiu, Mi Zhang, Min Yang
- Published: 2026-06-03
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.04769v1) | [pdf](https://arxiv.org/pdf/2606.04769v1)

## Abstract

The Model Context Protocol (MCP) has emerged as a critical standard empowering Large Language Models (LLMs) to utilize external tools. In this ecosystem, LLMs rely on natural language descriptions provided by MCP servers to select and execute functions. This interaction implicitly assumes that tool descriptions faithfully reflect their underlying implementations, while this assumption is not mandatorily verified in practice. As a result, MCP deployments may suffer from a problem named Description-Code Inconsistency (DCI), where a tool's description of its capabilities and security boundaries is not consistent with what the code actually does.
  In this paper, we present a comprehensive study of DCI in real-world MCP servers. We formally define the problem and propose a comprehensive taxonomy spanning functionality inconsistencies and undeclared side effects. Guided by this taxonomy, we develop DCIChecker, an automated framework that combines structure-aware static analysis with the Direct-Reverse-Arbitration prompting method to cross-validate tool descriptions against actual code implementations. We apply this framework to a large-scale dataset comprising 19,200 description-code pairs extracted from 2,214 real-world MCP servers. Our measurement reveals that DCI is widespread, with 9.93% of these pairs exhibiting inconsistencies. We further demonstrate that DCI creates a critical defense blind spot, facilitating varied risks from operational failures to stealthy malicious behaviors. Finally, we propose mitigation strategies to enforce semantic consistency and enhance the reliability of the emerging agentic ecosystem.

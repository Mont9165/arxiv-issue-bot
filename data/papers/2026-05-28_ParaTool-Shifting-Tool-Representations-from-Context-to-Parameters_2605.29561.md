# ParaTool: Shifting Tool Representations from Context to Parameters

- arXiv ID: `2605.29561v1`
- Authors: Zekai Yu, Qi Meng, Qizhi Chu, Yu Hao, Chuan Shi, Cheng Yang
- Published: 2026-05-28
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.29561v1) | [pdf](https://arxiv.org/pdf/2605.29561v1)

## Abstract

Tool calling extends large language models (LLMs) by enabling grounded interaction with external executable interfaces, thereby supporting environment-coupled problem solving. However, mainstream in-context learning (ICL) approaches typically incorporate detailed tool documentation and usage examples directly into the context. This results in substantial inference overhead and heightened risks of hallucination as the context length grows. Conversely, while tuning-based methods improve general tool-calling capabilities, they often fail to effectively internalize the specific details of previously seen tools, thereby retaining a dependency on in-context documentation. To address these limitations, we propose ParaTool, a framework that projects each tool into a dedicated, loadable set of parameters. By equipping a dynamic integration of these parameterized tools, the LLM can perform tool calling without relying on in-context documents or examples. Specifically, our approach consists of three stages: (1) parametric tool pre-training encapsulates the knowledge of different tools into independent parameter modules; (2) soft tool selection employs a gating network to dynamically weigh and aggregate relevant tool parameters; and (3) parametric tool fine-tuning jointly updates tool parameters to align the training and inference processes. Experiments on Stable ToolBench and BFCL demonstrate that ParaTool significantly outperforms strong ICL-based baselines, achieving superior performance while reducing computational complexity.

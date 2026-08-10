# Beyond Text Matching: Towards Reference-Free Evaluation for Human-Oriented Binary Reverse Engineering

- arXiv ID: `2608.07038v1`
- Authors: Xiuwei Shang, Li Hu, Xiao Jiang, Jieke Shi, Junda He, Zhou Yang, Shaoyin Cheng, Guoqiang Chen, Weiming Zhang, David Lo
- Published: 2026-08-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2608.07038v1) | [pdf](https://arxiv.org/pdf/2608.07038v1)

## Abstract

Human-Oriented Binary Reverse Engineering (HOBRE) aims to transform decompiled pseudocode into a more human-friendly representation, thereby reducing the cognitive burden of reverse analysis and improving efficiency. However, reliably evaluating HOBRE outputs remains a fundamental challenge: human evaluation is costly, time-consuming, and difficult to scale, while existing automated metrics either require executable test cases and runtime environments that are often unavailable for real-world binaries, or rely on high-quality source code references that are typically inaccessible and fail to capture semantically equivalent but lexically diverse outputs. Although LLM-as-a-Judge paradigm is naturally well-suited to HOBRE evaluation, its effectiveness remains underexplored.
  This paper presents the first systematic investigation of the LLM-as-a-Judge paradigm for HOBRE across three representative tasks: function name recovery, binary code summarization, and decompilation optimization. We introduce BinJudgeBench, the first expert-annotated, reference-free evaluation benchmark based on multi-dimensional human judgment, where LLM-as-a-Judge achieves an average correlation of 63.20\% with human judgment, outperforming traditional automated metrics at 35.04\%. By analyzing judge configurations across backbone LLMs, prompting strategies, and decoding temperatures, we find that no ``one-size-fits-all'' configuration exists, as the optimal setup varies across tasks and individual samples. To address this, we propose BinJudge, which employs a lightweight routing mechanism to adaptively select the optimal judge configuration for each task and sample. BinJudge improves correlation with human experts by 4.5\%-24.7\% and reduces API cost to 0.06$\times$-0.84$\times$ of that of static best configurations, providing a scalable, cost-effective, and high-fidelity automated evaluation scheme for HOBRE.

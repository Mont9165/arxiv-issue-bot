# An Empirical Study of Proactive Coding Assistants in Real-World Software Development

- arXiv ID: `2605.05700v1`
- Authors: Lehui Li, Ruixuan Jia, Guo-Ye Yang, Jia Li
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.05700v1) | [pdf](https://arxiv.org/pdf/2605.05700v1)

## Abstract

Large language model (LLM)-based coding assistants have made substantial progress, yet most systems remain reactive, requiring developers to explicitly formulate their needs. Proactive coding assistants aim to infer latent developer intent from integrated development environment (IDE) interactions and repository context, thereby reducing interaction overhead and supporting more seamless assistance. However, research in this direction is limited by the scarcity of large-scale real-world developer behavior data. Existing studies therefore often rely on LLM-simulated IDE traces, whose fidelity to real development behavior remains unclear. In this paper, we investigate this simulation-to-reality gap through a large-scale empirical study. We collect real IDE interaction traces from 1{,}246 experienced industry developers over three consecutive days using a custom Visual Studio Code extension, and construct paired LLM-simulated traces for controlled comparison. Our analysis shows that simulated traces differ substantially from real traces in behavioral diversity, temporal structure, and exploratory patterns. Based on the collected data, we introduce \textbf{ProCodeBench}, a real-world benchmark for proactive intent prediction. Experiments with representative LLMs, retrieval-augmented methods, and agentic baselines show that current approaches remain far from reliable under real IDE traces, suggesting that simulation-based evaluation can overestimate real-world performance. Finally, our training study shows that simulated data cannot replace real data, but can complement it when used before real-world fine-tuning. These findings highlight the importance of real developer behavior data for evaluating and training proactive coding assistants.

# REStack: A Large-Scale Dataset of Reverse Engineering Discussions from Stack Exchange

- arXiv ID: `2606.05493v1`
- Authors: Md Humaun Kabir, Md Rakibul Islam, Farha Kamal
- Published: 2026-06-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.05493v1) | [pdf](https://arxiv.org/pdf/2606.05493v1)

## Abstract

Reverse engineering (RE) is a critical activity in software engineering and cybersecurity, supporting tasks such as malware analysis, vulnerability discovery, legacy system maintenance, and firmware inspection. Despite its importance, there is limited empirical understanding of the challenges, topics, and knowledge gaps faced by RE practitioners in real-world settings, and no publicly available dataset has systematically captured RE discussions from developer Q&A forums.
  In this paper, we present REStack, a large-scale dataset of RE discussions collected from Stack Overflow and the dedicated Reverse Engineering Stack Exchange site. The dataset comprises over 12,000 RE-related posts spanning more than 15 years. Using Latent Dirichlet Allocation (LDA) with Genetic Algorithm (GA)-based hyperparameter optimization, followed by manual topic labeling, we identify 23 semantically coherent RE topics grouped into six high-level thematic categories. The dataset is further enriched with metadata and difficulty indicators derived from community interaction signals, such as unanswered rates and response times.
  Our analysis reveals that RE discussions are predominantly practical and task-oriented, with strong emphasis on debugging, decompilation, and system-level analysis, while topics related to memory, firmware, and file format analysis exhibit high difficulty and unresolved rates. Beyond empirical characterization, REStack provides a reusable resource for empirical studies, educational research, and the development and evaluation of AI- and LLM-based developer assistance tools for RE. By releasing the dataset and accompanying scripts, this work aims to facilitate reproducible research and advance data-driven support for RE practice.

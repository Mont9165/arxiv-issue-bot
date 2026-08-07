# Assessing the Impact of Requirement Ambiguity on LLM-based Function-Level Code Generation

- arXiv ID: `2604.21505v1`
- Authors: Di Yang, Xinou Xie, Xiuwen Yang, Ming Hu, Yihao Huang, Yueling Zhang, Weikai Miao, Ting Su, Chengcheng Wan, Geguang Pu
- Published: 2026-04-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.21505v1) | [pdf](https://arxiv.org/pdf/2604.21505v1)

## Abstract

Software requirement ambiguity is ubiquitous in real-world development, stemming from the inherent imprecision of natural language and the varying interpretations of stakeholders. While Large Language Models (LLMs) have demonstrated impressive capabilities in generating code from precise specifications, such ambiguity poses a significant obstacle to reliable automated code generation. Existing benchmarks typically assume clear and unambiguous requirements, leaving an empirical gap in understanding how LLMs behave when faced with the inherent uncertainty of real-world software requirements. In this paper, we introduce Orchid, the first code generation benchmark specifically designed with ambiguous requirements. It comprises 1,304 function-level tasks covering four distinct types of ambiguity: lexical, syntactic, semantic, and vagueness. Leveraging this dataset, we conduct the first systematic empirical study to evaluate the impact of requirement ambiguity on LLM-based code generation. Our results demonstrate that ambiguity consistently degrades the performance of all evaluated LLMs, with the most pronounced negative effects observed in highly advanced models. Furthermore, we observe that LLMs frequently produce functionally divergent implementations for the same ambiguous requirement and lack the capability to identify or resolve such ambiguity autonomously. These findings reveal a significant performance gap between clear and ambiguous requirements, underscoring the urgent need for ambiguity-aware techniques in the next generation of automated software engineering tools. The Orchid benchmark is publicly available at https://huggingface.co/datasets/SII-YDD/Orchid.

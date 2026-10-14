# Evaluating Non-English Developer Support in Machine Learning for Software Engineering

- arXiv ID: `2605.05902v1`
- Authors: Jonathan Katzy, Yongcheng Huang, Gopal-Raj Panchu, Maksym Ziemlewski, Paris Loizides, Sander Vermeulen, Arie van Deursen, Maliheh Izadi
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.05902v1) | [pdf](https://arxiv.org/pdf/2605.05902v1)

## Abstract

Large Language Models are increasingly used in software engineering, but both code generation and its evaluation remain predominantly English-centric. This leaves a major gap in our understanding of how well current tools support multilingual development, where code contains non-English natural language. In this paper, we investigate non-English code comment generation and the reliability of current methods for evaluating such outputs. We evaluate five code LLMs (CodeGemma, CodeLlama, CodeQwen1.5, GraniteCode, and StarCoder2) across five natural languages: Dutch, English, Greek, Polish and Chinese. We further conduct an open-coding study of 12,500 generated comments, from which we derive a publicly released human-annotated dataset and a taxonomy of 26 error types. We use these human annotations, to evaluate the performance of neural metrics, and LLM-as-a-judge pipelines.
  Our findings show that generative performance deteriorates substantially outside English, with linguistic errors increasing by up to 15.1$\times$, alongside frequent incoherent generations and a rise in semantic errors. More critically, we show that detecting errors in non-English comments underperforms. Across classical overlap-based metrics, off-the-shelf neural metrics, extended neural metrics using newer multilingual, language-specific, and code-specific models, and LLM-as-a-judge pipelines, no automatic approach provides reliable and consistent assessment. Neural metrics fail to distinguish correct comments from incorrect outputs or even random noise, and tend to overestimate quality in non-English settings. LLM-as-a-judge methods achieve the highest agreement with human annotations but fail to reliably capture important language-related and semantic errors. Overall, our results show that evaluation and generation are key barriers for multilingual tooling, and that human judgment remains indispensable.

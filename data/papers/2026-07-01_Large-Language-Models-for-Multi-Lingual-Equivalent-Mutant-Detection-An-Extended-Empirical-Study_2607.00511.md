# Large Language Models for Multi-Lingual Equivalent Mutant Detection: An Extended Empirical Study

- arXiv ID: `2607.00511v1`
- Authors: Honglin Shu, Zhao Tian, Dong Wang, Junji Yu, Jiazhe Zhang, Xuejie Cao, Junjie Chen, Yasutaka Kamei
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.00511v1) | [pdf](https://arxiv.org/pdf/2607.00511v1)

## Abstract

Mutation testing is a powerful technique for ensuring software quality. However, the presence of equivalent mutants introduces unnecessary costs and biases, limiting its practical effectiveness. Although numerous equivalent mutant detection (EMD) methods have been proposed, they often face distinct challenges: pure-code analysis methods can be limited by their reliance on specific compiler infrastructures, while existing machine-learning approaches remain constrained by scarce training data and limited generalization to unseen mutants. Large language models (LLMs) have recently demonstrated remarkable performance across diverse code-related tasks by better capturing program semantics. Yet their potential for EMD remains largely unexplored, particularly in the multi-lingual context. This paper presents the first comprehensive empirical study on LLMs for EMD, using 3,302 Java and 1,088 C mutant pairs to benchmark against state-of-the-art methods, explore strategy variations, assess efficiency, and evaluate cross-lingual generalization. Experimental results show that LLM-based approaches achieve higher F1-scores than the evaluated traditional methods, with fine-tuned code embedding yielding the highest detection accuracy among the tested strategies. Moreover, LLM-based approaches strike a practical balance between effectiveness and efficiency with inference times comparable to existing machine-learning models. Importantly, fine-tuned LLMs demonstrate measurable generalization across programming languages. These findings establish LLMs as a viable and efficient approach for tackling the longstanding challenge of equivalent mutant detection, offering new directions for advancing mutation testing in practice.

# Think Harder and Don't Overlook Your Options: Revisiting Issue-Commit Linking with LLM-Assisted Retrieval

- arXiv ID: `2605.00447v1`
- Authors: Cole Morgan, Muhammad Asaduzzaman, Shaiful Chowdhurry, Shaowei Wang
- Published: 2026-05-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.00447v1) | [pdf](https://arxiv.org/pdf/2605.00447v1)

## Abstract

Linking issue reports to the commits that resolve them is essential for software traceability, maintenance, and evolution. Accurate issue-commit links help developers to understand system changes and the rationale behind them. While numerous automated techniques have been proposed, ranging from heuristic and feature-based approaches to modern deep learning and large language model approaches, our goal is to evaluate these techniques to determine which are most effective and efficient. In this study, we revisit several established issue-commit link recovery techniques, including BTLink, EasyLink, FRLink, RCLinker, and Hybrid-Linker, and assess their performance for reranking issue-commit links. We first evaluate different retrieval methods (BM25, BM25L, SBERT-Semantic Search, ANNOY, LSH, HNSW) for their ability to efficiently retrieve relevant commits, reducing the candidate set that must be considered by more computationally expensive models. Using the best retrieval methods, we then investigate the reranking effectiveness of different machine learning-based techniques, including traditional machine learning models, a cross-encoder, and large language models (ChatGPT, Qwen, Gemma, Llama), to refine the reranking of candidate commits and improve precision. Finally, we compare the effectiveness of these techniques. Our results show that dense retrieval methods outperform sparse retrieval approaches in identifying relevant commits and that combining dense and sparse retrieval can improve recall. Additionally, we find that traditional machine learning-based reranking techniques achieve higher performance than LLM-based approaches. Our results highlight that retrieval-based pipelines remain a practical and effective solution for large-scale issue-commit linking, and that simpler models should be carefully considered before adopting computationally expensive LLM-based approaches.

# Agent-Based Test Assertion Generation via Diverse Perspective Aggregation

- arXiv ID: `2608.05822v1`
- Authors: Dong Wang, Qiaoyu Han, Lin Yang, Jianyi Zhou, Guangtai Liang, Junjie Chen
- Published: 2026-08-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.05822v1) | [pdf](https://arxiv.org/pdf/2608.05822v1)

## Abstract

Test assertions are critical elements of unit tests, serving as checkpoints to validate expected behavior and ensure software correctness. Numerous techniques have been proposed to automate assertion generation, with recent progress notably driven by large language models (LLMs). Despite the promise, existing approaches such as ChatAssert suffer from modest accuracy, heavy reliance on oversampling, and vulnerability to model randomness due to one-shot prompting. To address these limitations, we propose AssertMate, a novel agent-based assertion generation framework that enhances the quality and reliability of LLM-generated assertions through three key components: (1) actual value construction that identifies assertion targets via static analysis and type-aware heuristics; (2) multi-perspective expected value prediction using code generation, retrieval-augmented generation (RAG), and chain-of-thought (CoT) reasoning agents; and (3) an LLM-as-a-Judge collaboration mechanism to select the most appropriate assertion. Evaluation on the Defects4J benchmark demonstrates that AssertMate significantly outperforms state-of-the-art techniques in compilation success and pass rates, along with substantially higher bug detection capabilities. Integration with EvoSuite further validates AssertMate's practicality, yielding superior mutation coverage and kill counts. Ablation studies reveal that each of the three components makes a significant and complementary contribution to the overall performance. This work affirms the great potential of aggregating diverse perspectives to enhance the effectiveness of LLM-based assertion generation.

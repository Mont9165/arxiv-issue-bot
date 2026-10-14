# Memoir: Learning, Verifying, and Evolving False-Positive Memories for Static Application Security Testing Tools

- arXiv ID: `2608.09181v1`
- Authors: Shenyuan Guan, Qiaodan Hou, Yanjun Chen, Xincheng Wen, Jia Feng, Keke Lian, Cuiyun Gao
- Published: 2026-08-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2608.09181v1) | [pdf](https://arxiv.org/pdf/2608.09181v1)

## Abstract

Static Application Security Testing (SAST) tools have become indispensable in modern secure software devel- opment. However, these tools often generate false-positive (FP) alerts, imposing substantial manual inspection costs and reducing the trust from developers. Existing FP reduction methods still face two primary challenges. First, the large differences among SAST tools and vulnerability categories make it difficult for these methods to learn recurring patterns in historical false positives. Moreover, the knowledge used by these methods are largely static and cannot be updated as newly validated cases accumulate. To address these challenges, we propose Memoir, a memory- driven framework for identifying false positives by transform- ing historical FP alerts into reusable semantic memories. It consists of two key modules. First, historical semantic memory construction converts historical FP alerts into structured semantic memories through LLM-guided annotation, pattern clustering, and memory synthesis to capture reusable behavioral patterns. Moreover, memory-driven identification and evolution retrieves relevant memories and performs semantic verification against taxonomy consistency and security invariants before making the final prediction. It then incorporates verified predictions back into the memory repository, allowing the knowledge base to evolve as new cases accumulate. We evaluate Memoir on CWE- Bench-Java to demonstrate its effectiveness in real-world security analysis. Specifically, Memoir achieves an F1-score of 99.43% with a Recall of 98.88% and perfect Precision, consistently outperforming other baselines. Furthermore, an industrial case study on production software systems from a top IT company shows that the learned memory base generalizes effectively across different SAST tools without retraining.

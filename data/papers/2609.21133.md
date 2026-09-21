# The Stochastic Shift: A New Evaluation Paradigm for Text-to-SQL with AI Operators

- arXiv ID: `2609.21133v1`
- Authors: Tarfah Alrashed, Fatma Ozcan, Per Jacobsson, Tal Neiman, Xianshun Chen
- Published: 2026-09-17
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.21133v1) | [pdf](https://arxiv.org/pdf/2609.21133v1)

## Abstract

SQL has been augmented with AI operators, enabling modern data analytics platforms to derive insights from both structured and unstructured data. We observe that while current Text-to-SQL systems can successfully generate these AI-augmented queries, reliably evaluating their correctness remains a critical open challenge. Current metrics, which rely on exact query results and deterministic execution, systematically fail against the flexible, non-deterministic outputs of AI operators. In this paper, we formalize these unique evaluation failure modes and introduce a Multilayered Evaluation Framework that decouples deterministic database logic from flexible AI semantics. We test our approach across both industry (BigQuery) and academic (ThalamusDB) systems. We demonstrate that traditional Execution Accuracy severely penalizes valid queries, achieving as low as a 25% detection rate for correct translations. Furthermore, even a state-of-the-art LLM-based autorater falsely rejects 32% of accurate queries due to the complexity of judging both relational and AI components simultaneously. By validating the standard relational logic and the AI operations separately, our framework achieves state-of-the-art overall accuracy across both platforms (up to 97.2%), proposing a reliable standard for benchmarking AI-powered SQL generators.

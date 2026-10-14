# Test-Time Verification for Text-to-SQL via Outcome Reward Models

- arXiv ID: `2606.30851v1`
- Authors: Mattia Tritto, Giuseppe Farano, Dario Di Palma, Gaetano Rossiello, Fedelucio Narducci, Dharmashankar Subramanian, Tommaso Di Noia
- Published: 2026-06-29
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.30851v1) | [pdf](https://arxiv.org/pdf/2606.30851v1)

## Abstract

Improving the reliability of large language models (LLMs) at inference time is a central challenge in structured reasoning tasks such as Text-to-SQL. Common test-time inference strategies, including Best-of-N sampling and Majority Voting, rely on heuristic signals such as execution success or output frequency, which provide limited semantic discrimination across candidate outputs. In this work, we study Outcome Reward Models (ORMs) as learned semantic scoring functions for test-time verification in Text-to-SQL. While ORMs have been previously explored for test-time scaling and alignment, their application to structured query generation remains underexplored. We introduce GradeSQL, a scalable framework for training task-specific ORMs via automated candidate generation and execution-based labeling, enabling verifier training without manual annotation. We integrate ORMs into a verification-driven Best-of-N pipeline and evaluate our approach on the BIRD and Spider benchmarks across multiple open-source LLM families. ORM-based selection consistently outperforms execution-based Best-of-N and Majority Voting, with gains of up to +4.33% on BIRD and +2.10% on Spider. We further show that ORMs scale effectively with larger candidate sets and yield stronger improvements on complex queries. Overall, our results demonstrate that ORM-based verification provides a simple, effective, and scalable alternative to heuristic test-time selection strategies for Text-to-SQL. Code datasets and models are publicly available.

# Evaluating LLMs in Database Scenarios: A Lifecycle Benchmark for Assessing Their Potential in Core Database Tasks

- arXiv ID: `2608.03794v1`
- Authors: Shunfan Zheng, Dongsheng Shi, Yue Li, Xin Yi, Linlin Wang, Gerard de Melo
- Published: 2026-08-04
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2608.03794v1) | [pdf](https://arxiv.org/pdf/2608.03794v1)

## Abstract

Large Language Models (LLMs) are transforming database interaction paradigms, evolving from simple query translators to autonomous database administrators (DBAs). However, current evaluation benchmarks remain disproportionately fixated on Text-to-SQL tasks, neglecting the holistic Database Lifecycle-from initial schema design to post-deployment maintenance. This narrow focus fails to capture the diverse capabilities required for real-world database management. To bridge this gap, we introduce DBLifeBench, the first benchmark to evaluate LLMs across five critical lifecycle phases: Design, Implementation, Operation, Debugging, and Maintenance. Furthermore, addressing the cognitive mismatch between ambiguous natural language and complex SQL logic, we propose Progressive-Text2SQL, a novel task utilizing structured reasoning graphs to mimic human iterative problem-solving. Our extensive evaluation reveals a critical insight: while general-purpose models demonstrate balanced performance, specialized Text-to-SQL models suffer from ``catastrophic forgetting'' in non-coding phases like design and maintenance. DBLifeBench serves as a foundational step toward evaluating and building true full-stack database intelligence.

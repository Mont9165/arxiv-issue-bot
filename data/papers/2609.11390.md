# VikingRAG: Accurate and Token-efficient Retrieval-augmented Generation over Structured Documents

- arXiv ID: `2609.11390v1`
- Authors: Peiyuan Gao, Gaoyuan Zhang, Haojie Qin, Yahui Sun, Qianyi Zhang, Yunhao Zhang, Zeyu Wang, Wei Lu
- Published: 2026-09-10
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.AI`, `cs.CL`, `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2609.11390v1) | [pdf](https://arxiv.org/pdf/2609.11390v1)

## Abstract

State-of-the-art retrieval-augmented generation (RAG) methods exploit document structures to acquire sufficient evidence, but often incur substantial token costs. To reduce structural-context tokens without compromising high RAG accuracy, we present {\sf VikingRAG}, a directory-aware semantic data management system that tightly integrates semantic and structural access to support structural-context-efficient, evidence-gap-driven multi-round retrieval. To further reduce token overhead of multi-round interaction, we materialize agentic multi-round retrieval traces as experience edges, and reuse these edges for similar queries, avoiding repeated multi-round exploration. To additionally reduce token costs when agentic multi-round retrieval is unnecessary, we introduce an adaptive escalation strategy that answers from one-round experience-augmented retrieval when the evidence is sufficient, and invokes agentic multi-round retrieval only otherwise. Experiments on real datasets show that the base system {\sf VikingRAG} matches high accuracy of state-of-the-art methods while consuming only 11.6\%--51.9\% of their tokens. With retrieval-trace reuse and adaptive escalation, token costs drop to 5.1\%--32.5\% while maintaining competitive accuracy and practical document-storage performance, showing the utility of this work for emerging AI knowledge bases.

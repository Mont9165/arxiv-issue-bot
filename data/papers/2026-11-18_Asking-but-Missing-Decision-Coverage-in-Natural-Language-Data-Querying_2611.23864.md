# Asking but Missing: Decision Coverage in Natural-Language Data Querying

- arXiv ID: `2611.23864v1`
- Authors: Hangle Hu, Chenyu Hou, Bin Cao, Jing Fan, Wei Luo
- Published: 2026-11-18
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.23864v1) | [pdf](https://arxiv.org/pdf/2611.23864v1)

## Abstract

Large language models are increasingly used to translate natural language questions about structured data into executable programs. A fundamental challenge is recognizing when a question admits multiple computational interpretations and identifying the decisions needed to resolve them. We investigate whether language models recognize these unresolved decisions before generating code, or silently adopt assumptions that may lead to incorrect results. We refer to the latter behavior as Underspecified Decision Completion (UDC). To distinguish different causes of UDC, we introduce Grounded Code Generation (GCG), a diagnostic protocol that separates the identification of unresolved decisions, their resolution using evidence, and their translation into executable code. By examining each stage separately, we can determine where the decisions responsible for incorrect results were first missed or mishandled. We evaluate this framework on BIRD-Pandas with twelve models. The results show that answering clarification questions consistently improves execution accuracy, yet substantial errors remain. Our findings suggest that the main difficulty lies not in answering clarification questions, but in recognizing which questions need to be asked in the first place.

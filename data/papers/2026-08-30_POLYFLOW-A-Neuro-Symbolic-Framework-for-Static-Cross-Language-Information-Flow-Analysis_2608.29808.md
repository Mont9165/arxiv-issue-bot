# POLYFLOW: A Neuro-Symbolic Framework for Static Cross-Language Information Flow Analysis

- arXiv ID: `2608.29808v1`
- Authors: Haoran Yang, Zhixuan Zhong, Jiawei Guo, Haipeng Cai
- Published: 2026-08-30
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.29808v1) | [pdf](https://arxiv.org/pdf/2608.29808v1)

## Abstract

Modern software systems are commonly constructed in multiple, interacting programming languages. This construction leads to additional, often stealthy vulnerabilities buried in complex information flow due to language interactions. Existing static analyzers are impeded by the heterogeneous semantics of different languages, whereas dynamic approaches suffer from the limited coverage of (available and/or generated) test inputs. In this paper, we develop PolyFlow, a neural-symbolic framework for statically reasoning about information flow across language boundaries, combining large language models (LLMs) and static analysis synergistically. Governed by the control-flow representation of a given multi-language system, PolyFlow leverages LLMs to identify implicit flow facts due to challenging language features, hence augmenting the base representation and then propagating data flow through the system. It tackles inherent barriers (e.g., token limit and hallucination) of LLMs by putting them under careful guidance (e.g., static-analysis-guided scoping, context management, and fact checking), along with a multi-LLM expert panel for negotiated validation. Our experiments on real-world Python-C and Java-C systems show that PolyFlow is cost-effective and superior to various kinds of state-of-the-art baselines, revealing previously unknown cross-language vulnerabilities that are missed by all the baselines.

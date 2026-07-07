# A Retrieval-Augmented Framework for Detecting and Resolving Pragmatic Ambiguities in Natural Language Requirements

- arXiv ID: `2607.04436v1`
- Authors: Pavithra PM Nair, Preethu Rose Anish
- Published: 2026-07-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.04436v1) | [pdf](https://arxiv.org/pdf/2607.04436v1)

## Abstract

Natural language requirements (NLRs) are essential for bridging communication gaps among diverse stakeholders in software development. However, the inherent ambiguity in NLRs can pose significant challenges. In particular, some requirements may be misinterpreted due to varying contextual knowledge and domain-specific expectations of the stakeholders, a phenomenon known as pragmatic ambiguity. This paper presents an approach for detecting and resolving pragmatic ambiguities in NLRs. The approach leverages retrieval-augmented generation techniques with novice, intermediate, and expert domain knowledge bases to simulate stakeholders with varying domain expertise and detect discrepancies in requirement interpretation. Candidate disambiguated requirements are generated using the expert domain knowledge base, with final validation by a requirements analyst required to ensure alignment with the intended functionality. We evaluate the approach on two requirements specification documents from the PUblic REquirements dataset, using four large language models: GPT-4o-mini, Mistral-7B, Llama-3.1-8B, and Qwen2.5-7B. Detection performance is assessed using macro-averaged accuracy, precision, recall, F1, and F2 scores. The resolution quality of the candidate disambiguated requirements is measured through human evaluation of relevance, clarity, and consistency. In this initial evaluation, results show that the proposed approach can detect pragmatic ambiguities and produce candidate disambiguated requirements that are relevant, clear, and consistent with the intended system functionality. Among the evaluated models, GPT-4o-mini achieved the highest macro-averaged recall (0.75) and F2 score (0.75) for pragmatic ambiguity detection. In the resolution task, GPT-4o-mini received the highest relevance scores from human evaluators, while Mistral-7B achieved the highest scores for clarity and consistency.

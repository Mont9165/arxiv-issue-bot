# Token-Efficient Data Reasoning Agents via Adaptive Structuring of Unstructured Data

- arXiv ID: `2608.31082v1`
- Authors: Milad Rezaei Hajidehi, Qitong Wang, Stratos Idreos
- Published: 2026-08-31
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.31082v1) | [pdf](https://arxiv.org/pdf/2608.31082v1)

## Abstract

Valuable data remains embedded in unstructured sources: web pages, reports, contracts, filings, earnings calls, and PDFs. The big bet in enterprise AI is deploying LLM agents that reason over this data to answer complex questions for every knowledge worker. Agents can do this today, but at prohibitive cost. Each question repeatedly opens large documents to recover scattered evidence, consuming up to a million tokens. However, if the data were already structured, the same question would reduce to a cheap database lookup. For example, on FanOutQA benchmark, reasoning over an ideal pre-structured store is 28X cheaper, and the gap grows to orders of magnitude as questions fan out over more documents. Yet structuring everything in advance is not viable: documents hold vastly more possible structure than any workload will use, and the useful structure and documents are unknown until queries arrive. We propose agentic data cracking, a method that structures unstructured data adaptively and speculatively as a byproduct of reasoning itself. Structuring is adaptive because observed queries decide when it happens and what matters, and speculative because it goes beyond the current question. Whenever the agent opens a document to answer, a cracking sub-agent forks from the already-loaded context at marginal cost and extracts grounded structure likely to serve related future queries. Over time, an increasing share of queries is fully covered by structured data and answered without opening a document, keeping agentic accuracy at close to RAG cost. On FanOutQA, extended with merely one related question per test question, cracking cuts cost by 53% while preserving accuracy. Agentic data cracking is a first step toward next-generation data infrastructure for agentic reasoning over unstructured data: a shared substrate beneath the model where knowledge that reasoning already paid to uncover accumulates.

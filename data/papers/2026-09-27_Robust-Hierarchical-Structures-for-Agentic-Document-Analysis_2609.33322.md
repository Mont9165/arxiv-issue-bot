# Robust Hierarchical Structures for Agentic Document Analysis

- arXiv ID: `2609.33322v1`
- Authors: Ruiying Ma, Yiming Lin, Aditya G. Parameswaran
- Published: 2026-09-27
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.CL`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2609.33322v1) | [pdf](https://arxiv.org/pdf/2609.33322v1)

## Abstract

Large Language Models (LLMs) enable us to better understand text documents, including PDFs and Word documents. However, LLMs, as well as more modern LLM agents, i.e., those with tool-calling abilities, typically treat such documents as plain text, ignoring the fact that they are often organized hierarchically into sections and subsections. Extracting this structure, while difficult, can improve efficiency and effectiveness for agents (and humans)---since only sections relevant to a given task need to be processed. Unfortunately, prior work on structure extraction provides no formal guarantees on how well the inferred structure matches the true one. Instead, we target a robust and compact variant that is feasible to infer and useful in practice. Robustness ensures that the text under each subsection header is a superset of the text under the same header in the true structure. Compactness seeks to minimize this superset, reducing agentic cost (or human cognitive load). We propose SHED, a two-stage workflow for inferring a robust and compact structure. The first stage is pluggable with an infinite family of approaches, each guaranteeing robustness for a specific document class. We theoretically characterize the document space using these classes and their hierarchical relationships. Empirically, SHED improves F-1 scores (measuring the robustness--compactness trade-off) by 13%--68% over non-LLM baselines and 9%--15% over expensive LLM-based approaches. Finally, we show how SHED-inferred structures are valuable for agentic document analysis: agents using SHED outperform baselines, achieving 3%--23% higher accuracy while being up to 10x cheaper.

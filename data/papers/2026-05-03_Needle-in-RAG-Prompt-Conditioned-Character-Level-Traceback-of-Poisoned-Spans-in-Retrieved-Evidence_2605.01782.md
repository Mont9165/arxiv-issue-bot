# Needle-in-RAG: Prompt-Conditioned Character-Level Traceback of Poisoned Spans in Retrieved Evidence

- arXiv ID: `2605.01782v1`
- Authors: Huining Cui, Wei Liu
- Published: 2026-05-03
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.01782v1) | [pdf](https://arxiv.org/pdf/2605.01782v1)

## Abstract

Retrieval-augmented generation (RAG) improves factual grounding by conditioning large language models on retrieved evidence, but it also opens a data-layer attack surface: poisoned corpus entries can steer outputs without changing model parameters. Existing defenses and traceback methods are largely passage-level, which is too coarse for modern attacks whose effective payload may be a short fabricated claim, trigger phrase, or hidden instruction embedded inside an otherwise benign chunk. We study black-box character-level poison traceback in RAG and present RAGCharacter, a two-pass forensic framework that localizes the responsible retrieved span for a concrete misgeneration event. Pass-0 runs standard RAG while logging a prompt-anchored execution trace. Pass-1 re-enters a triggered trace and performs event-conditioned traceback over prompt-used evidence via budgeted counterfactual masking and replay, yielding an attribution span for forensic reporting and a causal span under the logged trace. We further introduce an evaluation protocol that measures both event-level chunk traceback and character-level localization fidelity. Across two QA corpora, five poisoning attack families, six target LLMs, and multiple passage- and character-level baselines, RAGCharacter achieves the best overall trade-off within our benchmark between localization accuracy and low over-attribution. These results suggest that prompt-conditioned, black-box character-level traceback can be feasible, moving RAG forensics from document-level suspicion toward finer-grained evidence auditing and potential remediation.

# Runtime Compliance Verification for AI Agents

- arXiv ID: `2606.19242v1`
- Authors: Nafiseh Kahani, Masoud Barati, Diana Addae
- Published: 2026-06-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.19242v1) | [pdf](https://arxiv.org/pdf/2606.19242v1)

## Abstract

AI agents now handle personal data through tool use, function calls, and multi turn dialogue, which can create obligations under the General Data Protection Regulation (GDPR). Current testing practices mainly rely on offline red teaming or static prompt review, but they do not guarantee at runtime that agent behavior follows regulatory rules. We propose C-Trace (Compliance Trace based Runtime Agent Conformance Enforcement), a verification framework that: (i) expresses a subset of GDPR requirements, including consent, purpose limitation, data minimization, and the right to erasure, as formal policy predicates over agent execution traces; (ii) uses a runtime monitor that intercepts every tool invocation and model output and rejects non-compliant actions; and (iii) tests the agent with attack dialogues, including DSPy generated prompts and verbatim prompts from red teaming corpora, that try to induce violations. We evaluate the framework on four case studies reframed to GDPR. Under 10 percent per-category extractor noise, including drop-out and over-typing, the monitor keeps the attack success rate at less than or equal to 12 percent, below the baselines we compare against, and false positives at less than or equal to 16 percent, and reaches 0 percent ASR under perfect extraction.

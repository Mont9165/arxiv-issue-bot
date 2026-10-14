# From Safety Documentation to Safety Knowledge Support: An Evidence-Grounded LLM Framework for Medical Devices

- arXiv ID: `2608.12025v1`
- Authors: Tuhinangshu Gangopadhyay, Rasmus Adler, Peter Liggesmeyer, Jan Reich
- Published: 2026-08-12
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.12025v1) | [pdf](https://arxiv.org/pdf/2608.12025v1)

## Abstract

Medical devices are becoming more software-intensive, connected, and AI-enabled. Their development requires risk-management evidence aligned with ISO 14971 and, for software, IEC 62304. This evidence must be kept consistent across requirements, design decisions, software changes, verification results, complaints, and post-market data. These tasks are costly and depend on scarce safety and domain experts.
  Large language models (LLMs) may reduce parts of this effort because medical-device safety work is highly document-based. However, current LLM-based safety-engineering studies often address isolated methods, rely on generic prompting or public examples, and provide limited support for source links, traceability, uncertainty handling, lifecycle updates, and recorded expert review. This limits their use in regulated medical-device development.
  This paper argues that the central research problem is not safety-text generation, but source-linked safety-knowledge support. We propose an evidence-grounded framework that connects device artifacts, controlled knowledge storage and retrieval, method-specific generation of candidate safety items, critique and uncertainty checks, and recorded expert review. The framework prepares, links, checks, and updates candidate safety artifacts for expert decision-making. It does not decide whether a device is safe and does not provide regulatory approval. We also outline an evaluation strategy using non-public or newly built medical-device case studies and expert reference analyses to assess coverage, correctness, relevance, traceability, duplicate rate, unsupported claims, and review effort.

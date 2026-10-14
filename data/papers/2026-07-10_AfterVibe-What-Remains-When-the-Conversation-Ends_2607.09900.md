# AfterVibe: What Remains When the Conversation Ends

- arXiv ID: `2607.09900v1`
- Authors: Matteo Paltenghi, Satish Chandra
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.09900v1) | [pdf](https://arxiv.org/pdf/2607.09900v1)

## Abstract

We present AfterVibe, a framework that recovers natural-language specifications from a vibe coding session. Given a code artifact and the conversation trajectory that produced it, AfterVibe uses an LLM to extract an abstract natural-language specification capturing the developer's intent, and validates it through a regeneration test: a second, blind AI agent re-implements the artifact from the spec alone, and the resulting code is graded against the original through a multi-tier validation pipeline. Spec quality is thus measured by whether an agent can regenerate passing code; if the verifiers deem the implementations equivalent the spec is considered strong, otherwise it is iteratively refined. Evaluating AfterVibe on 72 real-world vibe-coded projects from a company's internal coding sessions, we find that its recovered specs are abstract by design-capturing behavioral intent without dictating implementation-yet strong. Multiple independent regenerations achieve a high mean regeneration score of 5.06 out of 6.0 while remaining diverse in their details, confirming that the spec constrains what without over-prescribing how. Besides outperforming existing human-authored descriptions, the specs can be further strengthened iteratively to a score of 5.74. A practical implication is that specifications-not code-could become the primary artifact for human review and the source of record at a time when AI-generated code is outpacing customary code review.

# Line-Anchored Feedback Cuts Token Costs and Improves Correctness in AI Code Editing

- arXiv ID: `2607.12713v1`
- Authors: William Franz Lamberti
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.12713v1) | [pdf](https://arxiv.org/pdf/2607.12713v1)

## Abstract

Generated tokens are a direct driver of the cost, latency, and energy of generative AI (GAI) code editing. We show the format of feedback is a lever on all three. We compare two deliveries of the same requested changes: a holistic prompt (control) versus the structured, line-anchored export of FileMark (treatment). FileMark is a VSCodium extension for inline comments on any file. In a paired experiment line anchoring cut generated tokens by 22% (Claude Opus) and 58% (Claude Sonnet), reaching 24%-80% on files of 100 lines or more, with four of seven models generating significantly fewer tokens after multiple-testing correction. Correctness rose where models had headroom: +2.0 points pooled and +5 to +7 points for three of five local models. An exploratory experiment in which the harness, not the GAI model, applies function-level patches shows the correctness benefit grows further when the edit-application burden is lifted: local-model correctness on 100+ line files roughly triples under anchoring. Line-anchored feedback reduces what stronger models spend and improves what weaker models get right.

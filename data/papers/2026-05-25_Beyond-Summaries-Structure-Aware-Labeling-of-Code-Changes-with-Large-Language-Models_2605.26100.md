# Beyond Summaries: Structure-Aware Labeling of Code Changes with Large Language Models

- arXiv ID: `2605.26100v1`
- Authors: Bar Weiss, Antonio Abu-Nassar, Adi Sosnovich, Karen Yorav
- Published: 2026-05-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.26100v1) | [pdf](https://arxiv.org/pdf/2605.26100v1)

## Abstract

Code review is a critical practice in software engineering, yet the growing scale and frequency of code patches in modern projects, together with the widespread adoption of AI code assistants, make manual review increasingly challenging. Identifying the types of changes within a patch, such as renames, moves, or logic modifications, can substantially improve review efficiency by enabling prioritization, filtering, and automation. However, existing LLM-based approaches to code review have largely focused on summarization and comment generation, leaving structured code reviews underexplored. In this paper, we present a systematic study of using large language models (LLMs) for taxonomy-based labeling of code changes in a code patch. We introduce a two-stage pipeline that assigns labels to diff hunks and then refines them to capture structural relationships and semantic attributes, such as rename propagation and type changes. Our approach employs few-shot prompting to produce language-agnostic and customizable labels, without the engineering overhead of traditional static-analysis pipelines. We evaluate four LLMs across multiple context configurations on a manually curated benchmark of natural and synthetic patches. Our best configuration achieves up to $84\%$ recall and $81\%$ precision, with high accuracy in extracting relational and attribute metadata. These results suggest that LLM-based labeling can effectively complement static analysis by enabling flexible, multilingual, and automation-friendly code review workflows.

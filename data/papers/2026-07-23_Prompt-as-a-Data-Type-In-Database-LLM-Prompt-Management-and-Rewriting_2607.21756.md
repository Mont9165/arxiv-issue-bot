# Prompt as a Data Type: In-Database LLM Prompt Management and Rewriting

- arXiv ID: `2607.21756v1`
- Authors: Denis Mayr Lima Martins, Gottfried Vossen
- Published: 2026-07-23
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.21756v1) | [pdf](https://arxiv.org/pdf/2607.21756v1)

## Abstract

Large Language Models (LLMs) are increasingly used in database-backed applications to classify tuples, filter records using semantic predicates, extract structured attributes, and enrich query results. Yet the prompt that start these computations are typically stored outside the DBMS in unstructured formats, making them invisible to query execution, metadata management, and optimization. Drawing on Stonebraker's QUEL as a Data Type and the principles of reflective programming, this paper introduces PromptDB, a database system that treats prompts as tuple-level database values. PromptDB provides a logical PROMPT datatype whose values store a template, bindings to tuple attributes, model metadata, and task metadata. Relations may contain PROMPT attributes directly in base tables, or expose them through views over joined tuples. Users query prompt-valued attributes through generated evaluation views, while the system internally renders, rewrites, optimizes, and executes prompts through an EVAL operator. Making prompts database-visible creates a new optimization space. The key idea is to bring query-optimizer thinking to prompts: just as query optimizers exploit database metadata to rewrite SQL plans, PromptDB exploits database metadata to rewrite prompts. We evaluate PromptDB on synthetic and real-world data workloads across different tasks. The results show how database-guided rewriting improves output validity and yields favorable cost-quality trade-offs compared with static, manually written prompts.

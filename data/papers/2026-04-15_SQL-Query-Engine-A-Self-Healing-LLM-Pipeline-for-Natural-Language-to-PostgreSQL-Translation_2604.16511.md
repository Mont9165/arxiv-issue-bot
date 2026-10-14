# SQL Query Engine: A Self-Healing LLM Pipeline for Natural Language to PostgreSQL Translation

- arXiv ID: `2604.16511v1`
- Authors: Muhammad Adeel Ijaz
- Published: 2026-04-15
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2604.16511v1) | [pdf](https://arxiv.org/pdf/2604.16511v1)

## Abstract

We present SQL Query Engine, an open-source, self-hosted service that translates natural language questions into validated PostgreSQL queries through a two-stage LLM pipeline. The first stage performs automatic schema introspection and SQL generation; a multi-strategy response parser extracts SQL from any LLM output format (JSON, code blocks, or raw text) without requiring structured output APIs. The second stage executes the query against PostgreSQL and, upon failure or empty results, enters an iterative self-healing loop in which the LLM diagnoses the error using full SQLSTATE codes and PostgreSQL diagnostic messages. Two mechanisms prevent regressions: early-accept returns successful queries immediately without LLM re-evaluation, and best-result tracking preserves the best partial result across retries. Schema context is cached per session in Redis, progress events stream via Redis Pub/Sub and SSE, and an OpenAI-compatible /v1/chat/completions endpoint lets existing tools work without modification. All database connections are read-only at the driver level. We evaluate across five LLM backends on a synthetic benchmark (75 questions, three databases) where the self-healing loop yields up to +9.3pp accuracy gains with zero regressions on the best model (Llama 4 Scout 17B, 57.3%), and on BIRD (437 questions, 11 databases migrated from SQLite to PostgreSQL) where the full pipeline reaches 49.0% execution accuracy (GPT-OSS-120B, +4.6pp). Source code: https://github.com/codeadeel/sqlqueryengine.

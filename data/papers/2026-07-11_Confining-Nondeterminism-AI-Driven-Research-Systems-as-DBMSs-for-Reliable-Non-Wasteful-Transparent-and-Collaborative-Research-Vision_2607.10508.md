# Confining Nondeterminism: AI-Driven Research Systems as DBMSs for Reliable, Non-Wasteful, Transparent, and Collaborative Research [Vision]

- arXiv ID: `2607.10508v1`
- Authors: Kyoungmin Kim, Anastasia Ailamaki
- Published: 2026-07-11
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.10508v1) | [pdf](https://arxiv.org/pdf/2607.10508v1)

## Abstract

LLM agents that conduct research (proposing ideas, writing and running code, analyzing results) can already carry a study from research question to figures, yet cannot be fully trusted. The same question asked twice in a row returns different answers; the agent announces a number that no execution produced, and tool use does not prevent this, because nothing binds what the agent reports to what its tools returned; a small upstream change leaves downstream results silently stale, with no way to list which ones; and the agent re-runs preprocessing and rewrites code it has already produced. We argue these failures share one root: every step of today's agent loop is a stochastic LLM call whose internal state nobody, including the agent, can check. Rather than trying to see inside the LLM, we take a lesson from databases, which earn trust without being watched, because deterministic operators over well-defined state make their guarantees hold by construction. We propose organizing a research project the same way. The project lives in a deterministic, versioned dataflow engine (in effect, a query plan over materialized views), and the LLM, together with the user, is a stochastic compiler that may only edit that plan. The executor never calls the LLM; LLM output enters only as versioned code and data that the executor then runs, and any asserted result enters the record only with an execution behind it. Five design rules at this boundary turn familiar database machinery, from versioning and provenance to incremental maintenance and cost-based scheduling, into guarantees that make research reliable, non-wasteful, transparent, and collaborative. This report presents the diagnosis, the requirements, and the design; the guarantee walkthrough, a prototype, and the research agenda appear in the full version, in preparation. The LLM, we argue, should be the query compiler, never the executor.

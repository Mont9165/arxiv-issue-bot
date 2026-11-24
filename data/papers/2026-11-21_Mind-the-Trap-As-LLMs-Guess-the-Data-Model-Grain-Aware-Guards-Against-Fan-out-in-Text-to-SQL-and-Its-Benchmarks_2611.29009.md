# Mind the Trap As LLMs Guess the Data Model: Grain-Aware Guards Against Fan-out in Text-to-SQL and Its Benchmarks

- arXiv ID: `2611.29009v1`
- Authors: Ahmed M. Mahran
- Published: 2026-11-21
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2611.29009v1) | [pdf](https://arxiv.org/pdf/2611.29009v1)

## Abstract

Text-to-SQL systems built on large language models (LLMs) often aggregate over one-to-many and many-to-many joins, a classic trap: when the joined rows repeat an entity, a SUM or COUNT counts it more than once, yet the query runs and returns a plausible number. We characterize these fan-out errors by one condition on the relation an aggregate reads, which depends on two facts a schema does not show: each measure's grain, and how many rows a join on each key repeats. An audit that tests the condition on the data finds distorted gold answers for 4.2% of the dev questions of BIRD, a widely used benchmark, and BIRD's later, independent revision changed 44% of the answers the audit flags as definite fan-out, against 16% of unflagged ones. We release BIRD-FanOut, 486 BIRD questions with reviewed gold, and GrainTraps, synthetic questions that set this trap and related ones. Across eight LLM agents, functional dependencies (FDs) computed from the data help no more than per-column statistics on GrainTraps, but grain-aware FDs, which also state each measure's grain and the repetition per key, cut fan-out errors on BIRD from 18.4% of runs to about 13%, also on held-out questions and without LLM judges. Accuracy rises less, because most remaining errors are not fan-out and BIRD's hints often prescribe the over-count. Text-to-SQL models should be given the grain of the data, and benchmark gold should be audited on the data. Code, data and benchmarks are available at https://github.com/ahmed-mahran/misqal

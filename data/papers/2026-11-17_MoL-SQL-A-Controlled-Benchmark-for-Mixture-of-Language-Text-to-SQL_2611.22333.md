# MoL-SQL: A Controlled Benchmark for Mixture-of-Language Text-to-SQL

- arXiv ID: `2611.22333v1`
- Authors: Tianqi Luo, Boyan Li, Yuyu Luo
- Published: 2026-11-17
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.22333v1) | [pdf](https://arxiv.org/pdf/2611.22333v1)

## Abstract

Text-to-SQL systems are usually built and evaluated under a monolingual assumption, yet in international applications users often query databases stored in a different language. Existing multilingual benchmarks mostly translate only the question without aligning schema and value entities, so they can neither locate the source of an accuracy drop nor rule out translation errors. Hence, we introduce MoL-SQL, a benchmark for mixture-of-language Text-to-SQL that switches the languages of the question, schema, and stored values independently while keeping each task fixed, and grades every cross-lingual entity mapping into four difficulty levels. We migrate five Text-to-SQL benchmarks of different domains and source languages through a unified alignment pipeline that builds a shared cross-lingual entity map, migrates each database with its constraints, rewrites the gold SQL under execution-equivalence checks, and regenerates the question from the verified SQL, keeping all language versions of a task aligned in entities, intent, and execution result. MoL-SQL provides two splits: MoL-Full (16,892 samples) for overall evaluation and MoL-Cube (3,840 samples) covering every language combination to isolate question, schema, and value effects. Experiments with eight LLMs and four families of Text-to-SQL methods show that schema and value languages have distinct effects, with stored values costing up to 23 points, and that these effects mainly stem from cross-lingual entity mapping. Neither question translation nor additional reasoning narrows the value gap, whereas access to target-database values substantially reduces it, indicating that mixture-of-language Text-to-SQL benefits most from language-aware context grounding.

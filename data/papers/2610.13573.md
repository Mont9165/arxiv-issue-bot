# MatQuery: Execution-Grounded Natural-Language Querying over Heterogeneous Materials Databases

- arXiv ID: `2610.13573v1`
- Authors: Chen Jason Zhang, Qi Chen
- Published: 2026-10-09
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.13573v1) | [pdf](https://arxiv.org/pdf/2610.13573v1)

## Abstract

Materials scientists increasingly combine information from several public databases, each with its own interface, schema, units and calculation conventions. MatQuery is a prototype and experimental infrastructure for studying how a natural-language request can be turned into queries over such databases and how the returned values can be interpreted. This report describes what has been built and the preliminary results obtained so far. The prototype holds frozen, self-verifying local copies of six public materials databases (about 10,000 records each), a catalog of declared fields derived from them, a database-independent query representation with an adapter for each database, and an eight-step pipeline in which a language model proposes and deterministic program steps check, execute and assemble. A benchmark generator produces questions whose reference queries are verified by execution on the frozen copies and whose wording is checked by back-translation and review. An evaluation harness runs direct prompting, CHESS and Alpha-SQL on the same frozen basis. Preliminary experiments on an 800-question development set show that direct generation with three demonstrations reaches 82.4% strict execution accuracy (56.5% without demonstrations), that a low-cost scorer selects the exact set of databases for 85.0% of complete requests with well-calibrated probabilities, and that band gaps differ by more than 0.5 eV in 31.6% of composition-matched cross-database clusters. Two pilots show the limits of the current approach: a probe-then-ask policy gave answers rated valid by both reviewers in only 11 of 50 sessions, and only 115 of 300 sampled record pairs could be compared by structure. The complete pipeline is in smoke testing and has not yet been evaluated at scale.

# Same Pattern, Different Answer: A Reference Semantics and Divergence Map for GQL and SQL/PGQ Path Patterns

- arXiv ID: `2609.23032v1`
- Authors: Madhulatha Mandarapu, Sandeep Kunkunuru
- Published: 2026-09-19
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2609.23032v1) | [pdf](https://arxiv.org/pdf/2609.23032v1)

## Abstract

GQL (ISO/IEC 39075:2024) is the first international standard for a graph query language, and SQL/PGQ (ISO/IEC 9075-16:2023) embeds the same pattern-matching core, GPML, in SQL. Both fix a precise semantics for path patterns: four path modes, four selectors, quantified segments. What engines compute for those patterns has never been measured. Work on GQL is theoretical and runs no engine; cross-engine work measures performance and normalises the semantics away. We build an executable reference semantics for the GPML path core and gate it against the six worked answers printed in the standard's own reference exposition. We then run a 17-construct suite against six releases of five products - Kuzu, DuckPGQ, Neo4j at 5.26 and 2026.04, Memgraph, Apache AGE - scoring each cell as conforming, diverging, rejected, or inexpressible in that dialect. Nine of seventeen constructs draw more than one answer across the engines that accepted them. Of 26 disagreements, 15 are silent - the query runs, returns a different multiset, raises no error - a silence ratio of 0.58. Scoring each divergence against the path mode each engine's manual declares separates language from implementation: 9 of 15 are documented differences, 6 are departures from the standard the engine implements. A metamorphic layer needing no reference semantics finds 39 self-consistency violations, yielding two minimal defects. No engine we measured parses the order the standard's own examples are written in, except the authors' own, which added it after this suite reported the gap. Suite, semantics, reproducers and results are open source.

# Rebuilding a Field's Open-Problem Catalog from the Literature: A Two-Layer Knowledge Graph, and Why Status Must Stay Proposed

- arXiv ID: `2610.39641v1`
- Authors: Madhulatha Mandarapu, Sandeep Kunkunuru
- Published: 2026-10-29
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.DL`
- Links: [abs](http://arxiv.org/abs/2610.39641v1) | [pdf](https://arxiv.org/pdf/2610.39641v1)

## Abstract

A research field records its open problems in surveys, keynotes and community reports. Those are prose, written every few years, and nobody can ask them who works on a problem now or whether it was settled last year. We argue the problems should be data, and we build the system that makes them so: a hand-curated problem layer carried in unchanged, under an evidence layer rebuilt from a bibliographic index, joined by typed, provenance-carrying links in one graph database and queryable from one language. A language model does four jobs -- per-paper extraction, catalog grounding, per-paper status verdict, and idea generation -- each constrained to a candidate set so out-of-set answers are refused rather than stored. We report a study on two curated catalogs, database research (1,053 problems) and AI research (1,000 problems), each with a prior catalog-only graph. The rebuilt graph answers every question the catalog-only graph answered -- 47 of 47 on databases, 34 of 35 on AI -- plus questions the catalog-only graph refused: recent workers, untouched problems, methods tried, and outside papers bearing on a problem (336 problems, 770 works on databases). The capability we most wanted does not survive its own audit. Of 41 solves and refutes verdicts hand-checked against the papers, 9 are correct, 30 partly correct and 2 wrong; no refutes verdict (0 of 34) disproves an open problem, and only 1 of 7 solves closes the central question. We report that failure in full and draw the design conclusion: a status change must be proposed with its evidence and never applied, making the human reviewer part of the architecture. We close with the data-engineering problems this raises: entity resolution across curated and harvested layers, verifying model status claims, freshness under source quotas, and evaluation without ground truth.

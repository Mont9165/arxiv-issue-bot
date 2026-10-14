# Teach Your DBMS to LIKE Strings: Fast and General Pattern Matching for Wildcard Joins and Filters

- arXiv ID: `2608.23307v1`
- Authors: Lam-Duy Nguyen, Pascal Ginter, Duc-Tam Nguyen, Thomas Neumann, Viktor Leis
- Published: 2026-08-24
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.23307v1) | [pdf](https://arxiv.org/pdf/2608.23307v1)

## Abstract

Nowadays, modern applications do more than just store text -- they need to derive meaningful insights from it. To do that, they usually rely on wildcard queries with LIKE predicate to extract patterns. However, modern database management systems (DBMSs) handle these wildcard operations poorly, resorting to nested loops for joins and expensive interpreted evaluation for filters. To address the former, we propose a new join algorithm based on the Aho-Corasick algorithm, which significantly reduces the time complexity. For wildcard filtering, we leverage the code-generation infrastructure to improve performance: we generate specialized code for the LIKE predicate, eliminating the overhead of interpreting the pattern per tuple. Our experimental results show that the new wildcard join algorithm significantly outperforms both baseline DuckDB and Umbra, achieving speedups of up to 30.6x and 114.75x, respectively. The new wildcard filter approach likewise outperforms both baselines, achieving a speedup of 13.3x in a filter-focused stress benchmark. We believe these two techniques will play key roles for high-performance text analytics in modern query engines.

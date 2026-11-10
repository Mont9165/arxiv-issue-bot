# Transactional Data Change for Real-Time Analytics in Lakehouses

- arXiv ID: `2611.12169v1`
- Authors: Dongyang Geng, Haoqiong Bian, Zinuo Li, Haoyue Li
- Published: 2026-11-09
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.DC`, `cs.PF`
- Links: [abs](http://arxiv.org/abs/2611.12169v1) | [pdf](https://arxiv.org/pdf/2611.12169v1)

## Abstract

Real-time data analytics has become a key demand for lakehouses. It requires propagating data changes from the data source to the lakehouse in real time, while ensuring ACID guarantees and minimizing resource consumption and impact on analytical query performance. This is highly challenging for a data system according to the RUM conjecture, especially given the read-optimized immutable file storage layer in lakehouses. Existing lakehouses offer only git-style catalog version control on a single table, and they trade data freshness, query performance, and/or resource efficiency to achieve a barely acceptable data-change throughput. In this paper, we propose a novel data synchronization framework, Retina, that enables real-time, cost-efficient, query-performant, and fully transactional data changes in lakehouses. We implement and open-source Retina. Evaluations show that Retina delivers 10-millisecond-level data freshness and over 3.2 million row/s linear-scalable data-change throughput with low resource consumption and query-performance overhead, significantly outperforming state-of-the-art lakehouse systems and lake-compatible HTAP databases.

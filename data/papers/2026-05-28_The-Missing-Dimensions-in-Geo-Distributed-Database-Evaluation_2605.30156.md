# The Missing Dimensions in Geo-Distributed Database Evaluation

- arXiv ID: `2605.30156v1`
- Authors: Oto Mraz, Kyriakos Psarakis, George Christodoulou, Paris Carbone, Asterios Katsifodimos
- Published: 2026-05-28
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.30156v1) | [pdf](https://arxiv.org/pdf/2605.30156v1)

## Abstract

Geo-distributed OLTP databases are widely deployed across cloud regions, yet current evaluation practices do not cover the challenges of this aspect. Existing benchmarks assume stable network conditions; they lack explicit settings for data and client locality, and they largely ignore data transfer costs across regions. In addition, most evaluations rely on a limited set of geo-distribution patterns. In this paper, we propose Gaia, a comprehensive evaluation framework that addresses these gaps. We use Gaia to perform a comprehensive evaluation of existing geo-distributed OLTP systems. We deploy them across multiple cloud regions, using different geo-distribution patterns and variable cross-region network conditions. Among other interesting findings, our framework reveals that: i) most systems are sensitive to network instabilities, ii) network costs dominate cloud deployment expenses iii) multi-region fault-tolerance mechanisms incur measurable critical-path overhead that is often overlooked in prior evaluations. We argue that for the design of future geo-distributed databases, we must rethink the trade-offs between performance, fault-tolerance, and cost.

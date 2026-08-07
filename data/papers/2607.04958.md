# Look-Ahead-Freedom as Temporal Non-Interference: A Verifiable Correctness Property for Backtesting and Agentic Trading Pipelines

- arXiv ID: `2607.04958v1`
- Authors: Xavier Fonseca
- Published: 2026-07-06
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.LO`, `cs.PL`, `cs.SE`, `q-fin.PM`
- Links: [abs](http://arxiv.org/abs/2607.04958v1) | [pdf](https://arxiv.org/pdf/2607.04958v1)

## Abstract

Look-ahead bias (using information from after a decision epoch to make the decision at that epoch) is the dominant way a backtest or a machine-learning evaluation flatters a system that will disappoint in deployment. The field manages it with construct-specific recipes and empirical detectors, which are sound only channel by channel and certify nothing by their silence. We show that look-ahead-freedom is a formal property in disguise: fixing an epoch, the demand that the future not influence the present is temporal non-interference over a time-indexed information lattice. From this identification we develop a pipeline calculus separating a datum's availability from its reference time, and settle the problem's boundary. Where availability may depend on data values, look-ahead-freedom is undecidable (indeed Pi-0-1-hard): leakage is recursively enumerable but freedom is not. On the value-independent fragment (covering windowing, resampling, joins, point-in-time and vintage reads, and agentic retrieval) we give a type-and-effect system that is sound and decidable in linear time. An artifact confirms the theory: the check scales linearly, an independent oracle witnesses no leak in any accepted pipeline, and the checker catches every planted leak that differential and tiling detectors miss.

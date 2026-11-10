# LoStBench: Benchmarking Longitudinal Studies Data Integration

- arXiv ID: `2611.10242v1`
- Authors: Pratik Pokharel, Oliver Kennedy, Abhi Ramtel, Poonam Kumari, Jeff Good, Katarzyna Kordas, Marianthi Markatou, Andrew Talal
- Published: 2026-11-06
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.10242v1) | [pdf](https://arxiv.org/pdf/2611.10242v1)

## Abstract

A longitudinal study observes the same subjects or variables, repeatedly over an extended period of time, allowing researchers to examine changes, trends, and relationships as they develop. Such studies typically evolve over their life cycles, as improved understanding of the study's domain, or external factors trigger the need for revisions. The resulting heterogeneity among collected data must be resolved before the survey's results may be analyzed. Although this problem is a form of schema matching, it is a form of schema matching that differs significantly from prior workloads explored by the database community. For instance, rather than the short attribute names and data instances that many schema matching tools rely on, a stronger signal in longitudinal studies arises from longer prose questions that these tools are less equipped to handle.
  This paper documents the joint efforts of a team of computer scientists and domain experts to adapt existing schema matching algorithms to our new use case of longitudinal data integration. We present a case study in the context of a representative workload: The American National Election Studies (ANES) dataset, a nearly eight-decade survey with publicly available data and a canonical domain-expert curated schema matching. Using ANES, we develop LoStBench (Longitudinal Studies Benchmark for data integration), a medium-scale, subject-matter-expert-annotated benchmark. Using LoStBench, we conduct a comprehensive empirical study evaluating state-of-the-art schema matching algorithms, and expose limitations of these algorithms when applied in the context of longitudinal studies. We propose improvements that address some of these limitations, and identify key challenges to motivate future data integration work to address the others.

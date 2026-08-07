# Model-Driven Discipline for Multi-Agent LLMs: Requirement-to-Verification Generation of Traceable System Models

- arXiv ID: `2607.16708v1`
- Authors: Ran Wei, Le Zhu, Haochi Wang, Ruizhe Yang, Jiapeng Guan, Siyuan Ji, Yuchen Hu, Zhe Jiang, Xiangyang Ji
- Published: 2026-07-18
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.16708v1) | [pdf](https://arxiv.org/pdf/2607.16708v1)

## Abstract

Software complexity is a long-standing challenge for system engineers. Model-Driven Engineering (MDE) addresses it by treating models as first-class artefacts, but a typical MDE process spans many tools and produces heterogeneous models of different system aspects, making traceability, maintenance, and change management difficult.
  We propose RADIANT, an engineering methodology that combines MDE with Multi-Agent Large Language Models (LLMs) for complete model-based system development, with a focus on safety-critical systems. From a carefully specified requirement model, RADIANT automatically generates heterogeneous models across engineering phases -- a concept model, a domain-specific modelling language, a conforming system model, and a behaviour model -- together with executable, element-level traceability links, on top of which it provides exact, automated change-impact analysis. Generated behaviour models are translated into CSP and formally verified (e.g.\ for deadlock freedom and convergence) with a counterexample-driven repair loop. Evaluating RADIANT across three LLMs, we find that the multi-agent decomposition reliably improves the \emph{syntactic validity} of the generated formal artefacts over a single-agent baseline -- and their \emph{executability} where the model's code generation permits -- while gains in semantic accuracy are model-dependent. A six-participant study shows an order-of-magnitude ($10$--$15\times$) reduction in development time, and the unmodified pipeline transfers to a second domain.

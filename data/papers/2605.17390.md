# NOETHER: A Constructive Framework for Metamorphic Pattern Discovery from Operator Algebras

- arXiv ID: `2605.17390v1`
- Authors: Meng Li, Xiaohua Yang, Jie Liu, Shiyu Yan
- Published: 2026-05-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2605.17390v1) | [pdf](https://arxiv.org/pdf/2605.17390v1)

## Abstract

Context. Metamorphic Testing is recognised in IEEE/ISO software-testing standards and increasingly recommended for AI systems, but its progress is bottlenecked by metamorphic relation (MR) identification: existing approaches (structured frameworks, mining and evolutionary pipelines, LLM-assisted methods, MetaPattern catalogues) share an inductive grounding that leaves three foundational questions open: origin, closure, and transferability.
  Objective. We propose a framework whose downstream step from program-induced operator algebra to MetaPattern set is mechanical and provable, while the upstream curation of the algebra is a stated empirical hypothesis with explicit scope precondition.
  Method. NOETHER is a two-layer framework. The upstream layer is an eight-block decomposition over recurrent mathematical structures (symmetry, order, self-adjoint, time-reversal, limit, qualitative-dynamics, method-comparison, relational equivalence). The downstream CONSTRUCT-MP algorithm produces a MetaPattern set with algebraic-closure (Theorem 1) and polynomial-time decidability (Theorem 2) guarantees. We test the framework on three operator-algebraic domains.
  Results. On Boltzmann reactor physics NOETHER systematises a prior inductive catalogue; on equivariant ML it derives executable MRs for rotation invariance, adjoint duality, and training-trajectory reversibility; on relational query optimisers it exercises the relational-equivalence block. The central falsifiable prediction (L*-blindness on homogeneity-preserving mutators) holds on the in-scope substrate. The absolute-completeness conjecture (Theorem 1') is falsified on PWR core diffusion via two pairwise-independent counterexamples that identify five Translate-extension dimensions.
  Conclusion. Induction is relocated from per-program MR sampling to a per-domain algebraic layer; the downstream step is deductive and mechanical.

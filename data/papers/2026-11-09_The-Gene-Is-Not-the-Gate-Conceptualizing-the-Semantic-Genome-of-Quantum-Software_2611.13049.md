# The Gene Is Not the Gate: Conceptualizing the Semantic Genome of Quantum Software

- arXiv ID: `2611.13049v1`
- Authors: Jiongchi Yu, Yue Duan, Ziming Zhao, Xiaofei Yue, Zhaoxuan Li
- Published: 2026-11-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.13049v1) | [pdf](https://arxiv.org/pdf/2611.13049v1)

## Abstract

Quantum software spans applications, program representations, compilers, runtimes, and hardware-facing control. Existing abstractions describe these artifacts and layers, but they do not capture the semantic responsibilities that must remain valid as a computation is transformed across the stack. This limits systematic reasoning about cross-layer correctness, evolution, and reuse.
  We present QGenome, a semantic foundation for quantum software genomics. We define a quantum software gene as a typed, reusable responsibility characterized by an explicit contract, execution context, concrete expressions, and supporting evidence. QGenome organizes genes across five software strata and ten responsibility families grouped into computational semantics, coordination, realization, and assurance. Typed genes compose into pathways and genomes through dependency, refinement, provenance, and phenotype relations, enabling responsibilities to be traced across alternative implementations and execution contexts.
  We illustrate the taxonomy using representative public artifacts across the quantum software stack and define principles for contextual validity, genome evolution, environmental adaptation, and capability expression. Rather than presenting a complete taxonomy or an automated extraction technique, QGenome establishes a falsifiable framework and a concrete research agenda for gene mining, lineage recovery, cross-layer regression testing and repair, and evidence-grounded quantum software agents.

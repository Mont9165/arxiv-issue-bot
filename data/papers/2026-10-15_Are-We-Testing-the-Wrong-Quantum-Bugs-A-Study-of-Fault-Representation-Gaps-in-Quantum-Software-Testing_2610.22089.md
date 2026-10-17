# Are We Testing the Wrong Quantum Bugs? A Study of Fault Representation Gaps in Quantum Software Testing

- arXiv ID: `2610.22089v1`
- Authors: Asif Mohammed Saad, Ahsanul Ameen Sabit, Jonah Brandenburgh, Jiyuan Wang, Qian Zhang, Soneya Binta Hossain
- Published: 2026-10-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2610.22089v1) | [pdf](https://arxiv.org/pdf/2610.22089v1)

## Abstract

Quantum software relies on compilers, intermediate representations, and execution frameworks that transform programs before execution. Faults in these components can change the behavior of otherwise correct quantum programs. Yet quantum testing techniques are often evaluated using mutation-generated faults and curated bug benchmarks. We investigate how well the faults represented by these artifacts reflect those encountered in modern quantum software. We audit four quantum mutation-testing tools and three curated bug benchmarks, and collect 410 verified bugs from ten quantum software repositories over two years. We classify faults from all three sources into a common taxonomy of 56 bug families and compare their representation across mutation operators, curated benchmarks, and recent real-world bugs. The mutation tools support 20 bug families, and curated benchmarks add 15 more. Yet only 56 of the 410 real-world bugs (13.7%) belong to families represented by either source; the remaining 354 (86.3%) belong to families absent from both. The largest unrepresented families concern compiler transformations (66 bugs), type handling (53), and input validation (47). Unlike local gate or statement changes, these faults often depend on intermediate representations, compiler pipelines, input types, or dependency versions. Existing mutation operators primarily modify circuits and program constructs, whereas many real-world faults arise in the compilers, representations, and framework interfaces that process them. Addressing this gap requires looking beyond circuit-level faults toward testing semantic preservation across compiler transformations, correctness at representation boundaries, and interactions between software components. Our study provides empirical evidence to guide fault models and benchmarks that capture these mechanisms and preserve the contexts needed to reproduce them.

# High-level quantum structured programs as quantum registers compositions

- arXiv ID: `2608.03873v1`
- Authors: David Chamizo, Jose Garcia-Alonso, Juan M. Murillo
- Published: 2026-08-04
- Primary category: `quant-ph`
- Categories: `quant-ph`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03873v1) | [pdf](https://arxiv.org/pdf/2608.03873v1)

## Abstract

Current quantum programs are mainly designed at the level of quantum gates acting on individual qubits; on a large scale and for complex problems this may involve a high cognitive load on the programmer, making the program specification nontrivial and error-prone. In this context, providing quantum programming with higher abstraction mechanisms will assist in making this task more manageable and robust against design errors. In this work, a conceptual framework is addressed following the notion of the whole quantum computation as a structure composed of quantum registers representing each an undivided entity. Thus, computation progresses through semantically well-defined transformations that act on, or entangle, quantum registers, thereby modifying the global state. Ultimately, the program reaches the desired state by following a specific composition strategy. With this in mind, high-level syntax is presented through an algebraic formalism that bridges them with their low-level semantics. Proposed syntax is based on certain well-know operations used on quantum algorithms that apply phase shifts upon logical condition satisfaction or leverage on parallel evaluation. Based solely on the formalized operations, a quantum satisfiability modulo theories (SMT) solver can be designed. At its core, this work contributes to establishing some methodological principles towards realizing a high-level quantum structured programming.

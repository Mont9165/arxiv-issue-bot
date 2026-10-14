# What Bugs Do Prolog Students Write? An Empirical Taxonomy and Data-Driven Mutation Framework

- arXiv ID: `2607.21193v1`
- Authors: Ricardo Brancas, Pedro Orvalho, Carolina Carreira, Vasco Manquinho, Ruben Martins
- Published: 2026-07-23
- Primary category: `cs.LO`
- Categories: `cs.LO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.21193v1) | [pdf](https://arxiv.org/pdf/2607.21193v1)

## Abstract

Automated feedback tools for logic programming education depend on realistic bug datasets that reflect the mistakes students actually make. However, existing mutation testing frameworks for Prolog treat all mutations as equally likely, producing synthetic faults that diverge from classroom reality. We present an empirical study of 7,201 Prolog submissions from 265 undergraduate students, from which we derive a fine-grained taxonomy of student bugs through manual classification of 200 bug-fixing submissions. Guided by this taxonomy, we develop LogMorph, a data-driven mutation tool whose 17 operators are weighted according to the observed error distribution. LogMorph enumerates valid mutation sites on the abstract syntax tree, samples operators proportionally, injects faults, delegating to an SMT-based synthesizer when new code fragments are needed, and validates each mutant against a reference test suite. An evaluation of 16,000 generated mutants shows that the synthetic error distribution closely matches the student distribution, with most bug categories agreeing to within two percentage points. We identify cut-related mutations and synthesizer-generated code as the main sources of residual divergence, and outline how combining the SMT back-end with a language model fine-tuned on student code can further improve realism.

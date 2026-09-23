# Modular Composition of Inductive Types Using Lean Meta-programming

- arXiv ID: `2609.25427v1`
- Authors: Ramy Shahin
- Published: 2026-09-21
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.LO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.25427v1) | [pdf](https://arxiv.org/pdf/2609.25427v1)

## Abstract

Inductive types are ubiquitous building blocks in many programming and theorem proving languages. An inductive type is a closed set of constructors from which values of the type can be created. That set cannot be extended though once a type is defined. This limits extensibility, reuse, and modular separation of concerns when defining types and functions operating over their values. This limitation is manifested in the expression problem, where extending an expression language with new syntactic constructors without having to modify or re-compile existing ones is a challenge in almost all programming languages.
  This paper presents inductive type and function implementation composition algorithms based on meta-programming. In addition, a set of syntactic extensions to the Lean proof assistant implementing those algorithms are presented. This framework allows for modular reuse, composition, and extension of a subset of Lean type and function definitions. In addition, semantic subtyping relations between component and composite types are discussed both at the type theoretic and implementation levels.
  The framework is demonstrated on a case study, involving the composition of syntactic and semantic artifacts of three sublanguages into one language. The case study highlights both the features and limitations of the composition framework.

# Stratified Negation in RDF Rules: A Correct Approach (Extended Version)

- arXiv ID: `2607.28778v1`
- Authors: Nils Küchenmeister, Alex Ivliev, Dörthe Arndt, Markus Krötzsch
- Published: 2026-07-30
- Primary category: `cs.LO`
- Categories: `cs.LO`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.28778v1) | [pdf](https://arxiv.org/pdf/2607.28778v1)

## Abstract

Combining RDF rule languages, such as N3 or SHACL Rules, with default negation is challenging. Existing methods to stratify negation often fail for RDF rules, since individual triples do not carry enough information to meaningfully restrict potential dependencies. Blank nodes in rule heads further complicate the matter, since the order of rule applications may determine whether new values are created, which in turn can change the applicability of rules with negation. To solve these open problems, we propose chain stratification as a robust new condition that guarantees a well-behaved semantics for RDF rules with negation, and existential rules in general. Our condition combines an elaborate analysis of potential multistep derivations with a mechanism for using integrity constraints to discard impossible cases. Applying rules in any order that respects chain stratification is guaranteed to derive an RDF graph that is unique, lean, and justified under the usual negation-as-failure semantics. To show the practicality, we also provide a prototype implementation.

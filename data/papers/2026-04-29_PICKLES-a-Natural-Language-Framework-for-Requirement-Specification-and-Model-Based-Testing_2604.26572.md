# PICKLES: a Natural Language Framework for Requirement Specification and Model-Based Testing

- arXiv ID: `2604.26572v1`
- Authors: María Belén Rodríguez, Petra van den Bos
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.26572v1) | [pdf](https://arxiv.org/pdf/2604.26572v1)

## Abstract

This paper combines methods from the fields of Model-Based Testing (MBT) and Behaviour-Driven Development (BDD) to define a testing approach with human-readable specifications and test cases, as in BDD, while using the modelling techniques and automatic test generation algorithms from MBT. We introduce PICKLES, a Precise Input and Control-flow Keyword-based Language for tEst Scenarios; an extension of Gherkin-style BDD scenarios, specified in structured natural language. We provide a bi-directional translation from Pickles scenarios to formal models, where both specifications and tests are human-readable, and a method to obtain a so-called master model combining all translated scenarios. Standard MBT algorithms can then be applied to automatically derive test cases from it. We implement a prototype of the translation and composition steps, which we use on an industrial case study: a software component from a traffic management system. With it, we illustrate the pipeline and show how Pickles can achieve significantly higher coverage with respect to BDD from the same set of scenarios.

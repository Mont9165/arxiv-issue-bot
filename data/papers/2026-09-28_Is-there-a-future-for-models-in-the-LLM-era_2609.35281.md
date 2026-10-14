# Is there a future for models in the LLM era?

- arXiv ID: `2609.35281v1`
- Authors: Marco Calamo, Massimo Mecella, Monique Snoeck
- Published: 2026-09-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.35281v1) | [pdf](https://arxiv.org/pdf/2609.35281v1)

## Abstract

In an era where software development is deeply tied with Large Language Models, does Model Driven Engineering (MDE) still make sense? This raises the question of the extent to which MDE can be successfully combined with an LLM approach to address the downsides of each approach separately. In this paper, we try to answer that question by investigating a central Research Question: Can Agents powered by Large Language Models improve code generated from UML diagrams and text specifications by Model Driven Engineering (MDE) tools? To investigate this problem, we developed a novel LLM-powered Multi-Agentic approach called ARTHUR (Architecture Refactoring Through Hybrid UML Reasoning), a framework that aims at combining the reliability of MDE and the ease of use of LLMs. ARTHUR is designed to refactor legacy Java code produced by traditional, rule-based, MDE code generators from UML diagrams. To asses the answer to our question, we have refactored the legacy code of several projects from our custom dataset crafted for this purpose. \name{} which made it possible to add support for modern frameworks like Spring Boot, while ensuring compliance with Model-Based Testing techniques to verify that the code still corresponds to the initial model's specifications. We then measured the results obtained in terms of time and cost, passing test rate, and \texttt{compile@k}, \texttt{pass@k} and \texttt{pass$^k$} metrics. We also observed the effect of generating code directly from the conceptual model without the refactoring. Our preliminary test results show that MDE could not be more far from retirement, after all.

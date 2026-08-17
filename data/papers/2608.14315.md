# Breaking Models to Test the Judge: A Mutation Testing Approach for Semantic Evaluators of Domain Class Diagrams

- arXiv ID: `2608.14315v1`
- Authors: Kevin Delcourt, Meriem Ben Chaaben, Abdelhamid Rouatbi, Luciano Marchezan, Houari Sahraoui
- Published: 2026-08-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.14315v1) | [pdf](https://arxiv.org/pdf/2608.14315v1)

## Abstract

In software engineering, many semantic modeling tasks lack a unique ground truth, as human judgments are both costly and subjective. This paper explores mutation testing as a scalable alternative for evaluating semantic judges (e.g., LLM-based) of models. We propose a mutation testing approach in which controlled semantic defects are injected into domain class diagrams. Starting from pairs of PlantUML class diagrams and textual system descriptions, we apply mutation operators (e.g., removing a class) to generate faulty variants. A candidate judge is then evaluated based on its ability to detect the injected defects. We define 11 mutation operators for the task of comparing a domain class diagram against a textual description and evaluate the proposed approach against a conventional manual assessment of judgment validity. Across six judge configurations (three LLMs and two prompt variants), the automated mutation testing approach is largely consistent with the manual assessment in identifying the better-performing configurations. The results suggest that mutation testing may serve as a scalable proxy for analyzing semantic judges.

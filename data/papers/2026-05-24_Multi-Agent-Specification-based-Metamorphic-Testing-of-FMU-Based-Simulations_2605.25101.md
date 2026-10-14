# Multi-Agent Specification-based Metamorphic Testing of FMU-Based Simulations

- arXiv ID: `2605.25101v1`
- Authors: Ashir Kulshreshtha, Abdullah Mughees, Gaadha Sudheerbabu, Tanwir Ahmad, Kristian Klemets, Dragos Truscan, Mikael Manngård
- Published: 2026-05-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `eess.SY`
- Links: [abs](http://arxiv.org/abs/2605.25101v1) | [pdf](https://arxiv.org/pdf/2605.25101v1)

## Abstract

In many industrial domains, the Functional Mock-up Interface (FMI) is used to exchange simulation models as Functional Mock-up Units (FMUs) across different partners using various modelling tools. This opens up the possibilities for simulation-based verification and validation using FMUs for ensuring reliable system behaviour. However, deriving effective test oracles for these simulation models remains challenging due to the absence of explicit expected outputs. This limits the applicability of conventional testing approaches, which require access to the internal workings of the systems. Metamorphic testing (MT) addresses this limitation by leveraging metamorphic relations (MRs), but extracting such relations from specifications remains largely a manual and error-prone process. To address this challenge, we propose an LLM-powered multi-agent workflow for specification-based metamorphic testing of FMU-based simulation models. The approach takes functional and interface specifications as input and orchestrates multiple agents to extract requirements and derive MRs. These MRs are expressed using Given-When-Then patterns to structure input conditions (Given), transformations (When), and expected output behaviours (Then). These relations are then used to generate metamorphic test cases, execute simulations, and evaluate output consistency across multiple sessions. We evaluate the approach on a Lube Oil Cooling system FMU, demonstrating its ability to automatically generate meaningful MRs and corresponding test cases. Preliminary results indicate that the proposed workflow can effectively support the systematic verification and validation of dynamic simulation models by reducing manual effort and improving test generation.

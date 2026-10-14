# Integration of an Agent Model into an Open Simulation Architecture for Scenario-Based Testing of Automated Vehicles

- arXiv ID: `2605.13539v1`
- Authors: Christian Geller, Daniel Becker, Jobst Beckmann, Lutz Eckstein
- Published: 2026-05-13
- Primary category: `cs.RO`
- Categories: `cs.RO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.13539v1) | [pdf](https://arxiv.org/pdf/2605.13539v1)

## Abstract

Simulative and scenario-based testing are crucial methods in the safety assurance for automated driving systems. To ensure that simulation results are reliable, the real world must be modeled with sufficient fidelity, including not only the static environment but also the surrounding traffic of a vehicle under test. Thus, the availability of traffic agent models is of common interest to model naturalistic and parameterizable behavior, similar to human drivers. The interchangeability of agent models across different simulation environments represents a major challenge and necessitates harmonization and standardization. To address this challenge, we present a standardized and modular simulation integration architecture that enables the tool-independent integration of traffic agent models. The architecture builds upon the Open Simulation Interface (OSI) as a structured message format and the Functional Mock-up Interface (FMI) for dynamic model exchange. Rather than introducing yet another model or simulation tool, we provide a reusable reference implementation that translates these standards into a practical integration blueprint, including clear interfaces, data mappings, and execution semantics. The generic nature of the architecture is demonstrated by integrating an exemplary agent model into three widely used simulation environments: OpenPASS, CARLA, and CarMaker. As part of the evaluation, we show that the model yields consistent behavior in all simulation platforms, thereby validating the interoperability, modularity, and standard compliance of the proposed architecture. The reference implementation lowers integration barriers, serves as a foundation for future research, and is made publicly available at github.com/ika-rwth-aachen/agent-model-integration

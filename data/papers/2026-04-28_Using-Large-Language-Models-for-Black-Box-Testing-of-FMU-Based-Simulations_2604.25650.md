# Using Large Language Models for Black-Box Testing of FMU-Based Simulations

- arXiv ID: `2604.25650v1`
- Authors: Abdullah Mughees, Gaadha Sudheerbabu, Tanwir Ahmad, Dragos Truscan, Mikael Manngård, Kristian Klemets
- Published: 2026-04-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `eess.SY`
- Links: [abs](http://arxiv.org/abs/2604.25650v1) | [pdf](https://arxiv.org/pdf/2604.25650v1)

## Abstract

We propose a human in the loop approach for black-box testing of Functional Mock-up Units (FMUs) using Large Language Models (LLMs). The goal is to reduce the manual effort in defining test scenarios for dynamic simulation models and to improve the interpretability of results. The approach takes the functional and interface specifications of an FMU as input, and prompts an LLM to generate structured scenario goals in Given-When-Then format that define the initial input conditions of the simulation, a possible change in those conditions, and the expected output behaviour of the system against those changes. The corresponding scenario plans specify input patterns and add assertion oracles that describe expected output patterns defined in scenario goals. The approach generates a complete input time series for the scenario plans, runs the FMU simulation, and evaluates assertions on the recorded outputs. It produces human-readable logs and plots that show statistics for each scenario with overlays, aggregate pass rates, and per-goal outcomes. The generated scenarios and results are stored for evaluation and later re-execution. We evaluate the approach on a Lube Oil Cooling system and discuss design choices that make the approach practical for everyday use. Results suggest that LLM-assisted scenario generation can facilitate automatic test design and verification of dynamic simulation models.

# Backtracking Agent Applications Security Incidents

- arXiv ID: `2611.26525v1`
- Authors: Yicheng Cai, Taegyu Kim, Peng Liu
- Published: 2026-11-19
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.26525v1) | [pdf](https://arxiv.org/pdf/2611.26525v1)

## Abstract

Agent applications are increasingly deployed, yet agent-specific attacks pose real threats to them. Upon a security incident, organizations backtrack to identify the CEP (compromise entry point), remediate the damage, and prevent its recurrence. The main artifacts available for backtracking are trajectory logs, which record agent functionalities, and source code; app(lication)-specific function call logs are often fairly limited. However, trajectory logs are at the agent functionality abstraction layer, while the CEP candidates are function calls at the app code execution layer. Due to this semantic gap, the analyst needs to manually inspect the relevant code for each CEP candidate to infer its corresponding agent functionality. In this work, we present Origin, a backtracking tool for the analyst to submit a small number of queries to identify CEPs that existing tools cannot provide. Our approach poses two challenges: (1) define the intermediate abstraction that captures the mapping relationships between the two semantic layers; (2) determine the region-to-variable mapping for constructing the cross-layer graph defined in the intermediate abstraction. Each region is a specific group of agent functionalities. Origin addresses the challenges by (1) the cross-layer dependency graph (CLDG) that connects region-inferred functions at the semantic level to the variables in the low-level taint propagation subgraph, plus the associated query language, and (2) the region inference algorithm. Case studies on five popular agent applications across eight attack incidents show that an analyst using Origin correctly identifies all the CEPs.

# Automated Vulnerability Injection in Smart Contracts Using Large Language Models

- arXiv ID: `2609.02624v1`
- Authors: Luca Migliaccio, Roberto Natella, Naghmeh Ivaki, Nuno Laranjeiro, Marco Vieira
- Published: 2026-09-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2609.02624v1) | [pdf](https://arxiv.org/pdf/2609.02624v1)

## Abstract

Assessing vulnerability detection tools for smart contracts requires datasets with known ground truth, yet such datasets are scarce and difficult to build by hand. We propose an approach that uses Large Language Models (LLMs) to automatically inject vulnerabilities into Solidity smart contracts, and demonstrate it in a case study targeting 49 vulnerability types from OpenSCV. Injected contracts are validated through a multi-step pipeline checking compilation, execution, business logic, and the presence of the intended vulnerability. Applied to real-world contracts from SmartBugs, LLMs generate nearly 1,000 candidate variants; after deduplication and validation, 32 confirmed vulnerable contracts spanning 25 vulnerability types survive (a 16.58% survival rate). Surviving contracts concentrate in structurally simpler targets and vulnerability types with localized syntactic patterns. We report practical challenges including LLMs' non-determinism and the difficulty of preserving contract semantics. We then use the validated contracts to assess three static analyzers, revealing complementary and incomplete coverage profiles. Results show that LLM-based vulnerability injection is feasible, while exposing key limitations in scalability and diversity.

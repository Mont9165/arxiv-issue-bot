# QuSema: Detecting Silent Bugs in Quantum Libraries via Quantum-knowledge-enhanced Agents

- arXiv ID: `2610.10258v1`
- Authors: Yujin Song, Kaining Zhang, Qixin Zhang, Shuai Wang, Pingchuan Ma, Yuxuan Du
- Published: 2026-10-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `quant-ph`
- Links: [abs](http://arxiv.org/abs/2610.10258v1) | [pdf](https://arxiv.org/pdf/2610.10258v1)

## Abstract

Quantum libraries are now critical infrastructure for quantum algorithm development, yet their correctness remains difficult to test. Existing testing techniques mainly rely on failure-based or comparison-based oracles, exposing bugs only when executions fail, violate runtime checks, or disagree with another implementation. Their applicability is limited when suitable execution-based oracles are unavailable, leaving some silent bugs undetected. Such missed bugs can produce incorrect results that propagate into experimental conclusions, simulation studies, and algorithmic designs. Here we present QuSema, an autonomous testing agent for finding silent bugs in quantum libraries. QuSema uses constraints from quantum semantics and documentation as a source-level semantic oracle to assess whether implementation logic can produce invalid outputs from valid inputs. It operates through an agentic loop that repeatedly inspects library API documentation and source code, reasons about the intended behavior of quantum operations, identifies potential semantic deviations, and validates them by generating executable tests through library APIs. Guided by quantum-domain reasoning, QuSema turns high-level behavioral mismatches into concrete, user-triggerable bug reports, enabling it to uncover non-crash defects. We implement QuSema for Qiskit and PennyLane. On a benchmark of 20 historical silent bugs, QuSema achieves higher mean bug relocation counts than Claude Code and Codex, with the DeepSeek configuration costing less than Claude Code. QuSema also discovers 40 previously unknown bugs confirmed by the developers, including 30 silent bugs.

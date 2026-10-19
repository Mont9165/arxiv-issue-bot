# An Interactive GraphRAG Workspace for Reifying, Auditing, and Steering Conversational AI Memories

- arXiv ID: `2610.23559v1`
- Authors: Munshi Md Arafat Hussain, Md. Abdur Rahman, Md Saeed Siddik
- Published: 2026-10-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.23559v1) | [pdf](https://arxiv.org/pdf/2610.23559v1)

## Abstract

Conversational Large Language Models (LLMs) are widely employed in software engineering for code generation, debugging, and architectural design. However, as developers engage in multi-session development tasks, technical knowledge becomes siloed in isolated, linear chat histories. Reusing context across sessions leads to three critical challenges: (1) flat-vector retrieval fails to traverse multi-hop relational dependencies between distant architectural decisions; (2) temporal drift in software packages and APIs results in silent context poisoning when reusing aged dialogue logs; and (3) raw conversation concatenation induces prompt bloat and attention degradation.
  We present CognitiveCanvas, an interactive tool that transforms conversational AI memories from ephemeral text logs into persistent, manipulable, and audited knowledge objects. \textsc{CognitiveCanvas} integrates: (1) a Hierarchical Semantic Fact-Graph (HSFG) that distills dialogues into Goal, Fact, and Code artifacts, achieving a 92.2\% token reduction while enabling multi-hop GraphRAG traversal; (2) a Continuous Temporal Drift Auditor coupling 60+ regex heuristics with live calendar-anchored LLM verification for 1-click self-correction; and (3) a Spatial-Symbolic Prompt Compiler (SSPC) that translates 2D direct manipulation gestures (Voronoi clustering, node resizing, synthesis edges) directly into structured attention directives

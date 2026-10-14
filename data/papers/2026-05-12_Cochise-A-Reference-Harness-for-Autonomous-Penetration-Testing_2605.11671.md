# Cochise: A Reference Harness for Autonomous Penetration Testing

- arXiv ID: `2605.11671v1`
- Authors: Andreas Happe, Jürgen Cito
- Published: 2026-05-12
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.11671v1) | [pdf](https://arxiv.org/pdf/2605.11671v1)

## Abstract

Recent work on LLM-driven autonomous penetration testing reports promising results, but existing systems often combine many architectural, prompting, and tool-integration choices, making it difficult to tell what is gained over a simple agent scaffold. We present cochise, a 597 LOC Python reference harness for autonomous penetration-testing experiments. Cochise connects an LLM-driven agent to a Linux execution host over SSH and supports controlled target environments reachable from that jump host.
  The prototype implements a separated Planner--Executor architecture in which long-term state is maintained outside the LLM context, while a ReAct-style executor issues commands over SSH and self-corrects based on command outputs. The scenario prompt can be adapted to different target environments. To demonstrate the efficacy of our minimal harness, we evaluate it against a live third-party testbed called Game of Active Directory (GOAD).
  Alongside the harness, we release replay and analysis tools: (i) cochise-replay for offline visualization of captured runs, (ii) cochise-analyze-alogs and cochise-analyze-graphs for cost, token, duration, and compromise analysis, and (iii) a corpus of JSON trajectory logs from GOAD runs, allowing researchers to study agent behavior without provisioning the 48--64 GB RAM / 190 GB storage testbed themselves. Cochise is intended not as a state-of-the-art pen-testing agent, but as reusable experimental infrastructure for comparing models, agent architectures, and penetration-testing traces.

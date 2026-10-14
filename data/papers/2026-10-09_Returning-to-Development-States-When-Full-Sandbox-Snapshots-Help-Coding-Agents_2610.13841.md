# Returning to Development States: When Full Sandbox Snapshots Help Coding Agents

- arXiv ID: `2610.13841v1`
- Authors: Daniel Thi Graviet, Tanmay Shah
- Published: 2026-10-09
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.13841v1) | [pdf](https://arxiv.org/pdf/2610.13841v1)

## Abstract

Coding agents often make useful progress before they fail, but retry-from-scratch discards the machine state created along the way. This makes failure recovery an interesting search problem: if intermediate environment states preserve meaningful progress, restoring and branching from them could outperform repeatedly restarting from the initial state. We implement Go-Explore-style search over full Daytona snapshots and find that higher and more efficient solve rates depend mainly on progress that sits outside the repository, such as databases, services, and other runtime state. Our results suggest that full-snapshot search is most effective when long-horizon coding work spans multiple services whose state cannot be reconstructed from a single diff.

# Does Code Cleanliness Affect Coding Agents? A Controlled Minimal-Pair Study

- arXiv ID: `2605.20049v1`
- Authors: Priyansh Trivedi, Olivier Schmitt
- Published: 2026-05-19
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.20049v1) | [pdf](https://arxiv.org/pdf/2605.20049v1)

## Abstract

As autonomous coding agents see rapid adoption, their evaluation has primarily focused on task completion rates holding the target codebase fixed. This leaves a critical question unanswered: does the structural and stylistic quality, or ``cleanliness'' of the underlying code affect an agent's ability to navigate and modify it? To isolate the effect of code cleanliness from agent capability, we introduce an evaluation protocol built around minimal pairs: repositories that match on architecture, dependencies, and external behaviour, but differ on static-analysis rule violations and cognitive complexity. The pairs are constructed in both directions, by agent pipelines that either degrade a clean repository or clean a messy one. We author 33 tasks across six such pairs, evaluated through hidden tests at the application's public surface. Across 660 trials with Claude Code, code cleanliness does not change the agent's pass rate. However, it substantially alters the agent's operational footprint: agents working on cleaner code use 7 to 8% fewer tokens and reduce file revisitations by 34%. Our findings suggest that traditional maintainability principles remain highly relevant in the era of AI-driven development, shaping the computational cost and navigational efficiency of coding agents. Code cleanliness joins model choice, harness, and prompting as a factor that materially affects agent behaviours.

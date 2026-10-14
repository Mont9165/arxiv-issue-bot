# KISS Sorcar: A Stupidly-Simple General-Purpose and Software Engineering AI Assistant

- arXiv ID: `2604.23822v1`
- Authors: Koushik Sen
- Published: 2026-04-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.23822v1) | [pdf](https://arxiv.org/pdf/2604.23822v1)

## Abstract

Large language models can generate code and call tools with remarkable fluency, yet deploying them as practical software engineering assistants still expose stubborn gaps: finite context windows, single mistakes that derail entire sessions, agents that get stuck in dead ends, AI slop, and generated changes that are difficult to review or revert.
  We present KISS Sorcar, a general-purpose assistant and integrated development environment (IDE) built on top of the KISS Agent Framework, a stupidly-simple AI agent framework of roughly 1,850 lines of code. The framework addresses these gaps using a robust system prompt and through a five-layer agent hierarchy in which each layer adds exactly one concern: budget-tracked ReAct execution, automatic continuation across sub-sessions via summarization, coding, and browser tools with parallel sub-agents, persistent multi-turn chat with history recall, and git worktree isolation so every task runs on its own branch.
  To assess the power of the KISS agent framework, we implemented KISS Sorcar as a free, open-source Visual Studio Code extension that runs locally and effectively for long-horizon tasks, and supports browser automation, multimodal input, and Docker containers.
  In this research, we deliberately prioritize output quality over latency: giving a frontier model adequate time to validate its own output -- running linters, type checkers, and tests -- dramatically reduces the low-quality code that plagues faster but less thorough agents. The entire system was built using itself in 4.5 months, providing a continuous stress test in which any agent-introduced bug immediately impairs its own ability to work. On Terminal Bench 2.0, KISS Sorcar achieves a 62.2% overall pass rate with Claude Opus 4.6, comparing favorably to Claude Code (58%) and Cursor Composer 2 (61.7).

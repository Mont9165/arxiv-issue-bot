# All Green, Still Broken: Real-Flow Verification Lessons from an LLM-Integrated, Multi-Market Web Application

- arXiv ID: `2606.22475v1`
- Authors: Muhammad Bilal, Ali Hassaan Mughal
- Published: 2026-06-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.22475v1) | [pdf](https://arxiv.org/pdf/2606.22475v1)

## Abstract

Modern web applications increasingly combine three ingredients that are hard to test: output from large language models, multi-market internationalization, and browser-driven front-ends over external data sources. We report on a production rental-search assistant whose automated suite grew to 1,553 test cases in six weeks. The suite passed continuously, yet user-facing defects continued to reach production. We studied all 252 bug-fix commits in the project and classified each by the boundary, or seam, it escaped through. About 44 percent of the fixes fall in four seams that component-level unit tests cannot observe: the live browser runtime, the non-default market, the end-to-end flow, and the whole-system level. A fix without a guard at the seam let one defect ship twice. We present the four-seam framework, the measured defect distribution, and the practices we adopted, including a simple way for a team to find the seam that carries the most fixes.

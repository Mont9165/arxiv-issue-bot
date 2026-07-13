# Writing Bug Reports for Software Repair Agents: What Information Matters Most?

- arXiv ID: `2607.09553v1`
- Authors: Vincenzo Luigi Bruno, Alessandro Giagnorio, Daniele Bifolco, Leon Wienges, Massimiliano Di Penta, Gabriele Bavota
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.09553v1) | [pdf](https://arxiv.org/pdf/2607.09553v1)

## Abstract

Software development is increasingly moving toward agentic-first workflows. This includes AI agents responsible for generating initial fixes for submitted issue reports. In this setting, issue reports are no longer merely documentation for human maintainers; they become the primary task specification for the agent. However, little is known about how such reports should be written to maximize the agent's chances of producing a correct fix. We study what makes a bug report agent-ready. Starting from the SWE-bench Verified benchmark (i.e., a collection of 500 real repository issues with human-written gold patches and test suites for evaluating generated fixes) we manually classify each issue by change type (e.g., bug fix vs refactoring) and annotate each sentence with its information type, such as observed behavior, expected behavior, reproduction steps, localization cues, and suggested fixes. We focus on the 441 issues representing bug reports, and we run on them mini-swe-agent using three LLM backbones (i.e., GPT-5-mini, MiniMax M2.5, and Gemini 3 Flash). We then fit a binomial regression model to estimate the incremental association between each information type and agent success, controlling for confounding factors. Our results suggest that agentic-first reports benefit most from information that narrows the agent's search and repair space. Localization cues, such as references to affected code areas, are positively associated with successful repairs, while suggested fixes, expressed either in code or natural language, show some of the strongest positive associations with pass probability. An ablation study removing selected information types confirms that agents benefit less from information traditionally useful to humans, such as reproduction steps, and more from sentences that expose a repair direction, either through bug localization or a suggested fix.

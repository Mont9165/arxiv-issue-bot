# Engineering Sustainable Agents: A Systematic Comparison of Agentic LLMs for Developer Workflows

- arXiv ID: `2610.03010v1`
- Authors: Merve Astekin, Yan Naing Tun, Arda Goknil, Erik Johannes Husom, Lwin Khin Shar, Hasan Sözer, Ratnadira Widyasari, Hui Song
- Published: 2026-10-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2610.03010v1) | [pdf](https://arxiv.org/pdf/2610.03010v1)

## Abstract

Large language models (LLMs) are increasingly used in software engineering, including agentic systems that coordinate multiple agents, but impose higher computational and environmental costs. In this paper, we present a comprehensive empirical study of agentic LLM systems across five software engineering tasks: code generation, technical debt identification, code vulnerability detection, log parsing, and log analysis. For each task, we compare LLM configurations that range from a non-agentic single-query baseline to multi-agent workflows, using six open-weight LLMs, two prompt strategies, and three hardware platforms. We assess each configuration in terms of accuracy, inference latency, and energy consumption. Our results reveal substantial trade-offs between agentic complexity and energy efficiency: multi-agent designs consume on average 6.36$\times$ as much energy and run 6.07$\times$ as long as the non-agentic baseline, with worst-case slowdowns of up to 160$\times$ for individual task--hardware pairs. Accuracy gains from additional agents are limited and task-specific: multi-agent improves average vulnerability-detection accuracy, but lightweight non-agentic and single-agent configurations still dominate the Pareto front, accounting for 59 of 66 Pareto-optimal configurations. Model and prompt choice act as task-specific levers whose effective direction varies between tasks rather than as global defaults. We translate these findings into design guidelines for sustainable, task-aware LLM-based development tools.

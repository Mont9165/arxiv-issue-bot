# Comment and Control: Hijacking Agentic Workflows via Context-Grounded Evolution

- arXiv ID: `2605.11229v1`
- Authors: Neil Fendley, Zhengyu Liu, Aonan Guan, Jiacheng Zhong, Yinzhi Cao
- Published: 2026-05-11
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.11229v1) | [pdf](https://arxiv.org/pdf/2605.11229v1)

## Abstract

Automation platforms such as GitHub Actions and n8n are increasingly adopting so-called agentic workflows, which integrate Large Language Model (LLM) agents for tasks such as code review and data synchronization. While bringing convenience for developers, this integration exposes a new risk: An adversary may control and craft certain inputs, such as GitHub issue comments, to manipulate the LLM agent for unwanted actions, such as credential exfiltration and arbitrary command execution. To our knowledge, no prior academic work has studied such a risk in agentic workflows. In this paper, we design the first detection and exploitation framework, called JAW, to hijack agentic workflows hosted on automation platforms via a novel approach called Context-Grounded Evolution. Our key idea is to evolve agentic workflow inputs under the contexts derived from hybrid program analysis for hijacking purposes. Specifically, JAW generates agentic workflow contexts through three analyses: (i) static path-feasibility analysis to identify feasible agent-invocation paths and the input constraints required to trigger them, (ii) dynamic prompt-provenance analysis to determine how that input is transformed and embedded into the LLM context, and (iii) capability analysis to identify the actions and restrictions available to the agent at runtime. Our evaluation of JAW on GitHub workflows and n8n templates showed that 4714 GitHub workflows and eight n8n templates can be successfully hijacked, for example, to leak user credentials. Our findings span 15 widely-used GitHub Actions, including official GitHub Actions for Claude Code, Gemini CLI, Qwen CLI, and Cursor CLI, and two official n8n nodes. We responsibly disclosed all findings to the affected vendors and received many acknowledgements, fixes, and bug bounties, notably from GitHub, Google, and Anthropic.

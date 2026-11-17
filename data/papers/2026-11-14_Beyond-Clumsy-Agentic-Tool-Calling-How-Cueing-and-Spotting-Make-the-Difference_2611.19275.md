# Beyond Clumsy Agentic Tool Calling: How Cueing and Spotting Make the Difference

- arXiv ID: `2611.19275v1`
- Authors: Xindi Yang, Yan Liu, Jiajun Sun
- Published: 2026-11-14
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.19275v1) | [pdf](https://arxiv.org/pdf/2611.19275v1)

## Abstract

LLM-based task-oriented agents depend on tools to interact with their environments, but may overlook execution feedback, repeat ineffective calls, or persist with unproductive strategies. These behaviors can hinder agents' ability to use tools autonomously and sustain task progress. We characterize tool-use symptoms at two temporal granularities: local clumsy tool-use behaviors and tool-use detours spanning multiple interactions. Towards greater autonomy in tool use, we present ToolPulse, an online middleware supporting autonomous tool use through cueing and spotting. ToolPulse tracks execution state and temporal interaction patterns, monitoring proposed calls before dispatch and inspecting execution feedback prior to the agent resumes reasoning. It combines state-based rules, semantic sequence analysis, and interaction-feature similarity to identify intervention opportunities and provide verbal reminders, structured feedback, or context-specific advice from auxiliary models. Our process-oriented evaluation distinguishes trigger validity, behavioral cessation, and substantive correction alongside task outcomes and resource costs. Using SWE-agent with three backbone models, we evaluate 1,350 trajectories on 90 Python, C++, and Java bug-fix tasks, comparing unassisted execution with four assistance strategies. Substantive responses follow 61.6-90.9% of valid triggers for tool-use detours. Concise reminders achieve the highest observed aggregate substantive-response rate; more elaborate assistance offers symptom-dependent benefits and can be less effective. Aggregate repair outcomes remain close to baseline, with token savings in selected settings. These findings support proactive runtime assistance for autonomous tool use. The gap between behavioral adjustment and aggregate repair gains calls for careful decisions on intervention timing and assistance strategy in autonomous agents.

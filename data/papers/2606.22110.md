# TraceView: Interactive Visualization of Agentic Program Repair Trajectories

- arXiv ID: `2606.22110v1`
- Authors: Amirali Sajadi, Tu Nguyen, Kimmie Huynh, Esteban Parra, Preetha Chatterjee
- Published: 2026-06-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2606.22110v1) | [pdf](https://arxiv.org/pdf/2606.22110v1)

## Abstract

LLM-based automated program repair (APR) agents generate patches to fix software bugs with minimal human intervention. These agents often produce long trajectories of reasoning, tool use, and feedback to produce candidate patches. Final patch outcomes show whether a repair attempt succeeded or failed, but they do not show how the agent reached that outcome, or where the process became repetitive or misaligned with the task. This makes agentic repair failures difficult to diagnose, reproduce, and prevent. To help developers address these challenges, we present TraceView, an interactive tool for labeling and visualizing repair trajectories from APR systems. TraceView organizes raw and pre-labeled agentic runs with Thought, Action, and Result components to support semantic relation labeling and diagnosis, and renders the resulting trajectory as graph views. Furthermore, TraceView provides relation filters, patch outcome summaries, metrics, and node-level evidence panels to help users inspect how reasoning, actions, and feedback connect across the various steps of an agentic repair attempt. We evaluate TraceView with five researchers through a survey-based user study. Participants reported that TraceView made trajectories easier to scan and that its overview-to-detail workflow helped them better understand repair behavior. The TraceView source code is available at https://github.com/SOAR-Lab/agent-traj-visualization. A screencast of TraceView is available at https://youtu.be/9ZCh7Ifj2AQ.

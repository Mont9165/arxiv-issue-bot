# Instructions Are Evidence, Not Objectives: Measuring Outcome Alignment of Agents

- arXiv ID: `2610.17757v1`
- Authors: Kaiming Liu, Yuxuan Liu, Jinrui Ju, Minyuan Ruan, Xuanyu Lei, Peng Li, Yang Liu
- Published: 2026-10-13
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.17757v1) | [pdf](https://arxiv.org/pdf/2610.17757v1)

## Abstract

Large language model agents can follow complex human instructions to solve real-world tasks. In practice, however, initial instructions are often incomplete. In our analysis of 100 user-agent trajectories from SWE-chat, 56\% of initial instructions omit requirements that later emerge as necessary, and 52\% of the useful follow-up requirements could have been inferred from the project. A user states requirements from their own understanding of the task, and these \textbf{stated requirements} often differ from the \textbf{true requirements} that completing the task imposes. An agent should therefore treat the instruction as evidence rather than as the objective, inferring the true requirements from the instruction and the environment and satisfying them even when the user is not yet aware of all of them. We call this ability \textbf{outcome alignment}. In this work, we construct \textbf{TiGanEval}, a benchmark of software engineering and research tasks. In every task the user genuinely lacks part of the requirements, each requirement stays discoverable from the code and runtime behaviour of the environment, and requirements the agent infers are separated from those the user adds after observing delivered work. These properties together make outcome alignment measurable. Evaluating eight frontier models including GPT-5.6-Sol, we find outcome alignment broadly missing: the models lose 53 to 67 points of success rate when moving from the full specification to the partial instruction, and consequence feedback across four submissions does not close the gap. Furthermore, a plan-mode harness cannot compensate for the missing ability of the model itself, which places outcome alignment among the abilities the next generation of models should be developed for.

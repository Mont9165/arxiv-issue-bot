# Tracybot: Preserving Developer Intent by Tracing Agent-Generated Code to Prompts

- arXiv ID: `2611.09395v1`
- Authors: Răzvan Albu, Aliaksei Khval, Maxine Orlova, Danis Music, Filipe Araújo Veras Rosa, Lirong Yi, Ranim Khojah
- Published: 2026-11-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2611.09395v1) | [pdf](https://arxiv.org/pdf/2611.09395v1)

## Abstract

Large language models (LLMs) are now widely used in software development, and LLM-based coding agents are given increasing autonomy. With coding agents, many design decisions are made in the conversation between the developer and the agent. Typically, the developer starts a conversation with an agent and states their intent, the agent proposes options if needed, and the developer plans the change accordingly. Then, the resulting code is committed. However, in such scenarios, the decisions and the intent behind the changes remain in the conversation, with no link to the code they produced. In this paper, we present Tracybot, an open-source tool that integrates with VS Code, Git, and coding agents to keep track of relevant conversations in an LLM-assisted development process. Tracybot captures each change as a Tasklet which consists of optional planning prompts used to plan a change, together with a build prompt that produces it. Tracybot has two main features: (i) it maps line-level code changes made by coding agents to the Tasklets that produced them, and (ii) it allows the developer to export a Tasklet as a decision record when needed, for example when the decision concerns the architecture of the project. We developed the tool over two iterations of a design science study, while focusing the evaluation on the usability and user-friendliness of the tool. In a focus group (7 participants) and a survey (24 participants), we found that Tracybot was perceived as useful for activities like code review, and most participants found our Tasklet design and presentation to be a clear way to represent the developer's intent. Tool: https://github.com/TracyTeam/tracybot. Video: https://youtu.be/Vg_a1F5eO04.

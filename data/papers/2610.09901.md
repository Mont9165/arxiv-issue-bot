# A Chat Assistant for Software Exploration in a 3D Software Visualization

- arXiv ID: `2610.09901v1`
- Authors: Malte Hansen, Karim Issa, Wilhelm Hasselbring
- Published: 2026-10-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.09901v1) | [pdf](https://arxiv.org/pdf/2610.09901v1)

## Abstract

We present a chat assistant for interactive software exploration, embedded in the 3D software visualization tool ExplorViz. The assistant builds upon current Large Language Models (LLMs) and enables users to ask questions about the currently visualized software system and trigger actions that change the visualization through natural language. We integrate the chat assistant in our ExplorViz frontend using the CopilotKit libraries such that probabilistic LLMs are combined with deterministic and tool-based actions similar to implementations using the Model Context Protocol (MCP). The chat assistant is also enabled to restructure the software system by adding, removing, or modifying parts of the software system in the visualization. An empirical experiment with eleven participants evaluated both perceived comprehension support and the tool calls that were triggered by the chat assistant. Participants rated the assistant's generated summaries and explanations as largely correct. They also reported high usability for actions like highlighting entities in the visualization and the creation of new color themes. In contrast, open-ended chat-assisted software restructuring in the visualization showed mixed results. This suggests a need for stronger guardrails for the employed LLM and better incorporation of user feedback. Overall, the assistant was perceived as usable and promising for reducing interaction overhead during exploratory program comprehension tasks. We provide a video presenting the chat assistant's use and a reproduction package of the software system that was used in our evaluation.

# GUI Agents for Continual Game Generation

- arXiv ID: `2605.28258v1`
- Authors: Yixu Huang, Bo Li, Na Li, Zhe Wang, Kaijie Chen, Haonan Ge, Qingyi Si, Yuanzhe Shen, Ruihan Yang, Guangjing Wang, Hongcheng Guo
- Published: 2026-05-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CV`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2605.28258v1) | [pdf](https://arxiv.org/pdf/2605.28258v1)

## Abstract

Generating a game is not the same as making one that can be played. Despite advances in code generation, existing approaches treat game generation as one-shot translation from prompt to artifact, leaving interaction-level failures undetected. We argue that evaluating and improving game generation requires a player, and study two roles for graphical user interface (GUI) agents in this process: (1) as an objective evaluator, for which we introduce PlaytestArena, a new evaluation environment that pairs 200 browser-based game generation tasks across eight genres with rubrics of expected in-play behaviors, adjudicated by a GUI agent that loads each build in a browser and plays it; and (2) as a subjective playtester, for which we propose Play2Code, where a game agent and a GUI agent operate in a sustained loop with shared memory, turning game generation into a dialogue between coding and playing. Our experiments show that even frontier models struggle to generate playable games directly, while Play2Code achieves a 66.8\% rubric pass-rate, improving over single-pass and agentic-coding baselines by 37.1 and 14.6 points respectively. Further analysis shows that GUI playtester feedback is more traceable than a human report, yet idiosyncratic in ways reminiscent of human testers, establishing game playtesting as a critical testbed for interactive code generation. Our project website is available at https://continual-game-generation.vercel.app/.

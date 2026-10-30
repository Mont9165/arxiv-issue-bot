# RoleFUZZER: User-Behaviour Fuzzing for Role-Specification Adherence in Large Language Models

- arXiv ID: `2610.38438v1`
- Authors: Kshitish Ghate, Michael Saxon, Tadayoshi Kohno, Aylin Caliskan
- Published: 2026-10-28
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.38438v1) | [pdf](https://arxiv.org/pdf/2610.38438v1)

## Abstract

Large language models (LLMs) are often conditioned into specific roles such as tutors, interviewers, or agents acting for an organisation, through system prompts that specify how they should behave. The extent to which they can actually adhere to these role specifications under multi-turn interactions with realistic and potentially problematic users is understudied. To address this, we propose user behaviour fuzzing, a guided search over plausible user behaviours that can lead a model to violate its role specification, and introduce RoleFUZZER, a framework that adapts coverage-guided fuzzing from software testing to operationalise the search. RoleFUZZER constructs scenarios guided by a user-behaviour coverage grid that crosses a grounded taxonomy of user interaction types and the role specification of the model under test i.e. what is under pressure. With RoleFUZZER, we evaluate LLMs across five role specifications, including tutor, financial advisor, AI interviewer, antagonistic roleplay character, and web agent under organisational policies. Across simulated and validated conversations in 15 campaigns, the framework reaches >= 89% coverage of the 64-cell behaviour grid for every model and role tested, and surfaces specification-grounded failure patterns. At an equal budget of conversations, removing the RoleFUZZER grid and asking an LLM to generate specification targeting users free-form lowers coverage to 39-69% with fewer kinds of violations. The same specification can also fail in opposite directions. For e.g., on the antagonist, open-weight target models override the player's safety signals, while Claude Haiku 4.5 breaks character instead. RoleFUZZER offers a tractable way to uncover vulnerabilities in LLMs across role specifications by testing diverse user behaviours that are likely to violate them.

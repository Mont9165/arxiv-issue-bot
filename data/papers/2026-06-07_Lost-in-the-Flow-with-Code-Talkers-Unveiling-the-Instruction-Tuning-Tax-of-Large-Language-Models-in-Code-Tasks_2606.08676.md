# Lost in the Flow with Code Talkers: Unveiling the Instruction-Tuning Tax of Large Language Models in Code Tasks

- arXiv ID: `2606.08676v1`
- Authors: Shi Ying Chang, Chiok Yew Ho, Yichen Li, Yintong Huo
- Published: 2026-06-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2606.08676v1) | [pdf](https://arxiv.org/pdf/2606.08676v1)

## Abstract

AI coding assistants have significantly improved developer productivity by automatically suggesting code that aligns with user intent, and many of these tools are now integrated directly into Integrated Development Environments (IDEs). Developers interact with code in two distinct cognitive modes: Flow and Command. While developers require tools that directly complete or infill code in unfinished programs during Flow mode, they also need tools that can comprehend intentions expressed as natural-language instructions and convert them into executable code in Command mode. Although instruction-tuned Large Language Models (LLMs) dominate many application scenarios due to their abilities to infer and fulfill developers' intents, it remains unclear whether the same paradigm is equally suitable for different code-related tasks. Therefore, it is necessary to understand how instruction tuning affects the feasibility of CodeLLMs as coding assistants. To fill this gap, we conduct the first empirical study that uncovers a key trade-off caused by instruction tuning across programming modes, which we term the Instruction-Tuning Tax. Our results show that instruction tuning is not a free lunch: although instruction-tuned models are more capable of following instructions and leveraging structured guidance, these gains often come at the cost of weaker infilling performance. We further extend our study through both qualitative and quantitative analyses, including manual failure categorization, behavioral metrics that capture generation fidelity, and intermediate-checkpoint evaluation throughout the tuning process. Summarizing our results into seven findings and four implications, our study offers a new perspective on the development of AI-powered coding tools and highlights the need to carefully balance instruction-following ability with effective code generation assistance.

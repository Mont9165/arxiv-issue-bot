# EnvLunch: The Environment as a Free Lunch for Learning to Interact

- arXiv ID: `2610.33817v1`
- Authors: Wei Liu, Min Gao, Yali Du, Yulan He
- Published: 2026-10-24
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.33817v1) | [pdf](https://arxiv.org/pdf/2610.33817v1)

## Abstract

For agentic data analysis, language-model agents often require a large number of annotated tasks to learn how to interact effectively with executable environments (i.e., databases). While high-quality annotated tasks require heavy manual effort, an executable environment already provides rich interaction structure and verifiable outcomes. In this sense, the environment itself offers a free lunch, an additional set of verifiable tasks that require no human annotation. We propose EnvLunch, a warm-up stage that turns this environmental signal into agent training without human-written or model-generated task descriptions, before downstream agentic reinforcement learning. EnvLunch samples valid action trajectories, executes them to obtain final observations, and trains an agent to recover a functionally equivalent trajectory given only its final observation. This label-free warm-up enables the model to outperform the baseline by over 9 points on average across all downstream training budgets, and with few labels, the baseline needs 8 to 32 times as many annotated examples to match the accuracy that the EnvLunch model reaches at its smallest training budget. Letting the environment alone define the task yields a larger gain than having the model write its own tasks over the same environments, and this warm-up also improves fine-tuning on benchmarks beyond data analysis. EnvLunch therefore saves annotated tasks and provides a better starting point for fine-tuning agentic models when such tasks are limited.

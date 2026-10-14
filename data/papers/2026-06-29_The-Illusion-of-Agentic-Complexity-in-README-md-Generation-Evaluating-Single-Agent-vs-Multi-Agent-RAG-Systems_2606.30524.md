# The Illusion of Agentic Complexity in README.md Generation: Evaluating Single-Agent vs. Multi-Agent RAG Systems

- arXiv ID: `2606.30524v1`
- Authors: Abu Saleh, Tesfay Welegebreal Tesfay, Phuong T. Nguyen, Juri Di Rocco, Muhammad Umar Zeshan, Davide Di Ruscio
- Published: 2026-06-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.30524v1) | [pdf](https://arxiv.org/pdf/2606.30524v1)

## Abstract

Large Language Models (LLMs) are increasingly utilized to automate several software engineering tasks, including code completion, code summarization, testing, and the generation of repository-level documentation. While Multi-Agent Systems (MAS) are often adopted to support such tasks under the premise that task decomposition improves performance, the impact of architectural complexity on practical efficiency remains under-examined. This study empirically evaluates Retrieval-Augmented Generation (RAG) dependent architectures for the generation of README files for GitHub repositories. In this work, we conducted a systematic comparison between a Single-Agent pipeline, a specialized MAS, and a developer-guided planning (DevPlan) variant, benchmarked against LARCH -- a state-of-the-art baseline -- and the original ground truth. Results indicate a critical architectural trade-off: the Single-Agent pipeline achieves lexical quality comparable to MAS while reducing token consumption by 86% and operating at twice the speed. In contrast, manual taxonomy analysis demonstrates that MAS achieves high structural consistency (98%), resolving formatting issues observed in single-agent approaches. Autonomous planning is identified as the primary pipeline bottleneck; incorporating lightweight developer-guided plans produces the highest overall documentation quality, surpassing all the analyzed configurations.

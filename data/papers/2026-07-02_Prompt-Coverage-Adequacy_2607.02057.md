# Prompt Coverage Adequacy

- arXiv ID: `2607.02057v1`
- Authors: Florian Tambon, Michael Konstantinou, Cedric Richter, Charles Chenouard, Mark Harman, Mike Papadakis
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.02057v1) | [pdf](https://arxiv.org/pdf/2607.02057v1)

## Abstract

In recent years, it has become increasingly evident that large language models (LLMs) and autonomous agents raise the level of abstraction in software development by shifting the focus from writing precise procedures to expressing intents and goals. This paradigm shift introduces new challenges, particularly in how testing should be guided when prompts, rather than code, become primary development artifacts. To address this challenge, we propose Prompt Coverage Adequacy, a novel coverage criterion designed to support the testing of code generated from task descriptions. Prompt Coverage Adequacy serves as an analog to traditional code coverage, but operates at the level of prompts used in LLM and agent-based programming. Specifically, it measures how well a given test suite satisfies the requirements expressed in a prompt by leveraging the attention mechanisms of LLMs. We evaluate a simple instantiation of this criterion, based on attention boosting, across two datasets and multiple LLMs. Our results demonstrate that Prompt Coverage is associated with fault-detection effectiveness and can uncover over 30+% more faults than traditional code coverage when used to guide test generation. These findings suggest that Prompt Coverage Adequacy can serve as a foundation for developing testing metrics better suited to the emerging paradigm of LLM-driven software development, addressing the limitations of classical coverage criteria in this new context.

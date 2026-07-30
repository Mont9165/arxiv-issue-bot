# How Developers Experience Debugging Unfamiliar Codebases with Code Tours Generated and Evaluated by Local LLMs

- arXiv ID: `2607.26987v1`
- Authors: Balfroid Martin, Albert Julien, Aliti Dzenatan, Devroey Xavier, Vanderose Benoît
- Published: 2026-07-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.26987v1) | [pdf](https://arxiv.org/pdf/2607.26987v1)

## Abstract

Code tours are interactive, onboarding documentation to guide developers through a codebase. Large Language Models (LLMs) can automatically synthesize code tours. Prior work on code tour generation has not studied developer experience or trust calibration when debugging unfamiliar codebases with code tours generated and evaluated by open-weight LLMs. This study surveys how the properties of components in open-weight LLM-authored code tours influence developers' experiences when debugging unfamiliar codebases. We built a pipeline that generated and evaluated code tours from real reproducible bugs. 26 developers with varying backgrounds participated in a user study. In total, 26 code tours were authored from real Java bugs mined from 2025 GitHub commits, with each tour independently judged by two different LLMs, resulting in 52 evaluated configurations. Participants thought aloud as they explored each tour. Three authors qualitatively coded the interviews to identify recurring themes. Developers generally preferred tours that scaled detail with the code length, avoided merely restating code, were easily scannable, and adopted a guiding tone. However, some preferences were mutually exclusive, such as the use of imperative mood. Stack traces were often insufficient to identify all steps developers found relevant. Developers also trusted descriptions they perceived as human-written more than those they believed were AI-generated. Finally, LLM-generated annotations of tour quality were unreliable: sycophancy, confabulation, and incoherence were pervasive. This work lays a basis for future research on fine-tuning open-weight models for code tour generation, personalizing generation to accommodate diverging preferences, selecting relevant steps beyond stack traces, calibrating users' trust to avoid both disuse and misuse, and improving open-weight LLMs' ability to be more trustworthy evaluators

# Can LLMs Produce Better Object-Oriented Designs than Human-Involved Development?

- arXiv ID: `2605.19901v1`
- Authors: Zushuai Zhang, Elliott Wen, Ewan Tempero
- Published: 2026-05-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.19901v1) | [pdf](https://arxiv.org/pdf/2605.19901v1)

## Abstract

Background: Large Language Models (LLMs) are increasingly used for code generation. However, their ability to generate multi-class projects that require object-oriented design (OOD) remains unclear, especially relative to projects developed with human involvement. Aims: The primary objective of this study is to compare OOD quality in projects from three authorship conditions: PreAI (human-involved projects produced before widespread LLM use), PostAI (human-involved projects produced after widespread LLM use), and PureAI (projects generated end-to-end by contemporary LLMs). Method: We conducted a comparative case study on a postgraduate Java assignment. Two offerings of the same assignment were selected as the PreAI and PostAI datasets. PureAI projects were generated using three contemporary LLMs. We analyzed OOD quality using project-level OOD metrics, code smell density, and domain modeling. Results: Relative to human-involved projects, PureAI projects show lower code smell density and generally appear simpler in terms of total size, complexity, and coupling. However, this is consistent with oversimplification, as it is associated with missing abstractions and weaker responsibility separation. PostAI is closer to PureAI than PreAI on many OOD measures and also shows tendencies toward oversimplification. Conclusions: Our findings indicate that appropriate human guidance on object-oriented decomposition and responsibility assignment remains important when LLMs are used for object-oriented design.

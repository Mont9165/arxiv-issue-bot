# A Language for Describing Agentic LLM Contexts

- arXiv ID: `2605.01920v1`
- Authors: Noga Peleg Pelc, Gal A. Kaminka, Yoav Goldberg
- Published: 2026-05-03
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.01920v1) | [pdf](https://arxiv.org/pdf/2605.01920v1)

## Abstract

Large language models are increasingly used within larger systems ("LLM agents"). These make a sequence of LLM calls, each call providing the LLM with a combination of instructions, observations, and interaction history. The design of the encoded information and its structure play a central role in the quality of the resulting system, leading to efforts spent on context engineering. It is therefore critical to communicate the composition of the LLM context in a system, and how it evolves over time. Yet, no standard exists for doing so: context construction is typically conveyed through informal prose, ad hoc diagrams, or direct inspection of code, none of which precisely capture how a prompt evolves across interaction steps or how two context representation strategies differ. To remedy this, we introduce the Agentic Context Description Language (ACDL), a language for specifying the structure and dynamics of LLM input contexts in a precise, readable, and standard manner, along with visualizations. ACDL provides constructs for specifying context aspects such as role message sequences, dynamic content, time-indexed references, and conditional or iterative structure, capturing the full architecture of a prompt independently of any particular implementation. ACDL diagrams can be hand drawn on a whiteboard, or written in formal language which can then be rendered. We describe the language, demonstrate it by documenting several existing systems and their variants, and encourage the community to adopt it for describing LLM systems context, both in day-to-day communication and in papers. Tooling, examples and documentation are available at www.acdlang.org.

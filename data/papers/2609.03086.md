# Large Language Models and Language Server Protocol: a match made in context

- arXiv ID: `2609.03086v1`
- Authors: Alessandro Schena, Ilgiz Mustafin, Julia Kotovich
- Published: 2026-09-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.03086v1) | [pdf](https://arxiv.org/pdf/2609.03086v1)

## Abstract

This article introduces Eiffel-tools, a language server protocol (LSP) implementation for the Eiffel programming language that uses Large Language Models (LLMs) to aid the development of statically verified software. The tool provides various interactive and non-interactive commands to produce code and specifications. It uses language and project specific knowledge to precisely direct the LLM and verifies the output using a static verifier. It crafts rich programmatic prompts for the input and corrects or rejects the output. Furthermore, it handles the retries until the program passes verification. The tool's bug fixing capability is evaluated on 2 public datasets using 3 models. The tool can fix 76% to 95% of bugs by combining LLMs and a formal verifier depending on the model and prompts used. The results show the trade-off between the number of fixing attempts and the success rate.

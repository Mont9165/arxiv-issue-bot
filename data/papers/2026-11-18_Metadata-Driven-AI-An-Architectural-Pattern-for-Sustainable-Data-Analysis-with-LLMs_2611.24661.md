# Metadata-Driven AI: An Architectural Pattern for Sustainable Data Analysis with LLMs

- arXiv ID: `2611.24661v1`
- Authors: Renaud Pawlak, Armen Sulejmani, Jordi Cabot
- Published: 2026-11-18
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.24661v1) | [pdf](https://arxiv.org/pdf/2611.24661v1)

## Abstract

Large Language Models (LLMs) let users analyse data in natural language, either by giving the data to the model to read directly or by having the model generate code to process it. Both routes send the data, or fragments of it, to the model; both pay for inference on every run; and the code a model writes to answer a question is usually discarded once the question is answered. We present Metadata-Driven AI, an architectural pattern that keeps the data away from the model and turns each analysis into a reusable program. Only metadata (not the actual data) crosses a one-way inference boundary to the LLM. The program the LLM returns runs next to the data and is kept, so that inference is paid once per analysis rather than once per run. We describe the pattern together with a simple cost model, a measurement of how little information crosses the boundary on public datasets, and a benchmark showing that a small, locally hosted model can serve as the generator. We illustrate the pattern on three applications, each built on a different implementation of it: geospatial photovoltaic prospection over live public APIs, extraction of portfolio positions from bank statements, and a conversational assistant over smart-city dashboards.

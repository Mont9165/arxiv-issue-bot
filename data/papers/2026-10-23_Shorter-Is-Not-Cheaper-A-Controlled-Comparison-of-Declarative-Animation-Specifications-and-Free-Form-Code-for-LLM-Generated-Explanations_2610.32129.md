# Shorter Is Not Cheaper: A Controlled Comparison of Declarative Animation Specifications and Free-Form Code for LLM-Generated Explanations

- arXiv ID: `2610.32129v1`
- Authors: Jiantang Huang
- Published: 2026-10-23
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.HC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.32129v1) | [pdf](https://arxiv.org/pdf/2610.32129v1)

## Abstract

Chat assistants increasingly answer conceptual questions with interactive, animated explanations, generated either as free-form HTML/JavaScript or as declarative specifications that a fixed runtime plays. The declarative route is widely expected to be cheaper, faster and more reliable, because its outputs are shorter and constrained. We test this expectation in controlled comparisons whose hypotheses and analysis plans were frozen before the runs. We designed ExplainSpec, a time-indexed declarative animation format, and an observation contract that makes every generated explanation programmatically inspectable; validated, pacing-agnostic checkers score 20 explanation requests from five domains. Three Claude models (360 jobs) and, in a follow-up, the open-weight Qwen3-14B with thinking enabled and disabled (240 jobs) answered every request in both formats. For every model the specifications were 25-48% shorter in answer tokens (output excluding reasoning), yet with reasoning enabled total output fell significantly only for the largest Claude model and no model generated significantly faster. The reasons differed. The Claude models reasoned far more before writing specifications (exploratory; for the two larger models, from 15-20% to 85-88% of generations). Qwen3-14B reasoned about as much in both formats (a pre-registered test of this shift was not supported), and its shorter answers saved little against a reasoning trace more than twice as long. Nor were specifications more reliable: free-form pages were valid after one repair round in 95-100% of jobs for every model, whereas Qwen3-14B produced valid specifications in only 33% of jobs and passed all semantic tests in 17% (HTML/JavaScript: 62%). For reasoning models, a shorter format alone therefore does not make generation cheaper, faster or more reliable, and a format learned in context can cost reliability.

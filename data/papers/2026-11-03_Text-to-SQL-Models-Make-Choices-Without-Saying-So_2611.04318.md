# Text-to-SQL Models Make Choices Without Saying So

- arXiv ID: `2611.04318v1`
- Authors: Yichen Xu, Shipei Lin, Chenhao Ma
- Published: 2026-11-03
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2611.04318v1) | [pdf](https://arxiv.org/pdf/2611.04318v1)

## Abstract

A text-to-SQL answer can run, return a plausible number and still compute something other than what the analyst meant. This can happen when the request leaves a calculation choice open, such as whether to count rows or distinct entities, and the model settles it without saying so. Standard benchmarks cannot detect this, because they score each question against a single reference interpretation. We introduce SpecBridge, which tests such a choice by varying it alone: it poses three otherwise identical requests, one leaving the choice open and one per interpretation, and scores each answer by running it. The databases are real, and the choices are ones that made models fail on existing benchmarks. On 204 hand-validated tests, four language models usually compute each interpretation when asked for it, yet for the open request return both in only 15-58% of the tests where they can, often without mentioning the choice. The gap lies in reporting, not in computing. Benchmarks even penalize the alternative: on BIRD questions where such a choice changes the answer, over two in five of the answers marked wrong are right under the other interpretation. Because the gap lies in reporting, a system can narrow it without a stronger model: it first decides whether a request leaves a choice open, then answers each interpretation in its own call. On our tests and on AMBROSIA, an existing benchmark of ambiguous questions, this approach raises the share of open requests that get every interpretation by 29-63 points over the single answer that production assistants give, without lowering precision on clear requests. It also needs fewer user turns than asking a clarifying question.

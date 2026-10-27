# A Multi-Domain Study on the Effectiveness of LLMs at Writing Property-Based Tests

- arXiv ID: `2610.34487v1`
- Authors: M M Abid Naziri,  Feiran,  Qin, Khush Patel, Marcelo d'Amorim
- Published: 2026-10-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.34487v1) | [pdf](https://arxiv.org/pdf/2610.34487v1)

## Abstract

A property-based test (PBT) checks a property of a program on many generated inputs, but writing one takes a property, a generator of valid inputs, and an oracle. LLM-based PBT writers produce all three, yet they have been evaluated only on Python libraries. We study how two of them, Proptest-AI and Agentic-PBT, generalize to ten programs in five domains: deep learning libraries, databases, system software, compilers, and LLM serving engines. Most of these programs take text in their own language, such as queries, configurations, and programs. Agentic-PBT covers more branches than Proptest-AI on seven of the ten programs with Opus 5 and on all ten with GLM-5.3-Flash. Domain-specific fuzzers cover more of the compilers and of PostgreSQL and less of PyTorch than Agentic-PBT. We filed 180 bug reports, 44 of which duplicate reports that others filed after the models' knowledge cutoffs; maintainers have confirmed 65 of the others, in all five domains, and fixed 23. We draw lessons for building and evaluating such writers: low observability hurts them, and mature fuzzers paired with LLM-written properties could check that each feature behaves as documented.

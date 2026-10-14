# Faithful Autoformalization of Natural Language Assertions

- arXiv ID: `2607.13303v1`
- Authors: Hongyi Liu, Madhusudan Parthasarathy, Adithya Murali
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.13303v1) | [pdf](https://arxiv.org/pdf/2607.13303v1)

## Abstract

Formal contracts are essential for software testing and verification, yet writing them remains labor-intensive and error-prone. LLMs offer a promising path toward autoformalization: synthesizing executable assertions from natural-language specifications and thereby bridging the gap between informal developer intent and formal executable specifications. We present Monty: an autoformalization framework for assertions that tackles the challenges of expectations of validity of assertions and ambiguity in natural-language. Our techniques are based on filtering formalizations using a novel conformance score metric and validity scores obtained from testing the code against formalized assertions. We evaluate our approach on 541 assertion-generation tasks derived from 22 collection-like Java classes, and show that our technique produces the ground truth more reliably (improving upto 20 points in precision on average) than when using LLMs naively to translate assertions.

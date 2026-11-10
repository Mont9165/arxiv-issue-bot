# DM-Call: Decision-Model-Guided Function Calling with Cumulative Verification Feedback

- arXiv ID: `2611.10977v1`
- Authors: Minhyeong Yu, Wonduk Seo, Seunghyun Lee
- Published: 2026-11-07
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.AI`, `cs.CL`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.10977v1) | [pdf](https://arxiv.org/pdf/2611.10977v1)

## Abstract

Reliable function calling requires Large Language Models (LLMs) to select appropriate functions and generate arguments consistent with user intent. However, syntactically valid calls may still be semantically incorrect due to inappropriate function selection or mismatched arguments. In this paper, we propose Decision-Model-Guided Function Calling (DM-Call), a framework that combines local schema validation with separate decision-model verification of function selection and argument correctness. For rejected candidates, DM-Call accumulates verification probabilities, binary judgments, and schema errors across attempts. A hybrid feedback representation further combines numerical probabilities with verbal correctness labels to guide iterative refinement without executing external tools. Extensive evaluation across BFCL and API-Bank (first-call) demonstrates DM-Call boosts function-calling accuracy versus direct generation, at modest additional cost.

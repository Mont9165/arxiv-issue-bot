# TrustedCode: Evaluating Large Language Models for Developing Trusted Code through Automated Program Verification

- arXiv ID: `2610.30432v1`
- Authors: Muhammad Danial, Muhammad Taimoor Khan
- Published: 2026-10-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LO`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2610.30432v1) | [pdf](https://arxiv.org/pdf/2610.30432v1)

## Abstract

Recent reports, such as "Who is using AI to code?", indicate that approximately 30\% of Python code contributions to GitHub are AI-generated. Given the inherent unreliability of this code, formal verification emerges as a promising approach to establish trust in software correctness. Although leveraging large language models (LLMs) for formal verification has garnered increasing attention, practical adoption remains limited due to the challenges in writing formal specifications and verifying program correctness against them. Existing tools predominantly support verification for languages such as Java and C, with minimal support for Python. We present TrustedCode, an automated framework for verifying AI-generated Python code. TrustedCode uses LLMs to (i) type-check Python code, (ii) translate it into WhyML via the Why3 framework, and (iii) verify it against formal specifications using Why3 back-end automated theorem provers. Our method integrates chain-of-thought prompting through LangGraph to identify and address LLM limitations in specification generation and proving the specified programs. To evaluate TrustedCode, we conducted experiments on ten Python programs of varying complexity. Our analysis reveals that 50\% of the observed errors stem from domain knowledge gaps, 30\% from syntactic inaccuracies, and the remaining 20\% from semantic and type-related issues. These findings underscore the importance of targeted improvements in LLM-guided formal verification workflows for Python. TrustedCode is an open source tool available at: \href{github.com/mtaimoorkhan/TrustedCode}{github.com/mtaimoorkhan/TrustedCode}. The video demonstration is available at: \href{youtu.be/Nr5I2g8ec-s}{youtu.be/Nr5I2g8ec-s}

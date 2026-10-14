# LLM-based Vulnerability Discovery in Business Process Documentation

- arXiv ID: `2608.04271v1`
- Authors: Ben Falchuk, Himanshu Garg, Euthimios Panagos, Sioan Zohar
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2608.04271v1) | [pdf](https://arxiv.org/pdf/2608.04271v1)

## Abstract

Just like software and hardware, business processes are susceptible to vulnerabilities that can lead to product quality issues, delays, and increased costs. Business process vulnerabilities can arise from a variety of sources, including conflicting requirements, ambiguous documentation, invalid measurement spec-ifications, omission of quality checks, or implementations that differ from speci-fications. MIRABELLE is a system that identifies and characterizes business logic (BL) vulnerabilities from available business process representations, in-cluding ISO 9000/9001 documentation, user guides, work instructions, and pro-cess execution logs. MIRABELLE leverages recent advances in AI/ML to pro-cess available business process documentation and generate attributed graph rep-resentations of the business logic that can be processed using both graph and for-mal logic approaches for identifying potential vulnerabilities. However, extract-ing the business logic (e.g., operation execution sequences, decisions, input/out-put resources) from mostly natural language artifacts is challenging due to the required domain expertise, inherent process complexity, and the sometimes very large volumes of information. This paper focuses on our experimentation with Large Language Models (LLMs) and their role within MIRABELLE. We report on the performance of several LLMs across vital stages of vulnerability detection, from grammatical and technical error-flagging in short phrasings, to complete process structure recovery and extraction.

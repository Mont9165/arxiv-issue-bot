# Can LLMs be Effective Code Contributors? A Study on Open-source Projects

- arXiv ID: `2604.23340v1`
- Authors: Chun Jie Chong, Muyeed Ahmed, Zhihao, Yao, Iulian Neamtiu
- Published: 2026-04-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.23340v1) | [pdf](https://arxiv.org/pdf/2604.23340v1)

## Abstract

LLM-generated code is widely used, and the share of committed code produced by LLMs is expected to increase. However, we are not at a point where LLMs can be effective contributors to production code. We present an approach that exposes the shortcomings of LLM generation on such projects, and proposes recommendations; the targets of our study are sizable open-source projects, e.g., FFmpeg and wolfSSL. First, we developed a framework that uses verification and validation to evaluate a given LLM's suitability to fix or add features to an existing project. Second, we apply the framework to 212 commits (bug fixes and small feature improvements) in eight popular open-source projects and three LLMs: GPT-4o, Ministral3, and Qwen3-Coder. The success rate varied from 0% to 60% depending on the project. The LLMs failed in a variety of ways, from generating syntactically incorrect code, to producing code that fails basic (static) verification, or validation via the project's test suite. In particular, the LLMs struggle with generating new code, handling contexts (function or file) outside a certain size range, and in many cases their success is due to parroting code changes they have been trained on.

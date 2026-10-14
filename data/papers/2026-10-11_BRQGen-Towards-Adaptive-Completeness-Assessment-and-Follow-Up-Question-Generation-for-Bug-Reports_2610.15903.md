# BRQGen: Towards Adaptive Completeness Assessment and Follow-Up Question Generation for Bug Reports

- arXiv ID: `2610.15903v1`
- Authors: Tevfik Emre Sungur, Akif Emre Köşüş, Uğurcan Doğruçam, Eray Tüzün
- Published: 2026-10-11
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.15903v1) | [pdf](https://arxiv.org/pdf/2610.15903v1)

## Abstract

Many bug reports lack the necessary information required to reproduce issues. In early studies, large language models have been employed to generate follow-up questions to enhance incomplete reports. However, they ask a fixed number of questions regardless of whether the report is incomplete. We propose BRQGen, an iterative framework that identifies missing or ambiguous information in bug reports and generates targeted follow-up questions, only if necessary. Reports with no identified gaps are classified as sufficient. When the author responds, BRQGen evaluates whether the answers provide the requested information and generates further questions for any exposed gaps. We curated a novel dataset of 429 incomplete bug reports from Home Assistant and Brave Browser, each containing at least one maintainer follow-up question. Each question is mapped to the author's answer and assigned a label indicating whether the requested information could have been provided directly through the issue template. Earlier maintainer requests were associated with author responses, whereas delayed requests were associated with no response. Among responding authors, requests within one hour received median replies after 0.52 hours in Home Assistant and 1.45 hours in Brave, versus 9.76 and 13.49 hours after four hours. BRQGen covered 35.4% (Qwen 3.8 Flash) to 51.8% (DeepSeek V4.1 Flash) of the 1,073 ground-truth follow-up questions. DeepSeek V4.1 Flash managed to ask 45.7% of all detailed questions and 63.9% of all generic questions. Gemini 3 Flash Preview reached the highest macro-F1 for completeness assessment of 49.3%, but with a post-hoc analysis by getting only the gaps with high severities, Qwen 3.8 Flash reaches 73.6% macro-F1 score. Completeness assessment improved when at least one identified gap had high severity, and nearly all ground-truth questions were captured within the first two iterations.

# Towards Scalable and Cost-Efficient Vulnerability Detection: A Study on Automatic Query Generation

- arXiv ID: `2609.10412v1`
- Authors: Ivana Clairine Irsan, Ratnadira Widyasari, Huihui Huang, Ting Zhang, Yue Liu, Ouh Eng Lieh, Shar Lwin Khin, Kang Hong Jin, David Lo
- Published: 2026-09-09
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2609.10412v1) | [pdf](https://arxiv.org/pdf/2609.10412v1)

## Abstract

Static analysis remains a cornerstone of software security, yet the effectiveness of tools such as CodeQL is often limited by the substantial manual effort required to develop high-coverage query suites. While large language models (LLMs) have emerged as a potential solution for automated code reasoning, their practical utility in generating structured, executable security queries remains underexplored. In this paper, we conduct an empirical study to evaluate the ability of LLMs to synthesize CodeQL queries using vulnerability data from the National Vulnerability Database. Through this investigation, we explore the potential of using LLMs as an automatic CodeQL query generator. Subsequently, we systematically evaluate the performance of various LLM architectures across a diverse set of real-world vulnerabilities, measuring their ability to improve detection coverage and precision. Our findings reveal that LLM-generated queries significantly enhance the baseline CodeQL queries, yielding 82% improvement in average F1-score. Furthermore, we provide a detailed cost- benefit analysis showing that while direct LLM-based scanning of entire repositories is often computationally and financially prohibitive, leveraging LLMs to synthesize CodeQL queries offers a scalable and cost-effective alternative for large-scale vulnerability detection. Our results suggest that LLMs can effectively bridge the gap between unstructured vulnerability reports and formal static analysis specifications, offering a scalable path toward comprehensive automated vulnerability detection.

# Characterizing and Mitigating False-Positive Bug Reports in the Linux Kernel

- arXiv ID: `2605.07678v1`
- Authors: Jiashuo Tian, Dong Wang, Chen Yang, Haichi Wang, Zan Wang, Junjie Chen
- Published: 2026-05-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.07678v1) | [pdf](https://arxiv.org/pdf/2605.07678v1)

## Abstract

False-positive bug reports represent a significant yet underexplored challenge in the development and maintenance of the Linux kernel. They occur when correct system behavior is mistakenly flagged as a defect, consuming developer effort without leading to actual code improvements. Such reports can mislead developers, waste debugging resources, and delay the resolution of real bugs. In this paper, we present the first comprehensive empirical study of false-positive bug reports in the Linux kernel. We manually construct a dataset of 2,006 bug reports comprising 1,509 genuine bugs and 497 false positives collected from Bugzilla and Syzkaller. Our analysis indicates that false positives demand effort comparable to real bugs, often requiring extended discussions and non-trivial closure time. They occur in several components, especially File Systems and Drivers, mainly due to external dependencies and semantic misunderstandings. To address this challenge, we evaluate large language models (LLMs) for automated false-positive bug report mitigation. Among various prompting strategies, retrieval-augmented generation (RAG) performs best, achieving 91% recall and an F1 score of 88%. These findings highlight the non-negligible cost of false positive bug reports and show the promise of LLMs for more efficient false positive mitigation in the Linux kernel.

# Effective Construction of Feature Database of Fingerprinting Functions for Code-Clone SCA

- arXiv ID: `2610.24479v1`
- Authors: Zhiling Zhu, Tieming Chen, Chengwei Liu, Jiahui Wu, Qijie Song, Zhengzi Xu, Yueming Wu, Yang Liu
- Published: 2026-10-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2610.24479v1) | [pdf](https://arxiv.org/pdf/2610.24479v1)

## Abstract

In contemporary software development, the extensive adoption of third-party libraries has become standard practice to avoid reinventing the wheel. This trend is particularly evident in programming ecosystems that lack mature package managers, such as C/C++. Within this context, Code Clone Detection (CCD) techniques have emerged as essential tools for identifying instances of code reuse, thereby mitigating security and legal concerns. Despite significant advances in CCD algorithms, a notable gap persists between academic tools and real-world applications. This disparity primarily arises because academic tools rely on experimental datasets composed of a limited number of indexed repositories, whereas real-world applications require a much broader scope of code sources.
  To address this challenge, we propose a novel, systematic approach for selecting appropriate open-source repositories to construct a more effective CCD feature dataset. Our method, OSSScope, employs a greedy algorithm to analyze the diversity of fingerprinting functions across 2.55 million C repositories on GitHub, maximizing unique fingerprinting functions while minimizing the number of repositories required. OSSScope compiles an optimal feature dataset containing 61 million fingerprinting functions from 190K repositories, resulting in a 22.65% improvement in recall over SOTA tools, and covers over 95% of the features from other sources. Leveraging the selected repositories, we introduce RClassifier, a lightweight classification model that determines whether a repository should be included, streamlining construction for migration to other language ecosystems. Our evaluation of RClassifier in the Golang ecosystem validates its effectiveness, achieving recall comparable to the dataset produced by OSSScope.

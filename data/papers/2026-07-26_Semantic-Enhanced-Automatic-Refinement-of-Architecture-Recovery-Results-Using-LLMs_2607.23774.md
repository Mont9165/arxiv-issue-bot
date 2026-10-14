# Semantic-Enhanced Automatic Refinement of Architecture Recovery Results Using LLMs

- arXiv ID: `2607.23774v1`
- Authors: Yiran Zhang, Chengwei Liu, Yuqiang Sun, Zhengzi Xu, Weisong Sun, Wenke Li, Wuxia Jin, Yang Liu
- Published: 2026-07-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.23774v1) | [pdf](https://arxiv.org/pdf/2607.23774v1)

## Abstract

Understanding the architecture is crucial for effectively maintaining and managing large software systems. However, discrepancies often exist between the designed and implemented architectures, which can pose significant risks. To identify these discrepancies, architects need to extract the architecture from the system implementation, which is both time-consuming and error-prone. To simplify this procedure, many automatic architecture recovery techniques have been developed. Yet, their accuracy is often limited. Architects must still invest significant effort in refining recovery results to ensure they accurately reflect the implemented architecture.
  To reduce such manual effort, we introduce Semref, a framework that combines LLMs with dependency analysis to automatically refine architectures recovered by existing architecture recovery tools. By leveraging the LLM's semantic understanding capabilities and integrating structural dependencies, Semref enhances both the accuracy and the comprehension of recovered architectures. To evaluate Semref, we tested on 9 projects with published ground-truth architectures and 10 state-of-the-art architecture recovery tools. 5 commonly used metrics are adopted to evaluate the effectiveness of Semref. The results show that Semref improves accuracy across various metrics, with normalized gains ranges from 17.72\% to 43.35\%. Specifically, for MoJoFM and $a2a_{adj}$ metrics, Semref achieves relative improvements of 118.57\% and 100.41\%, respectively.

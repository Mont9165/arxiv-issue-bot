# Investigating Metamorphic Fuzz Oracle Enhancement via Large Language Models

- arXiv ID: `2606.14164v1`
- Authors: Ruixiang Qian, Ding Yang, Zengxu Chen, Yuxuan Gao, Chunrong Fang, Chao Zhang, Zhenyu Chen
- Published: 2026-06-12
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2606.14164v1) | [pdf](https://arxiv.org/pdf/2606.14164v1)

## Abstract

Fuzz drivers are essential components of greybox fuzzing, as they encapsulate target interfaces, define test spaces, and largely determine fuzzing effectiveness. Existing fuzz drivers typically rely on crash-based oracles for security testing, overlooking library functionality and limiting bug detection capability.
  In this paper, we present the first study on metamorphic-based fuzz oracle enhancement (MFOE), which augments existing fuzz drivers with metamorphic-based oracles derived from metamorphic relations (MRs). Since constructing and integrating such oracles requires substantial domain knowledge, automating MFOE is challenging. To address this challenge, we propose MetaFOE, an LLM-based framework that automatically generates and integrates metamorphic-based oracles.
  We evaluate MetaFOE on OSS-Fuzz drivers using three modern LLMs and five prompt strategies. MetaFOE generates 3,475 MRs, of which 77.3% are applicable, and implements 12,351 meta drivers, with 6,228 being valid. After three hours of fuzzing, the valid meta drivers improve edge coverage by an average of 18.7% and trigger 1,528 unique crashes. Our results demonstrate both the effectiveness of metamorphic-based oracle enhancement and the feasibility of using LLMs to automate MFOE, providing valuable insights for advancing greybox fuzzing.

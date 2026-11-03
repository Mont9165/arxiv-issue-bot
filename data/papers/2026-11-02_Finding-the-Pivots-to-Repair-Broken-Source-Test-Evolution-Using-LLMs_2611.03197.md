# Finding the Pivots to Repair Broken Source-Test Evolution Using LLMs

- arXiv ID: `2611.03197v1`
- Authors: Xiao Chen, Songqiang Chen, Jialun Cao, Yun Peng, Chun Yong Chong, Shing-Chi Cheung
- Published: 2026-11-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.03197v1) | [pdf](https://arxiv.org/pdf/2611.03197v1)

## Abstract

Repairing obsolete tests in response to source code evolution is critical for test suite reliability and software quality assurance. While large language models (LLMs) have emerged as promising tools for automating many software development tasks, the effective supply of context and the orchestration of repair pipelines in this source--test co-evolution scenario remain poorly understood. Moreover, although reasoning is found helpful for LLMs on some complex coding tasks, it remains unclear which reasoning steps actually contribute to effective test repairs and how the insights learned from LLMs' behaviors benefit coding agents. In this paper, we present a systematic empirical study of test repair for source-test co-evolution empowered by LLMs, investigating the effective setups and typical LLM behaviors. To support this study, we construct a new benchmark of 500 real-world source-test co-evolution cases from commits submitted between May 2024 and April 2026 across 15 highly-starred open-source Java projects. Our experimental results reveal several key insights for effective LLM-based test repair: the complementary benefits of combining test failure symptoms, source code changes, and supportive code context, as well as the effectiveness of self-repair rounds. We further derive a common reasoning action taxonomy from LLMs' reasoning traces, which proves instrumental in guiding LLMs to repair tests more effectively while at a lower financial cost. Applying our findings to the Codex agent further improves its repair success rate on challenging cases by 66.7%.

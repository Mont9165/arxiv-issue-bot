# SWE-Doctor: Guiding Software Engineering Agents with Runtime Diagnosis from Multi-Faceted Bug Reproduction Tests

- arXiv ID: `2607.00990v1`
- Authors: Yaoqi Guo, Yang Liu, Jie M. Zhang, Yun Ma, Yiling Lou, Zhenpeng Chen
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.00990v1) | [pdf](https://arxiv.org/pdf/2607.00990v1)

## Abstract

Large language model (LLM)-based software engineering agents are increasingly developed to resolve software issues by generating patches from issue reports and code repositories. Bug reproduction tests (BRTs) are an important building block for such agents and have been shown useful for patch validation. However, it remains unclear whether BRTs can also help the more central stage of patch generation. We first conduct a preliminary study and find that directly using advanced BRT generators to guide patch generation is not beneficial: fail-to-fail BRTs can mislead agents, while even fail-to-pass BRTs bring limited or negative gains. Our analysis reveals two reasons: fail-to-pass BRTs may cover only one manifestation of the reported issue, leading to partial patches, whereas fail-to-fail BRTs are unreliable as direct patch-generation targets. Motivated by these insights, we propose SWE-Doctor, a software issue resolution agent that guides patch generation with runtime diagnoses derived from multi-faceted BRT executions. SWE-Doctor first generates multi-faceted BRTs for different behavioral requirements stated in the issue, then executes and debugs these BRTs to construct runtime-grounded diagnosis records, and finally uses the diagnoses together with localization information inferred during BRT generation to guide patch generation and reduce partial patches. We evaluate SWE-Doctor on Python bug-fixing issues from the widely adopted SWE-bench Verified and SWE-bench Pro across five LLM backends. SWE-Doctor consistently outperforms existing agents across all 10 LLM-benchmark combinations, achieving average resolution rates of 75.7% on SWE-bench Verified and 59.4% on SWE-bench Pro. In particular, on the more challenging SWE-bench Pro, SWE-Doctor improves the average resolution rate by 8.0-8.9 percentage points over the baseline agents.

# Context Matters: Improving LLM-Based Code Summarization with Hierarchical Information

- arXiv ID: `2611.18964v1`
- Authors: Alexandre Petrachini, Breno Bernard Nicolau de França, Guido Araujo
- Published: 2026-11-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2611.18964v1) | [pdf](https://arxiv.org/pdf/2611.18964v1)

## Abstract

Source code documentation plays an important role in software quality activities, such as code review, program comprehension, maintenance, and bug fixing. However, it is often fragmented across individual code elements and focuses on local implementation details, providing little information about their surrounding context. This limits both developers' understanding of software systems and the effectiveness of Large Language Models (LLMs), whose reasoning is constrained by finite context windows. Enriching documentation with hierarchical context has the potential to improve software comprehension and support downstream, quality-related tasks for both developers and LLM-based tools. In this paper, we present an in silico study that showcases the impact of augmenting context on the generation of code-level documentation, using a variety of LLMs. By varying the function, class, and module hierarchy visible to the LLMs, we assess whether this variation produces a significant difference in the resulting code documentation compared with the existing documentation, which serves as a proxy for developer intent. Our results show that Documentation-Aware prompts with class or module-level context consistently yield summaries that are closest to the original documentation. Adding surrounding documentation yields statistically significant improvements over the baseline across models, with effect sizes ranging from negligible (DeepSeek) through weak (GPT-4o-mini) to medium (Gemini). We restrict the study to this immediate hierarchical context; call-graph traversal and cross-module dependency context fall outside our scope and are left to future work. These findings provide a clear path to improve automated documentation tools and enhance LLMs' ability to reason about codebases for downstream tasks, such as code retrieval.

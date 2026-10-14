# Towards Better Linux Kernel Fault Localization: Leveraging Contrastive Reasoning and Hierarchical Context Analysis

- arXiv ID: `2607.00562v1`
- Authors: Haichi Wang, Ruiguo Yu, Yesong Pang, Yingquan Zhao, Junjie Chen, Jiajun Jiang, Zan Wang
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.00562v1) | [pdf](https://arxiv.org/pdf/2607.00562v1)

## Abstract

Debugging the Linux kernel remains a formidable challenge due to its vast codebase, complex architecture, and low-level programming intricacies. Effective fault localization (FL) is thus essential for efficient kernel debugging and maintenance. While existing FL techniques (both traditional and LLM-based) have shown promise in general-purpose software, they are ill-suited for the kernel context. In particular, recent LLM-based techniques often treat bug reports and source code as plain text, lacking deep integration of kernel-specific knowledge, which limits their ability to identify root causes and achieve fine-grained localization. We present CoHiKer, a novel LLM-based FL technique tailored to the Linux kernel. CoHiKer introduces two key innovations: (1) contrastive reasoning, which identifies root causes by analyzing the behavioral divergence between carefully mutated passing and failing test cases, and (2) hierarchical context analysis, which systematically narrows the localization scope from files to methods by integrating crash reports, syscall semantics, inter-file dependencies, and kernel-specific features. Unlike prior techniques that rely on static understanding and full-code input, CoHiKer decomposes the localization task and enables structured LLM prompting to reason semantically over meaningful contexts. We evaluate CoHiKer on an extended Linux kernel bug dataset against five state-of-the-art baselines. CoHiKer consistently outperforms all competitors, improving Top-1 localization accuracy by up to 26.07% at the file level and 56.85% at the method level over state-of-the-art LLM-based baselines, while achieving up to 8.84% and 28.9% reductions in token consumption, respectively. Furthermore, CoHiKer demonstrates strong generalizability on the non-kernel dataset, with comparable gains (15.5% and 5.3% in Top-1 at file and method levels).

# When LLMs Invent Rust Crates: An Empirical Study of Hallucination Patterns and Mitigation

- arXiv ID: `2606.08444v1`
- Authors: Jieming Zheng, Hao Guan, Yepang Liu
- Published: 2026-06-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.08444v1) | [pdf](https://arxiv.org/pdf/2606.08444v1)

## Abstract

Large Language Models (LLMs) have become powerful tools for code generation, yet they remain prone to hallucinations-producing plausible but incorrect or fabricated outputs. Among these, package hallucination, where an LLM suggests non-existent dependencies, poses an emerging security risk to the software supply chain. While previous studies focus on popular languages like Python or JavaScript, in this work we present the first large-scale empirical study on crate hallucination in LLM-generated Rust code. We construct a multi-source dataset combining coding tasks from Stack Overflow, GitHub, and LLM-generated tasks, and evaluate both commercial and open-source models under various decoding settings. Our analysis reveals that, unlike prior findings in Python and JavaScript, hallucination behavior in Rust follows a distinct pattern: different models exhibit surprisingly consistent hallucination rates, and these rates show minimal sensitivity to model parameters. Furthermore, we investigate prompt engineering strategies to mitigate hallucinations without sacrificing code quality. This study provides new insights into the reliability and security implications of LLM-assisted Rust development, offering guidance for future research and safer model deployment in software engineering workflows.

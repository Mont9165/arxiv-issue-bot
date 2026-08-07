# Understanding the (In)Security of Vibe-Coded Applications

- arXiv ID: `2606.23130v1`
- Authors: Junquan Deng, Zhiyu Fan, Ruijie Meng
- Published: 2026-06-22
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.23130v1) | [pdf](https://arxiv.org/pdf/2606.23130v1)

## Abstract

Recent advances in large language models (LLMs) have enabled vibe coding, an emerging software development paradigm in which users create applications primarily through natural-language interactions with AI agents. Due to its low barrier to entry, vibe coding is rapidly gaining adoption in practice. Unlike conventional AI-assisted programming, where developers remain responsible for implementation and code review, vibe coding delegates a substantial portion of development to AI systems. This shift raises a fundamental question: how (in)secure are applications developed through vibe coding? In this paper, we conduct a systematic study of the security of vibe-coded applications. We collect a large corpus of real-world applications developed using popular AI agents and design a vulnerability analysis framework that combines agent-assisted code auditing with human validation. Using this framework, we examine the prevalence, severity, and root causes of vulnerabilities in the deployed vibe-coded applications. Our study reveals several key findings: (1) vibe-coded applications exhibit recurring vulnerability patterns that differ from those commonly observed in conventional software development workflows, including placeholder logic, unfiltered input, and secret exposure; (2) these vulnerabilities arise from systematic limitations of AI agents throughout the vibe-coding lifecycle, such as memory loss, locally optimized objectives and insufficient security knowledge; and (3) while advances in LLM capabilities and improved prompting strategies can reduce the incidence of vulnerabilities, they do not eliminate the underlying security risks. Overall, our study provides an empirical understanding of the security landscape of vibe-coded applications and lays the groundwork for addressing the security challenges introduced by the growing delegation of software development to AI systems.

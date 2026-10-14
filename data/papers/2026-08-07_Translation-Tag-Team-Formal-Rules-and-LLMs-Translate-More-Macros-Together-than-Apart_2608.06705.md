# Translation Tag Team: Formal Rules and LLMs Translate More Macros Together than Apart

- arXiv ID: `2608.06705v1`
- Authors: Brent Pappas, Joseph Zalusky, Zachary Burkett, Paul Gazzillo
- Published: 2026-08-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.06705v1) | [pdf](https://arxiv.org/pdf/2608.06705v1)

## Abstract

Modern critical software infrastructure is largely written in C. Since C lacks memory safety, researchers are investigating automatic translation of C to safer languages like Rust. But real-world C software consists of more than just C code, often using named code fragments called macros which are not part of the C language proper. State-of-the-art techniques avoid translating macros by preprocessing C code first before translating it. But this approach produces translations that are dissimilar to the original C code, because preprocessing inlines all macro definitions. To preserve macro usage in translated code, we study the language features that macros and C share and distill them into the first formally-specified translator, MerC. To evaluate MerC, we introduce the first macro translation benchmark, MacroBench, with test cases based on macros randomly sampled from real-world C programs. We find that MerC supports 50% of MacroBench's macro test cases. We also use MacroBench to evaluate how effective large language models (LLMs) are at performing the previously-unstudied task of macro translation. LLMs translate 22% to 77% more of MacroBench than MerC, but with 8% and 28% of these translations being incorrect translations requiring additional validation by developers. In contrast, MerC only produces correct translations. Our key insight is that running MerC first then using LLMs on the remainder reaps greater benefits than using either technique alone. This tag team approach has an average failure rate 32% lower than that of LLMs, while also translating an average of 51% more test cases than MerC.

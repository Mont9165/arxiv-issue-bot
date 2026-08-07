# LibEvoBench: Probing Temporal Knowledge Stratification in Code Generation Models

- arXiv ID: `2606.25402v1`
- Authors: Daniele Cipollone, Sergey Titov, Maliheh Izadi, Egor Bogomolov, Arie van Deursen
- Published: 2026-06-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.25402v1) | [pdf](https://arxiv.org/pdf/2606.25402v1)

## Abstract

Large software projects often depend on older versions of libraries, even as APIs continue to evolve across releases. This creates a challenge for LLMs: they must maintain knowledge of multiple API versions, not merely the latest or most common one. However, current LLMs are trained on temporally mixed corpora and lack explicit mechanisms for such version-specific reasoning, leading to anachronistic errors - calling APIs as they exist in a different library version. To systematically evaluate this phenomenon, we introduce LibEvoBench, a multi-task benchmark spanning multiple versions of widely used Python libraries, along with a new metric, the Software Evolution Understanding Score (SEUS), to measure models' consistency when working with evolving APIs. Our results show that state-of-the-art models are largely version-oblivious: performance degrades for evolving APIs, while for stable APIs it remains the same across versions. Moreover, simply specifying the target version provides no benefit, while relevant documentation significantly boosts models' accuracy. These findings highlight a systematic limitation of current training paradigms and motivate new approaches for temporally grounded knowledge in code generation.

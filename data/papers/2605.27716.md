# LLM Based Web Accessibility Repair: An Empirical Study of Detection, Remediation, and Cost

- arXiv ID: `2605.27716v1`
- Authors: Oluwatoyosi Oyelayo, Ghada Abushaqra, Parham Asadi, Durjoy Dey, Diego Elias Costa
- Published: 2026-05-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.27716v1) | [pdf](https://arxiv.org/pdf/2605.27716v1)

## Abstract

Ensuring web accessibility at scale remains challenging because rule-based tools provide limited coverage while manual remediation is costly and error-prone. This paper evaluates large language model based agents, specifically Kimi K2.5, for automated accessibility detection and repair compared with rule-based approaches. For detection, the LLM achieves performance comparable to rule-based tools, with F1 around 0.65, strong semantic understanding with F1 of 0.83, but lower reliability for syntactic and layout-related violations. For remediation, LLM-generated fixes are syntactically valid in over 99.7 percent of cases and improve accessibility compliance in 80.2 percent of instances, reducing violations from 3.98 to 1.7 per file. However, fewer than 26 percent of cases are fully resolved, and about 30 percent of patches introduce structural changes. We also find that iterative agent-based refinement increases computational cost by 52 percent and API usage by 1.64 times without improving remediation outcomes. These findings indicate that while LLMs are effective for partial accessibility repair, they are insufficient for complete and reliable remediation. Scalable accessibility solutions require hybrid approaches that combine LLM capabilities with rule-based validation and constraint-aware correction mechanisms.

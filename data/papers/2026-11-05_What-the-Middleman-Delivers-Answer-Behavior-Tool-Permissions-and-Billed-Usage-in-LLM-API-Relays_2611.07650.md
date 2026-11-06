# What the Middleman Delivers: Answer Behavior, Tool Permissions, and Billed Usage in LLM API Relays

- arXiv ID: `2611.07650v1`
- Authors: Xiaodong Wu, Zhimin Zhao, Qi Li, Chaklam Cheong, Xiangman Li, Jianbing Ni
- Published: 2026-11-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.07650v1) | [pdf](https://arxiv.org/pdf/2611.07650v1)

## Abstract

Third-party application programming interface (API) relays offer access to large language models (LLMs), often at lower prices. Users depend on these services for model quality, instruction compliance, and accurate billing. However, existing studies leave unclear whether relays meet these expectations together. We test 20 relays offering GPT-6 Astra and Claude Opus 5. First, we compare answers to knowledge questions with batch-matched official responses. In our first-round sample, the analysis flags 7/10 low-price and 2/10 same- or higher-price relays for behavioral differences. On retesting 35 pairs, seven gain or lose a flag under the original rules, and six under matched correction families. Because answer comparisons cannot reveal every delivery problem, we examine returned content and tool permissions. No injection is confirmed in 3,332 screened responses to a fixed, non-adversarial code and setup workload, yet four relays return tool calls despite instructions disabling them in the first round. Finally, to connect reported usage to actual costs, we compare input-token counts with official references and check balances. For identical requests, five relays report 4,200 to 60,000 more input tokens than the official API. Where balances are available (six services), charges follow reported usage at listed prices, including extra reported input tokens at one service. Our study shows that advertised models and prices are insufficient to judge relay reliability. It identifies unexplained billed token quantities and tool-permission violations as risks and shows why service evaluations need repeated measurements.

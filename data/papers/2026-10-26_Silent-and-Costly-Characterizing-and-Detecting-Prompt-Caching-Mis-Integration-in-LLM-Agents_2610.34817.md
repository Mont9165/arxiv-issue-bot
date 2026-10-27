# Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents

- arXiv ID: `2610.34817v1`
- Authors: Ying Zhang, Ruoqi Guo, Yi Liu, Gelei Deng, Yuekang Li, Yepang Liu, Leo Zhang
- Published: 2026-10-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.34817v1) | [pdf](https://arxiv.org/pdf/2610.34817v1)

## Abstract

Large language model (LLM) services process massive volumes of user requests, resulting in substantial inference costs. To reduce both cost and latency, providers have introduced prompt caching. However, correctly integrating prompt caching is non-trivial due to heterogeneous provider-specific APIs and continuously evolving caching semantics. To understand prompt-caching mis-integration in downstream applications, we conduct the first empirical study of 120 prompt-caching-related pull requests from 10 popular open-source agent systems. Our findings show that prompt-caching mis-integrations arise in both request-side misconfiguration and read-side usage miscount. More importantly, most mis-integrations fail silently without causing observable runtime failures.
  Motivated by these findings, we design CACHELINT, which models a prompt-caching mis-integration as an invocation site together with the preconditions required for correct cache integration. CACHELINT locates caching invocation sites with CodeQL and discharges each precondition either against a dated provider capability oracle or with an LLM guard check. CACHELINT achieves 0.71 precision and 0.78 recall in identifying the 120 labeled mis-integrations across the 10 studied agent systems. Our evaluation further demonstrates the effectiveness of CACHELINT in real-world settings, identifying 32 mis-integrations across 571 agent projects with 0.86 precision. These findings have received 21 developer confirmations and led to 18 upstream fixes, including one in Anthropic's official SDK.

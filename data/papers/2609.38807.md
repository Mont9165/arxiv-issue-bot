# PatchHolmes: Agentic Patch Retrieval via Listwise Selection

- arXiv ID: `2609.38807v1`
- Authors: Guanqun Yang, Yingming Zhou, Jiangrui Zheng, Shudong Hao, Xueqing Liu
- Published: 2026-09-30
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.38807v1) | [pdf](https://arxiv.org/pdf/2609.38807v1)

## Abstract

Patch retrieval, the task of finding the commit that fixes a known vulnerability, is the foundation of vulnerability management workflows, yet 60% to 63% of CVEs in the major advisory databases lack a patch link. We present PatchHolmes, a two-phase patch retrieval system that pairs a hybrid first-stage retriever with an agentic second-stage inspection loop. Unlike pointwise prior work that scores each candidate independently, the Phase 2 agent reads the top-100 listwise: it sees the full candidate list at once and selectively reads 3 to 10 commits through four budgeted tools before submitting a single best commit. On GitHubAD, PatchHolmes beats the pointwise binary classifier Favia by 25.34% Recall@1 and the retrieve-and-CoT baseline IRCoT by 31.40%, at one agent conversation per CVE versus Favia's ten; with the candidate set held identical, the agent adds 27.32% Recall@1 over taking the retriever's top candidate, and the same agent, transferred unchanged to PatchFinder_top10, lifts Recall@1 from PatchFinder's own top-1 pick (24.28%) to 39.86%. Swapping the LLM backbone within the Qwen family changes Recall@1 by under 1%, and a second model family (gpt-oss) stays far above the no-agent floor, so the gain comes from the listwise agent loop; the entire system runs on a frozen open-weight model over a local Git repository, without fine-tuning or external search APIs.

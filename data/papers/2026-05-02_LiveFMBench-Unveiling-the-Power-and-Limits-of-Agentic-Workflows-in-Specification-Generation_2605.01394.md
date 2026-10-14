# LiveFMBench: Unveiling the Power and Limits of Agentic Workflows in Specification Generation

- arXiv ID: `2605.01394v1`
- Authors: Dong Xu, Jialun Cao, Guozhao Mo, Junjie Hu, Cheng Wen, Hongyu Lin, Xianpei Han, Shengchao Qin, Cong Tian, Shing-Chi Cheung, Le Sun, Yaojie Lu
- Published: 2026-05-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.01394v1) | [pdf](https://arxiv.org/pdf/2605.01394v1)

## Abstract

Formal specification is essential for rigorous program verification, yet writing correct specifications remains costly and difficult to automate. Although large language models (LLMs) and agents have shown promising progress, their true capabilities and failure modes remain unclear. We present the first systematic and contamination-aware study of LLM- and agent-based formal specification generation for C programs. We introduce LiveFMBench, a continuously evolving benchmark of 630 ACSL (ANSI/ISO C Specification Language)-annotated C programs, including 360 newly collected cases designed to mitigate data leakage. Using this benchmark, we evaluate direct prompting with different sampling sizes, reasoning-enabled (thinking mode) inference, the agentic pipeline, and perform a fine-grained failure analysis. Experimental results reveal that naive evaluation substantially overestimates performance because models under direct prompting may exhibit unfaithful behaviors, such as deceiving automated provers or ignoring code-context constraints; after excluding such cases, the true specification generation accuracy drops by approximately 20\%. We further find that both increased sampling and thinking mode significantly improve success rates, with smaller models benefiting more from thinking mode. Agentic pipelines are particularly effective under low sampling budgets and on harder datasets. Failure analysis further shows that incorrect loop invariants are the dominant error type, while agentic pipelines notably reduce assertion errors. These results expose fundamental limitations in current LLM-based approaches and suggest they remain far from replacing human-authored formal specifications. We release LiveFMBench at https://huggingface.co/datasets/fm-universe/Live-FM-Bench and all evaluation artifacts to support future research.

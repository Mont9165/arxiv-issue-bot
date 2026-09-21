# BI-Agent and BI-Bench: Towards Automating End-to-End Business Intelligence

- arXiv ID: `2609.20886v1`
- Authors: Chuxuan Hu, Yeye He, Penny Zhou, Wee Hyong Tok, Daniel Kang, Surajit Chaudhuri
- Published: 2026-09-16
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.20886v1) | [pdf](https://arxiv.org/pdf/2609.20886v1)

## Abstract

Business intelligence (BI) is a cornerstone of enterprise decision-making and is widely used by enterprise users in software such as Power BI and Tableau. In traditional BI workflows, users need to prepare data by (1) identifying relevant tables, (2) performing data transformations, and (3) building join relationships, before they can (4) answer their business questions. These steps can be complex and time-consuming, making BI challenging.
  Given the strong capabilities of large language models (LLMs) in working with data, we study their ability to answer BI questions end-to-end, without requiring users to manually perform the tedious preparation steps. To do this, we harvest a large collection of real-world BI projects from public sources, and manually extract pairs of (questions, ground-truth answers) from real user dashboards. The resulting benchmark, BI-Bench, is the first benchmark to systematically study LLMs' ability on end-to-end BI.
  We find that even frontier LLMs perform poorly on BI-Bench, with less than 50% accuracy. To address their limitations, we design a tool-augmented BI-Agent that decomposes BI workflows into subtasks on structured data, such as search, join, and transform, and orchestrates specialized data management methods across BI stages. Furthermore, we develop a post-training framework that synthesizes training trajectories from real BI projects, enabling BI-Agent to be further post-trained using both supervised fine-tuning (SFT) and reinforcement learning (RL). BI-Agent achieves substantial accuracy gains of up to 40 percentage points with vanilla LLMs, and post-trained BI-Agent yields gains of up to 30 points. Our results highlight the importance of combining tool-augmented reasoning with domain-specific post-training in complex BI workflows, and point to promising directions for future research.

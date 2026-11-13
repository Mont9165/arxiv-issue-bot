# Does a Self-Learning Migration Agent Learn? An Audited Evaluation of Evidence-Graded Experience Memory for Oracle-to-PostgreSQL Migration

- arXiv ID: `2611.16143v1`
- Authors: Oleg Grynets, Vasyl Lyashkevych, Valeriia Oliferuk, Vladyslav Babenko, Danylo Kovalchuk, Dmytro Kostetskyi
- Published: 2026-11-12
- Primary category: `cs.LO`
- Categories: `cs.LO`, `cs.DB`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.16143v1) | [pdf](https://arxiv.org/pdf/2611.16143v1)

## Abstract

Do large language model (LLM) migration agents learn from accumulated experience, or do apparent gains reflect retrieval and reference reuse? We evaluate an evidence-graded agent for Oracle-to-PostgreSQL migration across four studies. On 1,833 documentation-derived source-reference pairs, persistent memory improved reference conformity (RC) over a no-memory baseline by 0.015 [0.004, 0.025], while policy adaptation added no gain (-0.004 [-0.010, 0.001]). An audit found that 264 of 367 held-out units (72%) shared a PostgreSQL reference with training, and the memory effect on the 103 leak-free units fell to 0.002 [-0.008, 0.011]. A model-free nearest-target copy baseline scored RC 0.222, outperforming all LLM systems (at most 0.163). A reference-grouped split reduced copying to 0.119; a rerun on 374 units in 118 independent target groups found no statistically distinguishable memory effect (0.005 [-0.003, 0.017]) and no policy effect. A separate Oracle-grounded evaluation on 216-224 real PL/SQL units showed that 10-22% of PostgreSQL-accepted units were behaviorally incorrect; a human-gated fix cycle increased demonstrably correct units from 98/216 to 167/224. A write-back study showed a 54% decline in retrieval margin as the knowledge base grew from 12 to 1,200 entries. We derive six evaluation rules that distinguish cross-task learning from reference leakage, copying, metric artifacts, and unstable feedback.

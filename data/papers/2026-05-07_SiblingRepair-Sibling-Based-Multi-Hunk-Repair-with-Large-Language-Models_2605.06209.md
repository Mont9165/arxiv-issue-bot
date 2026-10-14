# SiblingRepair: Sibling-Based Multi-Hunk Repair with Large Language Models

- arXiv ID: `2605.06209v1`
- Authors: Xinyu Liu, Jiayu Ren, Yusen Wang, Qi Xin, Xiaoyuan Xie, Jifeng Xuan
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.06209v1) | [pdf](https://arxiv.org/pdf/2605.06209v1)

## Abstract

Developers often make similar mistakes across code locations implementing related functionalities. These locations, called siblings, share similar issues and require similar fixes. Accurately identifying siblings and consistently repairing them are crucial for automated program repair. Hercules is a SOTA technique designed for sibling repair. However, it is limited by strong assumptions about sibling locations and commit-history availability, rigid AST-based sibling matching, and inflexible template-based patch generation. To address these limitations, we present SiblingRepair, a new LLM-based multi-hunk APR technique specialized for sibling repair. Starting from a suspicious location identified by spectrum-based fault localization, SiblingRepair searches for semantically related sibling candidates using token- and embedding-based code matching, without restricting discovery to failing-test coverage or commit history. It then uses an LLM to identify failure-relevant siblings and generate consistent patches through two complementary strategies: simultaneous repair, which jointly repairs siblings, and iterative repair, which progressively analyzes candidates for patch construction. SiblingRepair further preserves promising patches generated from earlier suspicious locations and combines them into generalized multi-hunk patches. We evaluate SiblingRepair on the Defects4J and GHRB benchmarks. The results show that SiblingRepair substantially outperforms SOTA multi-hunk repair techniques including Hercules. Our evaluation further demonstrates its repair efficiency, the effectiveness of its sibling detection and repair components, and limited impact of the LLM data leakage on the results. Overall, SiblingRepair advances automated sibling and general multi-hunk repair.

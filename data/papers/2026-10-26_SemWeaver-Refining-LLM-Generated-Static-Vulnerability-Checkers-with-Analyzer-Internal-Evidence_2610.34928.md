# SemWeaver: Refining LLM-Generated Static Vulnerability Checkers with Analyzer-Internal Evidence

- arXiv ID: `2610.34928v1`
- Authors: Chengzhi Yi, Shenao Wang, Yanjie Zhao, Xiao Cheng, Haoyu Wang
- Published: 2026-10-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.34928v1) | [pdf](https://arxiv.org/pdf/2610.34928v1)

## Abstract

Recent work shows that LLMs can synthesize static-analysis checkers from security patches, but a compilable checker is not necessarily a correct one. A patch reveals what changed, not why the change is safe, so generated checkers often match only the surface edit and miss the deeper semantic condition. Existing refinement loops feed back compilation errors and validation reports, yet these signals describe symptoms without explaining what the checker misunderstands about the code. We observe that the analysis framework itself already computes the information needed to close this gap. Control-flow graphs, symbolic values, memory regions and checker callbacks are available inside the analyzer but unused by current refinement strategies. SemWeaver is a plug-in refinement layer that extracts patch-relevant analyzer evidence and assembles it with source context and validation feedback into a structured, provenance-labelled bundle. An iterative editing loop refines the checker on both the vulnerable and fixed revisions, guarded by a retention gate that accepts warning recovery or false-positive reduction while preventing over-pruning. We evaluate SemWeaver on 39 KNighter-derived CSA checkers from Linux kernel fixes. With analyzer evidence, refinement reaches 23 warning-positive vulnerable revisions (vs. 15 for KNighter's loop) and raises version-level $F_1$ from 0.448 to 0.575. An ablation removing internal evidence recovers fewer silent cases and produces different checker edits, indicating that the two evidence configurations address complementary recognition gaps. Additional experiments cover three editor models on a 12-subject subset, a CodeQL query refinement, and controlled source-form variations. A qualitative follow-up on all 11 non-tied comparisons traces each warning-count change to a specific checker repair, such as recognizing a lowered callback or unwrapping an expression cast.

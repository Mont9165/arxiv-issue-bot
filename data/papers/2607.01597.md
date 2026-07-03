# A Single Patch Is Not Enough: Deterministic Fusion of Repair Candidates

- arXiv ID: `2607.01597v1`
- Authors: Boyang Yang, Xiangliang Hu, Luyao Ren, Yanjun Chen, Bach Le, Tegawendé F. Bissyandé, Haoye Tian
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01597v1) | [pdf](https://arxiv.org/pdf/2607.01597v1)

## Abstract

Modern LLM coding agents are commonly evaluated using pass@k, but developers typically apply a single final patch in real-world settings. This pass@k-to-pass@1 gap is a post-generation problem: a candidate patch pool may contain a correct patch, but the system must decide which one to suggest to developers. Existing post-generation approaches mainly rank whole candidates, filter them with tests, or query an LLM judge, but none deterministically reuse shared edit-atom evidence to both select and construct the final patch. Thus, we propose PatchFusion, a deterministic atomic evidence fusion approach for candidate patches that consults no test outcome at decision time. PatchFusion first fuses whole-diff agreement into a repair neighborhood, selects an auditable representative, and then applies evidence-constrained fusion (ECF) to retain repeated edit atoms and prune unsupported parts. To evaluate this setting, we build PatchFuseBench, a fixed-pool benchmark covering SWE-bench Verified, SWE-bench Multilingual, and Defects4J candidate patches.
  On PatchFuseBench, PatchFusion solves 426/500 bugs on SWE-bench Verified and 236/300 on SWE-bench Multilingual, and reaches 87/371 plausible patches on Defects4J, outperforming every matched candidate-pool selector on all three. PatchFusion recovers 41 and 27 bugs that no single source solves (30 and 18 more over the best single source). Ablation studies show that ECF adds +5/+6/+9 solved bugs by recovering in-pool repairs that selection misses, with no observed regression, and that PatchFusion's gains remain stable as candidate pools are resampled. On these complementary multi-source pools, cross-candidate evidence recovers more correct patches than the test-based and LLM-based selectors we evaluate, at orders-of-magnitude lower cost, reaching within 96.2% and 89.7% of the candidate-reachable ceiling on the two SWE-bench benchmarks.

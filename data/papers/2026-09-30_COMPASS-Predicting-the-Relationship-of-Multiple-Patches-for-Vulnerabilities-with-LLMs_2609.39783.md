# COMPASS: Predicting the Relationship of Multiple Patches for Vulnerabilities with LLMs

- arXiv ID: `2609.39783v1`
- Authors: Yi Song, Dongchen Xie, Xiaoyuan Xie, He Zhang, Lin Xu, Chunying Zhou, Zhi Jin
- Published: 2026-09-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.39783v1) | [pdf](https://arxiv.org/pdf/2609.39783v1)

## Abstract

Modern software heavily relies on code reuse, so upstream vulnerability fixes do not automatically propagate to downstream codebases. Downstream maintainers must manually adopt patches to eliminate known risks. In practice, a single vulnerability often corresponds to multiple patches, which greatly complicates downstream patch adoption because different patch relationships imply different adoption strategies. To address this challenge, we first manually inspect large-scale multi-patch vulnerabilities (about 1K) in the real world and interview experienced developers, summarizing six typical types of patch relationships, i.e., Merge, Mirror, Better Solution, Fixing-of-Fixing, Collaboration, and Separation. Based on these observations, we propose COMPASS, an automated approach that predicts the relationships of multiple vulnerability patches with large language models. Given a CVE as input, COMPASS follows a four-phase pipeline that (i) identifies the patch group and pre-scans explicit relationships, (ii) performs individual patch analysis, (iii) infers relationship instances via a hierarchy-guided prompt, and (iv) validates completeness and consistency of the inferred results. As output, COMPASS reports the predicted relationships within the patch group and visualizes them as a relationship graph. We evaluate COMPASS on a benchmark of 300 multi-patch CVEs and compare it against mainstream learning-based and LLM baselines. Results show that our method achieves strong and consistent prediction effectiveness and outperforms SOTA by 85.04% on average. We publicly release an online querying website to support community reuse of patch relationships knowledge: https://patch-relation.com.

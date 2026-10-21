# TraceLite: Efficient Trace Reduction for SWE Agents via Optical Compression and Redundancy Removal

- arXiv ID: `2610.28612v1`
- Authors: Jingyu Xiao, Qianxi Liu, Yintong Huo, Yuan Jiang, Michael R. Lyu
- Published: 2026-10-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.28612v1) | [pdf](https://arxiv.org/pdf/2610.28612v1)

## Abstract

Software engineering agents solve repository-level tasks through iterative tool use, but their continuously growing interaction traces incur substantial token consumption and inference overhead. Existing compression approaches often require model training, auxiliary LLM calls, or assumptions about specific content such as source code. We present TraceLite, a simple yet effective, training-free framework for compressing heterogeneous SWE-agent observations. Our preliminary study shows that optical rendering preserves substantial textual and semantic information under moderate compression, while agent trajectories exhibit both cross-step and phase-level redundancy. Motivated by these findings, TraceLite preserves recent observations as high-fidelity text, renders historical observations as compact images, removes overlapping content, and discards phase-expired observation payloads after code editing. It requires neither offline training nor auxiliary LLM inference. We evaluate TraceLite on SWE-bench Verified and DeepSWE using GPT-5.6-Luna and Gemini-3.8Flash as backbone models. On SWE-bench Verified, TraceLite achieves 78.25% resolve rate, outperforming the evaluated compression baselines while reducing average input-token consumption and API cost by 33.05% and 21.30%, respectively. Moreover, it introduces only 0.438 seconds of compression latency per observation. These results demonstrate that TraceLite improves SWE-agent efficiency with low processing overhead and without compromising issue-resolution capability. Our code is available at https://github.com/xjywhu/TraceLite.

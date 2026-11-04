# How Agent Skills Evolve: A Large-Scale Empirical Study of Skills on GitHub

- arXiv ID: `2611.04456v1`
- Authors: Jinjun Huang, Jialun Cao, Junxiao Han, Zhonghao Jiang, Shing-Chi Cheung, Zhongxin Liu
- Published: 2026-11-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.04456v1) | [pdf](https://arxiv.org/pdf/2611.04456v1)

## Abstract

Large language model-based agents increasingly rely on external skills to reuse task-specific knowledge without retraining the model. As skills become common for extending agent capabilities, understanding creation and evolution is critical for reliable agent systems. However, existing studies mainly examine agent skills from a static perspective, leaving their evolution in real-world repositories largely unexplored. This limits our understanding of the patterns and motivations behind skill changes. To fill this gap, we present a large-scale empirical study of agent skills, capturing 84,200 skills and 750,898 commits from GitHub. We manually construct taxonomies of skill components, change patterns, and evolution motivations, and build an automated annotation pipeline to label changes at scale. Based on the taxonomy, we conduct quantitative analyses of skill composition and post-creation evolution frequency, together with qualitative assessments of modified components, change patterns, and motivations. Our findings reveal five implications: (i) reliability receives less attention in skill composition and change, motivating execution-contract skill design that incorporates verification and recovery mechanisms; (ii) evolution changes concentrate in project-coupled skills, calling for automated just-in-time skill updating mechanisms; (iii) change patterns are dominated by incremental enrichment and refinement, motivating pattern-guided skill enhancers that diagnose and improve incomplete skill components; (iv) redundancy is a practical maintenance issue, highlighting the need for context-efficient skill representation; (v) security-motivated changes show limited risk reduction, suggesting skill regression testing methods that objectively verify skill functionality and security. Beyond these insights, our dataset provides a basis for future studies on automated skill techniques.

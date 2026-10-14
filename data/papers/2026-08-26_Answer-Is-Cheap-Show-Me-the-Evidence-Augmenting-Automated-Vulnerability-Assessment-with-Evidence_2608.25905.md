# Answer Is Cheap, Show Me the Evidence! Augmenting Automated Vulnerability Assessment with Evidence

- arXiv ID: `2608.25905v1`
- Authors: Shengyi Pan, Zelong Zheng, Jiayuan Zhou, Xing Hu, Xin Xia, Shanping Li
- Published: 2026-08-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.25905v1) | [pdf](https://arxiv.org/pdf/2608.25905v1)

## Abstract

Software vulnerability (SV) assessment helps prioritize remediation by characterizing reported vulnerabilities. Existing
  automated methods predict assessment results from SV reports (SVRs), but often overlook information in rich text, such as
  screenshots and code snippets, as well as contextual information about vulnerable projects. They also focus on prediction
  accuracy without providing explanations or supporting evidence, limiting their practical use when analysts must validate
  imperfect predictions. We propose EAVA, a framework that uses large language models (LLMs) to assess SVs and provide
  supporting evidence. EAVA employs specialized LLM agents to process rich-text content and project information, and builds a
  dedicated assessment model through a two-stage training pipeline. It first uses supervised instruction tuning on automatically
  annotated reasoning trajectories to inject domain knowledge, and then applies reinforcement learning to improve intrinsic
  reasoning. EAVA also retrieves similar historical vulnerabilities as supplementary evidence. Experiments on a newly collected
  SVR dataset show that EAVA outperforms the strongest baseline by 5.3 to 35.2 percent across multiple metrics. Ablation studies
  confirm the effectiveness of assessment-specific model training and information enrichment. A user study with security experts
  further demonstrates that the evidence provided by EAVA is useful and practical for real-world SV assessment.

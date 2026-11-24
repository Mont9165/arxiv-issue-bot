# RepoClean: Evaluating Coding Agents on Repository-Level Obsolete Code Cleanup

- arXiv ID: `2611.30350v1`
- Authors: Hongyixuan Yuan, Qixing Zhou, Pengcheng Huang, Qingshuo Ni, Runsong Zhao, Shaokai He, Xiangpeng Li, Deqiang Ouyang
- Published: 2026-11-23
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.30350v1) | [pdf](https://arxiv.org/pdf/2611.30350v1)

## Abstract

Large language model (LLM) agents have demonstrated strong repository-level programming capabilities. However, as software evolves, repository code may become redundant or obsolete, increasing maintenance costs and potentially introducing functional issues. Agents must therefore identify and remove unnecessary code safely, yet autonomous repository-level code cleanup remains insufficiently evaluated in isolation. To evaluate this capability, we introduce RepoClean, a benchmark of 200 cleanup tasks from 34 popular open-source Python repositories. RepoClean is constructed by automatically reintroducing deleted code from real repository histories into newer versions, preserving current implementations and retaining instances where previously passing tests consequently fail. To restore existing functionality without new feature development, agents must use repository interfaces and cross-file dependencies to determine which historical code to remove and which implementations to preserve. Evaluation of seven models shows that even the best-performing model, GPT-6 Astra, resolves only 23% of tasks. Further analysis reveals that agents remove substantially less obsolete code when cleanup is not explicitly requested. RepoClean provides a foundation for systematically studying these cleanup challenges and advancing coding agents toward autonomous software maintenance.

# Self-Supervised Scaling of Terminal Environments for Scientific Domains

- arXiv ID: `2610.02710v1`
- Authors: Zhongzhi Li, Yucheng Shi, Zongxia Li, Junyao Yang, Ruhan Wang, Yu Wang, Jingyuan Huang, Jichao Yu, Ninghao Liu, Haitao Mi, Leowei Liang
- Published: 2026-10-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.02710v1) | [pdf](https://arxiv.org/pdf/2610.02710v1)

## Abstract

Terminal agents are increasingly deployed beyond software engineering in science and other specialized domains. Constructing training environments requires executable reference behavior and a domain-specific verifier that distinguishes semantic correctness from superficially plausible artifacts. Authoring these components for each task requires repeated engineering and limits reuse. We introduce software-in-the-loop reconstruction, a self-supervised framework that obtains reference outputs and verification targets from existing software workflows, executable programs mapping structured inputs to outputs. For each workflow, we execute multiple input configurations and partition cases into public observations and hidden evaluations. Given the instruction, input schema, and public input--output observations, an agent constructs an editable program without access to the source workflow. The candidate is evaluated on hidden configurations against workflow outputs. A hierarchical verifier combines domain-specific semantic comparison, structural validity, and anti-shortcut checks, while public feedback supports iterative revision. The construction admits additional workflows and configurations without authoring a reference solution for each task. We instantiate SWR with 500 workflows and 46 software families across six domains. Across three attempts per task, Qwen3.8-Max solves 838 tasks and produces 1,422 verified trajectories, which we oversample to 3,000 reconstruction-only training examples. Supervised fine-tuning of Qwen3.8-27B improves mean Terminal-Bench 2 performance from 47.94% to 53.56% across three seeds and achieves the highest mean among four matched-token corpus controls on all four reported evaluations. These results indicate that existing scientific software can provide scalable, behaviorally verified supervision for terminal agents.

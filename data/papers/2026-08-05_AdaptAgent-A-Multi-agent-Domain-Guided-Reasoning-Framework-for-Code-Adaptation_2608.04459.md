# AdaptAgent: A Multi-agent, Domain-Guided Reasoning Framework for Code Adaptation

- arXiv ID: `2608.04459v1`
- Authors: Xiaokai Rong, Hridya Dhulipala, Aashish Yadavally, Tien N. Nguyen
- Published: 2026-08-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.04459v1) | [pdf](https://arxiv.org/pdf/2608.04459v1)

## Abstract

Developers often need to adapt into their projects the code generated from LLMs or code snippets from online forums. However, integrating them into an existing repository remains challenging in a manual process. A successful integration typically requires more than copying code as a user must produce correct adapting changes at a designated location in the target repository. We formalize this as the code adaptation problem: given a snippet, functional intent, a target repository, and an adaptation location, generate a patch that adapts the snippet into the repository. We present AdaptAgent, a multi-agent, domain-guided reasoning framework for code adaptation. Rather than relying on single-shot prompting, AdaptAgent decomposes adaptation into specialized agents that communicate via typed artifacts: an Intent Summarizer extracts adaptation goals from Q&A text; a Policy Agent derives domain policies from six adaptation categories; a Domain Planner generates a self-ordered plan; a Context Miner distills sibling-method semantics from the target codebase; and a Code Adapter realizes the plan as a minimal unified diff, iteratively refined using a compiler-based Verifier. This division of labor enables robust, policy-aligned adaptations and supports adapting code snippets into a project. On a real-world dataset, AdaptAgent outperforms strong baselines in semantic correctness and produces patches that mirror developers' actual adaptation patterns. Our ablation study shows each agent's necessity, especially planning for code-hardening and exception-handling, and intent for logic customization.

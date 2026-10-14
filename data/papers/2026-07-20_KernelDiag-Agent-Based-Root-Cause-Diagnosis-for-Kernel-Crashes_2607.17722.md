# KernelDiag: Agent-Based Root Cause Diagnosis for Kernel Crashes

- arXiv ID: `2607.17722v1`
- Authors: Weijing Wang, Zan Wang, Dong Wang, Haichi Wang, Junjie Chen
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.17722v1) | [pdf](https://arxiv.org/pdf/2607.17722v1)

## Abstract

The Linux kernel is one of the most complex software systems, where automated fuzzing continuously exposes thousands of crashes, yet root-cause diagnosis remains a manual and time-consuming bottleneck. Existing LLM-based root cause analysis (RCA) techniques, effective for distributed systems, do not readily generalize to kernel debugging due to sparse low-level artifacts, heterogeneous diagnostic evidence (e.g., syscalls, logs, and crash reports), and complex non-linear fault propagation that demands fine-grained method-level reasoning. To address these challenges, we propose KernelDiag, an agent-based framework for kernel root-cause diagnosis via structured causal reasoning. KernelDiag first aligns heterogeneous diagnostic artifacts through log-to-code mapping, and then employs artifact-specialized agents to iteratively reason over source-level program semantics and crash-specific kernel configurations. The inferred causal dependencies are incrementally organized into structured Evidence Graphs, enabling accurate faulty-method localization and causal explanations. We evaluate KernelDiag on the real-world KGYM benchmark. KernelDiag consistently outperforms state-of-the-art localization approaches at both file and method levels, achieving significant improvements in Top@k accuracy, including up to 4x and 2x gains in challenging settings without explicit hints. Furthermore, both human and LLM-assisted evaluations show that KernelDiag generates accurate, coherent, and actionable diagnostic explanations. Overall, this work lays the foundation for automated kernel root-cause diagnosis by bridging low-level diagnostic evidence with source-level causal reasoning.

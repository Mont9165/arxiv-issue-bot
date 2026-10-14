# We Must Have Missed This Comment: Detecting and Repairing Stale Function References in Linux Kernel Comments

- arXiv ID: `2608.03734v1`
- Authors: Kexin Sun, Yunbo Lyu, Xutong Ma, Hongyu Kuang, Ratnadira Widyasari, He Zhang, Xiaoxing Ma, Julia Lawall, David Lo
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03734v1) | [pdf](https://arxiv.org/pdf/2608.03734v1)

## Abstract

As the Linux kernel evolves, code comments may become outdated, as the functions they reference can be refactored or removed independently without corresponding updates to the comments. Such stale function references can mislead maintainers and thus hinder code comprehension. Prior work on detecting code-comment inconsistency mainly focused on addressing semantic misalignment between Javadoc comments and their directly annotated functions, making them inapplicable to this type of externally induced staleness in the Linux kernel. Therefore, we propose ReCite, a three-stage approach to identify and repair such stale references: (1) detecting unresolved function-form symbols -- symbols in comments that appear to reference functions but for which no matching function can be found in the current codebase, (2) tracing the evolution history of each unresolved symbol through the Git history, and (3) generating LLM-based repair suggestions grounded in the evolution history and current code context. On Linux kernel v6.18-rc1, ReCite detects 869 stale references with generated repair suggestions. A manual evaluation on 200 sampled repairs shows that 178 (89.0%) provide useful repair guidance, with 85 (42.5%) directly applicable. Of our 75 submitted patches, 50 have been accepted. We also empirically study all unresolved function-form symbols.

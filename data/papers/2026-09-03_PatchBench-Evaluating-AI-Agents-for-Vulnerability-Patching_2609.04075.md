# PatchBench: Evaluating AI Agents for Vulnerability Patching

- arXiv ID: `2609.04075v1`
- Authors: Chihao Shen, Jiacheng Li, Aastha Mahajan, Jeffery Siyuan Tian, Yonghwi Kwon, Yizheng Chen
- Published: 2026-09-03
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.04075v1) | [pdf](https://arxiv.org/pdf/2609.04075v1)

## Abstract

AI agents have recently demonstrated strong performance in automated vulnerability patching. However, existing evaluations often validate a patch only by testing whether the provided Proof-of-Concept (PoC) input still triggers a crash. This leaves two key threats to validity: agents may reproduce memorized historical developer patches, or they may generate surface-level fixes that only suppress the reported crash.
  We study these concerns for C/C++ vulnerability patching. We introduce a patch similarity metric to detect memorized patches. On average, 25% of the agent patches exhibit substantial similarity to historical developer patches, indicating that patch memorization is a real threat to the validity of vulnerability patching evaluations. Meanwhile, agents also frequently exploit benchmark structures to pass patch validation by patching on the crash stack trace to suppress the crash, rather than localizing and fixing the root cause of the vulnerabilities.
  To handle these issues, we propose PatchBench, a new benchmark for evaluating AI agents on realistic vulnerability patching tasks. PatchBench selects vulnerabilities whose ground-truth fixes lie outside the crash stack and uses vulnerability transplant and code mutations to migrate historical vulnerabilities into new repository contexts, reducing the risks of surface-level fixes and patch memorization. We develop new patch validation methods that thoroughly evaluate both security and semantic correctness of agent patches. Across 11 state-of-the-art agents, including the top three AIxCC agents, the original PoC-only validation inflates the patching task solve rate of agents by 1.83$\times$ on average. Our results reveal key limitations of current patching agents and point to future research directions for more reliable vulnerability repair.

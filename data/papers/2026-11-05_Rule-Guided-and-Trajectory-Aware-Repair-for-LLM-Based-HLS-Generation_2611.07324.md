# Rule-Guided and Trajectory-Aware Repair for LLM-Based HLS Generation

- arXiv ID: `2611.07324v1`
- Authors: Xianjing Zhu, Wenqi Lou, Yuanbo Wen, Teng Wang, Lei Gong, Chao Wang, Xuehai Zhou
- Published: 2026-11-05
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.07324v1) | [pdf](https://arxiv.org/pdf/2611.07324v1)

## Abstract

Large language models (LLMs) offer a promising path for directly generating functionally correct and synthesizable HLS-C from natural-language specifications. However, existing approaches often struggle to turn multi-round tool feedback and reusable HLS knowledge into effective revisions, limiting end-to-end generation success. We propose MementoHLS, an agentic HLS generation framework built around executable and falsifiable dual-memory-guided repair. MementoHLS combines an Executable Repair Contract Library (ERCL), which converts cross-task HLS knowledge into evidence-gated repair actions, with a Reviewer-Grounded Falsification Ledger (RFL), which converts task-local repair history into trajectory evidence to suppress ineffective routes and preserve validated progress. To ensure reliable outcome attribution, a Same-Candidate Reviewer binds Parse, Compile, Testbench (TB), and Synthesis (Synth) outcomes to the corresponding candidate, while a Single-Commit Arbiter commits at most one candidate per round. Evaluated on 94 HLS-Eval and 170 Bench4HLS tasks, MementoHLS improves same-candidate TB$\wedge$Synth pass@1/pass@5 from 41.7%/57.4% to 58.9%/68.1% on HLS-Eval, and from 15.5%/32.9% to 32.4%/50.6% on Bench4HLS, demonstrating substantial improvements in end-to-end HLS generation reliability.

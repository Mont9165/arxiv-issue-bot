# Execution-Anchored Hallucination Calibration Reranking for Verilog Code Generation

- arXiv ID: `2608.22938v1`
- Authors: Guang Yang, Xing Hu, Xiang Chen, Terry Yue Zhuo, Xin Xia
- Published: 2026-08-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AR`
- Links: [abs](http://arxiv.org/abs/2608.22938v1) | [pdf](https://arxiv.org/pdf/2608.22938v1)

## Abstract

Large Language Models (LLMs) have demonstrated remarkable capabilities in code generation, yet their performance degrades significantly on low-resource Hardware Description Languages such as Verilog. While multi-candidate sampling improves the likelihood of generating correct solutions, au-tomatically selecting the optimal candidate remains an open challenge. Through a systematic empirical study across nine models and two benchmarks, we identify two critical limitations:(1) existing execution-based reranking methods, which rely on testbench pass/fail outcomes, exhibit poor domain transferability due to low-quality generated testbenches; and (2) LLM-as-a-Judge suffers from reasoning hallucination, producing incon-sistent judgments for execution-equivalent code. These findings reveal two signal types with orthogonal errors: execution signals(deterministic but testbench coverage limited)and reasoning signals (semantically rich but hallucination-prone). Their orthog-onality suggests combining the two signals, yet in our experiments letting the reasoner directly observe execution results merely anchors its judgments on test outcomes; we therefore acquire the two signals independently and fuse them only at the decision stage. Based on these insights, we propose EAHC, an Execution-Anchored Hallucination Calibration reranking framework that anchors reasoning judgments to execution behavior so that execution-equivalent candidates receive consistent scores, which implements a dual-channel architecture: EAHC-R, a 4B reasoning discriminator; and EAHC-T, a testbench generator leveraging RAG for execution verification.

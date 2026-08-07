# (How) Do Large Language Models Understand High-Level Message Sequence Charts?

- arXiv ID: `2605.13773v1`
- Authors: Mohammad Reza Mousavi
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2605.13773v1) | [pdf](https://arxiv.org/pdf/2605.13773v1)

## Abstract

Large Language Models (LLMs) are being employed widely to automate tasks across the software development life-cycle. It is, however, unclear whether these tasks are performed consistently with respect to the semantics of the artefacts being handled. This question is particularly under-researched concerning architectural design specification. In this paper, we address this question for High-Level Message Sequence Charts (HMSCs). These are visual models with a rigorous formal semantics that have been used for various purposes, including as a foundation for Sequence Diagrams in the Unified Modelling Language (UML). We examine whether LLMs "understand" the semantics of HMSCs by examining three LLMs (Gemini-3, GPT-5.4, and Qwen-3.6) on how they perform 129 semantic tasks ranging from querying basic semantic constructs in HMSCs (i.e., events and their ordering) to semantic-preserving abstractions and compositions, and calculating the set of traces and trace-equivalent labelled transition systems. The results show that LLMs only have a modest understanding of the formal semantics of HMSCs (ca. 52% overall accuracy), with great variability across different semantic concepts: while LLMs seem to understand the basic semantic concepts of MSCs (ca. 88% accuracy), they struggle with semantic reasoning in tasks involving abstraction and composition (ca. 36% accuracy) and traces and LTSs (ca. 42% accuracy). In particular, all three LLMs struggle with the notions of co-region and explicit causal dependencies and never employed them in semantic-preserving transformations.

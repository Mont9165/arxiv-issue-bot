# CodeChat-Eval: Evaluating Large Language Models in Multi-Turn Code Refinement Dialogues

- arXiv ID: `2606.25747v1`
- Authors:  Guoxiang,  Guo, Kla Tantithamthavorn, Neelofar Neelofar, Yuanyuan Qi, Aldeida Aleti
- Published: 2026-06-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.25747v1) | [pdf](https://arxiv.org/pdf/2606.25747v1)

## Abstract

Large Language Models (LLMs) are increasingly used in software engineering to generate and refine code. In practice, developers often continue from an initial code generation request with follow-up refinement instructions, such as requests to improve style, restructure implementation, or change the execution strategy while preserving the intended behaviour. However, existing benchmarks generally omit this multi-turn code refinement dialogue setting and therefore cannot evaluate whether LLMs maintain functional correctness, i.e., whether the refined code still passes the test suite for the original task. To address this limitation, we introduce CodeChat-Eval, an evaluation framework that constructs evaluation sessions from multi-turn code refinement dialogues using a dynamic instruction selection algorithm. Our empirical study on open-weight and proprietary LLMs observes a statistically significant decrease ranging from 19.2% (GPT-5 Nano) to 69.2% (Llama 3.1 8B) in functional correctness over multi-turn refinement. The largest correctness drops are associated with logic-level refinements and additive change requests. These findings indicate that LLMs struggle to maintain functional correctness during multi-turn code refinement dialogues, and highlight the need for benchmarks that evaluate functionality-preserving refinement beyond single-turn generation.

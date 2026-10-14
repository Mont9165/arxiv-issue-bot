# ExeCRE: Execution-Consistency Guided Reliability Estimation for Self-Correcting Code Generation

- arXiv ID: `2608.04439v1`
- Authors: Yiru Dong, Richong Zhang, Fanshuang Kong, Si Chen
- Published: 2026-08-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.04439v1) | [pdf](https://arxiv.org/pdf/2608.04439v1)

## Abstract

Large language models (LLMs) have made notable progress in code generation, but they still struggle on challenging tasks that require sophisticated algorithms or complex implementations. Recent methods increasingly use code execution as feedback, especially in self-correction pipelines that construct verification signals from generated code. However, these pipelines often depend on supervision signals whose reliability is unknown, which can introduce misleading feedback, unnecessary revisions, and incorrect final answers. To address this issue, we propose ExeCRE, an Execution-Consistency guided code Reliability Estimation framework. Instead of judging candidate code by tests or LLM feedback, ExeCRE estimates code reliability by statistically analyzing consistency patterns in execution outputs over a large number of randomly generated inputs. It collects execution outputs over generated inputs, projects them into consistency signals, and applies the Dawid-Skene model to infer latent code reliability. We integrate ExeCRE into self-correction for code generation. Experiments show that ExeCRE consistently improves both effectiveness and stability, while substantially reducing misleading correction signals. Under GPT-5.2 on LiveCodeBench, the average number of misleading feedback cases on already correct code drops from 113.2 with a representative self-correction baseline to 14.0 with ExeCRE. As an additional study, we apply the same reliability estimation strategy to code-based mathematical reasoning and observe similar benefits. These results suggest that ExeCRE enables more reliable use of generated code in execution-based pipelines.

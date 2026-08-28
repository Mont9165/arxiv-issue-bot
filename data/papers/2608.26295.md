# MemToC: Benchmarking Memory-Tool Conflict Resolution in Large Language Models

- arXiv ID: `2608.26295v1`
- Authors: Arseniy Varlamov, Rishat Zinnatullin, Elisei Rykov, Alexander Panchenko, Ilseyar Alimova
- Published: 2026-08-26
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.26295v1) | [pdf](https://arxiv.org/pdf/2608.26295v1)

## Abstract

Tool-augmented LLMs must arbitrate between two fallible sources when a tool return conflicts with their parametric memory, yet existing evaluations measure source preference without establishing source correctness. We introduce MemToC, a controlled benchmark for post-tool-return arbitration with executable tools. MemToC comprises 6,504 evaluation episodes constructed from 542 quality-controlled factual questions, independently elicited model-specific closed-book answers, and controlled tool returns of known correctness. These components instantiate four source-correctness cases; tool-error and no-tool conditions are separate controls. Across five open-weight 7-9B models, tool returns strongly dominate elicited closed-book answers. The four instruction-tuned models retain a verified-correct answer against an incorrect tool in only 6.5-17.1% of eligible cases, follow a correct tool in 86.0-93.1%, and repeat the tool return in 78.4-86.0% of cases where both sources are wrong. No cross-model ordering remains stable across three instruction-wording variants with the question and episode content held fixed. We compare prompting with SFT and DPO using chain-level cross-fitting over ToolHop, so questions sharing an underlying fact never straddle training and evaluation. We apply an asymmetric success criterion: correct-answer retention must improve without a detected reduction in correct-tool following. SFT and DPO meet this criterion on the same two of four instruction-tuned backbones. Improvements rarely come cleanly: 19 of 20 tested method-model combinations reduce abstention after tool errors or on unanswerable inputs. Transfer beyond MemToC is positive but partial and depends on the model and presentation frame. Correctness-conditioned arbitration can be improved through fine-tuning, but gains must be evaluated jointly with correct tool use, abstention, and robustness to formulation.

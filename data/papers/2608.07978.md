# Verication-driven closed-loop multi-agent large language modelframework for code-compliant structural design

- arXiv ID: `2608.07978v1`
- Authors: Jianbin Luo, Weibin Lin, Yiran Lin, Qing Wei, Wei Guo
- Published: 2026-08-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.07978v1) | [pdf](https://arxiv.org/pdf/2608.07978v1)

## Abstract

Multi-agent large language model(LLM)systems are applied to structural design,yet most use one-shot generation and cannot verify their output,leaving themill-suited to safety-critical tasks.Rather than trusting LLM self-correction,thisframework injects feedback from an external physics-based verier into a closedrepair loop.The framework couples a three-layernite-element verication systemwith a dual-node loop.Node 1 turns code violations into hard repair constraints,Node 2 turns a four-dimensional quality score into safety-rst soft constraints,and a retrieval-augmented code base makes every violation traceable to a clause.Overve structure types and 44 cases,code compliance rises from 56.8%to 98.6%and the composite score from 63.8 to 71.4(p<0.000001),using about 5.8%lessmaterial.Removing either node degrades performance,and compliance does notchange detectably across the two backbone LLMs tested,indicating that it ishere attributed to the external verier rather than the model.The framework,the 44-case benchmark and all experiment scripts are released as open source forreplicability.

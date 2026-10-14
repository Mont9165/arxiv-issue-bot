# Hype Meets Reality: Large Language Models as Mutators in Search-based Automated Program Repair of Simulink-Stateflow Models

- arXiv ID: `2608.19347v1`
- Authors: Ayesha Irshad, Pablo Valle, Jon Ayerdi, Aitor Arrieta
- Published: 2026-08-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.19347v1) | [pdf](https://arxiv.org/pdf/2608.19347v1)

## Abstract

Search-based Automated Program Repair (APR) techniques rely on carefully designed mutation operators to explore the space of candidate fixes. Recent advances in Large Language Models (LLMs) suggest that generative models could replace such operators by dynamically proposing repairs. In this paper, we investigate this hypothesis in the context of Cyber-Physical Systems (CPSs) modeled in Simulink/Stateflow. We extend the state-of-the-art FlowRepair approach by replacing a subset of its mutation operators with LLM-generated mutations, enabling more flexible and expressive patch generation. We evaluate the approach on a benchmark of 19 real-world faulty Stateflow models across four CPS domains, using the same experimental setup as FlowRepair for controlled comparison under the same wall-clock budget. Contrary to expectations, in this controlled evaluation, the LLM-based mutation substantially degrades repair performance under the FlowRepair experimental setup. Across the tested LLM variants, the LLM-based repair produced plausible patches for 4-6 models and valid patches for 4 models, compared to 18 and 16, respectively, with the original approach. Our analysis reveals that, in this integration, LLMs struggle with precise symbolic edits, lack behavioral feedback, and generate a noisy search space that hinders effective exploration. Rather than showing a general limitation of LLMs for APR, these findings highlight fundamental limitations of naively integrating LLMs into search-based APR and motivate hybrid approaches that combine structured mutation with generative guidance.

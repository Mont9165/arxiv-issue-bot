# SynAE: A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations

- arXiv ID: `2605.22564v1`
- Authors: Shuaiqi Wang, Aadyaa Maddi, Zinan Lin, Giulia Fanti
- Published: 2026-05-21
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.22564v1) | [pdf](https://arxiv.org/pdf/2605.22564v1)

## Abstract

Today, tool-calling agents are commonly evaluated or tested on static datasets of execution traces, including input commands, agent responses, and associated tool calls. However, internal production datasets are often insufficient or unusable for testing; for example, they may contain sensitive or proprietary data, or they may be too sparse to support comprehensive testing (especially pre-deployment). In these settings, practitioners are increasingly replacing or augmenting real datasets with synthetic ones for evaluation purposes. A key challenge is quantifying the relation between these synthetic datasets and the real data. We introduce SynAE, an evaluation framework for assessing how well synthetic benchmarks for multi-turn, tool-calling agents replicate and augment the characteristics of real data trajectories. SynAE assesses the validity, fidelity, and diversity of synthetic data across four metric categories: (i) task instructions and intermediate responses, (ii) tool calls, (iii) final outputs, and (iv) downstream evaluation. We evaluate SynAE using recent agent benchmarks and test common synthetic data failure modes via realistic and controlled generation schemes. SynAE detects fine-grained variations in data validity, fidelity and diversity, and shows that no single metric is sufficient to fully characterize synthetic data quality, motivating a multi-axis evaluation of synthetic data for agent testing. A demo of SynAE is available at https://synae-2026-synae-demo.static.hf.space/index.html, with code at https://github.com/wsqwsq/SynAE.

# Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills

- arXiv ID: `2606.07412v1`
- Authors: Chuan Xiao, Zhengbo Jiao, Shaobo Wang, Wei Wang, Bing Zhao, Hu Wei, Linfeng Zhang, Lin Qu
- Published: 2026-06-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.07412v1) | [pdf](https://arxiv.org/pdf/2606.07412v1)

## Abstract

LLM-driven software engineering agents have become a central testbed for real-world language-model capability, yet their training remains limited by the availability of high-quality SWE tasks. Existing synthetic data methods typically create tasks through fixed mutation or bug-injection procedures, making the resulting distributions largely independent of the agent's own weaknesses and training progress. We introduce Socratic-SWE, a closed-loop self-evolution framework that reuses the agent's historical solving traces as a source of training signal. Rather than treating traces only as evidence for reward computation, Socratic-SWE distills them into structured agent skills that summarize recurring failures and effective repair patterns. These skills then guide the generation of targeted repair tasks in real repositories. Candidate tasks are checked through execution-based validation and scored with a solver-gradient alignment reward, so that the retained tasks are both verifiable and useful for improving the Solver. The updated Solver produces new traces, enabling the task curriculum to adapt over successive rounds. Across SWE-bench Verified, SWE-bench Lite, SWE-bench Pro, and Terminal-Bench 2.0, Socratic-SWE consistently improves over self-evolving baselines under the same compute budget, reaching 50.40% on SWE-bench Verified after three iterations. These results suggest that solving traces can serve as a scalable substrate for self-evolving SWE agents.

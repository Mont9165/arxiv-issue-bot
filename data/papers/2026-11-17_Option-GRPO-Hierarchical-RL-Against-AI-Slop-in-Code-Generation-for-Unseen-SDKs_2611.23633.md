# Option-GRPO: Hierarchical RL Against AI Slop in Code Generation for Unseen SDKs

- arXiv ID: `2611.23633v1`
- Authors: Prashank Kadam
- Published: 2026-11-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2611.23633v1) | [pdf](https://arxiv.org/pdf/2611.23633v1)

## Abstract

Large language models increasingly produce AI slop in generated code: verbose, redundant, non-idiomatic implementations that pass functional checks but bloat codebases. The problem compounds on SDKs released after the model's training cutoff, where the model has neither idiomatic priors nor compositional understanding. We present Option-GRPO, a hierarchical reinforcement learning framework that adapts a code LLM to an unseen SDK from its source code alone, without human-written usage examples or test cases, and that explicitly optimizes for both functional correctness and code elegance. Our key insight is that SDK source code contains compositional structure that defines a hierarchy of reusable code patterns (code options) which simultaneously serve as the building blocks of a curriculum and the action space for efficient policy optimization. We show that code options induce a valid semi-Markov decision process, give conditional bounds under which shorter option description length implies more concise and, in expectation, more API-efficient programs, and analyze under stated assumptions how the option hierarchy improves credit assignment by a factor of $\sqrt{T/K}$. Using Group Relative Policy Optimization (GRPO) with execution-based rewards at each curriculum level, Option-GRPO discovers SDK idioms, composes them into patterns, and assembles patterns into complete programs. Experiments on 12 unseen SDKs with a 32B-parameter base model demonstrate 61.4% pass@1, outperforming flat GRPO by 8.7 points, ExploraCoder by 11.2 points, and ReCode by 6.3 points. Option-GRPO produces solutions that use 34.7% fewer API calls and are 27% shorter than flat-GRPO outputs while maintaining higher correctness, directly attacking the slop problem.

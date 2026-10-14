# PPO guided Agentic Pipeline for Adaptive Prompt Selection and Test Case Generation

- arXiv ID: `2605.00942v1`
- Authors: Gourisetty Venkata Sai Koushik, Dama Aditya, Mahankali Harish Sai, Peddi Siddarhta, Shadab Ahmad, Vivek Yelleti
- Published: 2026-05-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2605.00942v1) | [pdf](https://arxiv.org/pdf/2605.00942v1)

## Abstract

Developing effective test cases capable of thoroughly exercising large-scale software systems is inherently difficult, especially if such systems have voluminous, complex, and deeply nested source codes. In this work, we present a novel approach for generating test cases using a reinforcement learning-driven agentic framework where Proximal Policy Optimization (PPO) is coupled with an LLM engine to guide prompt selection during test generation. Our approach consists of two phases. In Phase I, the ToT-guided optimization agent partitions and minimizes the source code by removing redundancies without changing the functional behavior of the source code. In Phase II, a PPO-based policy network is trained to solve the problem of selecting prompts among eight different prompting techniques, such as Boundary Value Analysis, Random Fuzzing, etc., based on the inputted 11-dimensional state vector representing the source code complexity metrics and live coverage metrics to direct the LLM engine towards exploring unvisited paths in the program. The PPO agent receives rewards based on a combination of increases in line and branch coverages, penalties for unexplored branches, and rewards for reducing source code length. From experiments conducted on twenty benchmark programs, it is evident that the proposed approach, PPO-LLM, outperforms CBMC, kS-LLM, and kS-LLM++ in terms of branch and line coverage in almost all cases, for various loop bound values ranging from BOUND~1 to BOUND~2000. While at BOUND~1, the coverage of branches is 100\% using PPO-LLM on the PALS suite, in comparison, it is around 86.8\% using kS-LLM++. This confirms that adaptive prompt selection driven by PPO substantially outperforms static prompting strategies on PALS type programs.

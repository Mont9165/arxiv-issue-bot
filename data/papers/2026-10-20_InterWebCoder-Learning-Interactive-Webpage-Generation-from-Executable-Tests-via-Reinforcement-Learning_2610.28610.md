# InterWebCoder: Learning Interactive Webpage Generation from Executable Tests via Reinforcement Learning

- arXiv ID: `2610.28610v1`
- Authors: Jingyu Xiao, Dasen Dai, Yuxuan Wan, Jen-tse Huang, Yintong Huo, Hongyu Zhang, Michael R. Lyu
- Published: 2026-10-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.28610v1) | [pdf](https://arxiv.org/pdf/2610.28610v1)

## Abstract

Interactive webpages underpin modern applications, but reproducing both their visual appearance and multi-step behavior remains challenging for multimodal large language models (MLLMs). Scalable training data must capture user actions, state transitions, and expected outcomes, while real-world webpage code is often entangled with irrelevant scripts and external dependencies. Moreover, existing GUI-agent-based verification provides slow and potentially unstable functional feedback. To address these challenges, we propose InterWebCoder, an efficient framework for interactive webpage code generation. InterWebCoder introduces a Test-Specification-Guided and Execution-Verified Data Synthesis pipeline that records real-world interaction trajectories and synthesizes self-contained webpage code with executable test scripts. A failureattributed repair mechanism uses runtime evidence to locate and iteratively fix errors in either the webpage code or test script. We then combine test-ID-weighted supervised fine-tuning with group-relative policy optimization, directly optimizing functional correctness and visual fidelity using test pass rates and state-level visual similarity. This replaces costly GUI-agent verification with fast, reproducible executable feedback. Our pipeline produces 1,736 verified samples from 2,058 tasks, achieving an 84.35% synthesis success rate. On IWR-Bench and Vision2Web, InterWebCoder achieves final scores of 48.54 and 48.42 with a 9B backbone, outperforming 30B-level models and Gemini-3.7-Flash while remaining competitive with Claude-Sonnet-5. It reduces reward-computation latency by over 97%, eliminates external MLLM verification costs, and accelerates end-to-end training by up to 1.4x.

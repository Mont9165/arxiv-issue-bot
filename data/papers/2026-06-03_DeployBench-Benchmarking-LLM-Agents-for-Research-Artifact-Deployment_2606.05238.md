# DeployBench: Benchmarking LLM Agents for Research Artifact Deployment

- arXiv ID: `2606.05238v1`
- Authors: Yuanli Wang, Yaoyao Qian, Yue Zhang, Hanhan Zhou, Jindan Huang, Tianfu Fu, Qiuyang Mang, Huanzhi Mao, Wenhao Chai, Wendong Fan, Liqiang Jing
- Published: 2026-06-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.05238v1) | [pdf](https://arxiv.org/pdf/2606.05238v1)

## Abstract

LLM agents have made rapid progress on software engineering and ML research tasks, but these advances often assume access to a working runnable environment. For research artifacts released alongside published papers, setting up such an environment from a fresh machine remains a major bottleneck. Existing environment setup benchmarks do not cover the full scope of research artifact deployment, which involves multi-language toolchains, system-level dependencies beyond containers (e.g. GPU/CUDA and kernel configurations), and legacy artifact compatibility. We introduce DeployBench, a multi-domain benchmark of 51 research-artifact deployment tasks spanning AI/ML, computer systems, and scientific computing, covering all these dimensions. Each task is verified by a hidden pipeline that executes the paper's designated experiment and checks its outputs. Evaluating four state-of-the-art LLMs with OpenHands yields pass-rates from 7.8% - 51.0% . Failures are dominated by a completion-judgment problem: 97 of 154 are agent-terminated self-stops, where the agent's pre-finish checks validate a different or weaker target than the paper-specific task requires. DeployBench highlights the gap between current agents and autonomous deployment, and offers a realistic testbed for scientific research agents.

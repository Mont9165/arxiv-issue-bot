# Enhancing Bug-Exposing Test Generation via Step-Level Credit Assignment and Self-Distillation from Valuable Failures

- arXiv ID: `2610.27694v1`
- Authors: Wenjie Gan, Zhaoxi Zhang, Jiahui Liang, Weikang Li, Wanyuan Wang, Li Zhang, Jian Dong
- Published: 2026-10-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.27694v1) | [pdf](https://arxiv.org/pdf/2610.27694v1)

## Abstract

Large Language Models have shown strong code generation capabilities, yet their outputs often contain subtle bugs. Automatically repairing such code requires informative tests: inputs that expose faulty behavior, paired with correct expected outputs. Recent RL-based test generation methods apply the same outcome reward to all reasoning steps, which can discourage useful reasoning and reinforce flawed steps. They also fail to effectively learn from trajectories that find bug-triggering inputs but predict incorrect outputs, leaving their verified bug-triggering progress insufficiently exploited. To address these limitations, we propose SCALF, a process-supervised RL approach that combines Step-level Credit Assignment with targeted Learning from valuable Failed trajectories. SCALF derives step-specific advantages from process rewards, allowing each reasoning stage to receive its own learning signal. It further routes trajectories that expose bugs but predict incorrect outputs to on-policy self-distillation, using execution feedback to learn from their valuable bug-triggering progress. Across three benchmarks, SCALF outperforms strong prompting and post-training baselines by up to 2.97, 5.26, and 3.53 percentage points in joint success rate, output correctness rate, and bug-triggering rate, respectively. Our code and datasets are available at https://anonymous.4open.science/r/SCALF-F4D1.

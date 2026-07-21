# CommitLLM: A Fine-Tuned Pipeline for Git Commit Message Generation

- arXiv ID: `2607.17532v1`
- Authors: Md Rafid Haque, Poojan Narendrabhai Patel, Meetkumar Vijaybhai Raychura
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.17532v1) | [pdf](https://arxiv.org/pdf/2607.17532v1)

## Abstract

Developers frequently write uninformative git commit messages such as "fix" or "update stuff", degrading the value of version-control history for code review, debugging, and onboarding. We present CommitLLM, a three-stage pipeline that generates concise, Conventional Commits-compliant messages from code diffs using a fine-tuned small language model. The system combines (1) QLoRA fine-tuning of Mistral-7B-Instruct-v0.2 on the CommitPackFT dataset, (2) constrained decoding to enforce brevity, and (3) deterministic post-processing to strip conversational artifacts and enforce format. On a 50-sample evaluation, CommitLLM achieves 98% format compliance (vs. 22% for vanilla Mistral), reduces average output length from 154.8 to 37.9 characters, and improves LLM-as-a-Judge scores from 1.97 to 3.68 out of 5. Notably, the post-processing layers contribute more to quality improvement than the fine-tuning itself, suggesting that for structured-output tasks, treating the LLM as a component in a deterministic pipeline is more effective than optimizing the model alone. The entire system runs on a single consumer GPU (NVIDIA T4, 16 GB VRAM).

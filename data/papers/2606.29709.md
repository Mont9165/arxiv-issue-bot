# Bash-Commenter: Leveraging Syntax-Aware Preference Optimization to Reinforce Large Language Model for Bash Code Comment Generation

- arXiv ID: `2606.29709v1`
- Authors: Lei Yu, Jingyuan Zhang, Xin Wang, Li Yang, Fengjun Zhang, Peng Wang, Jia Xu, Jiajia Ma
- Published: 2026-06-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.29709v1) | [pdf](https://arxiv.org/pdf/2606.29709v1)

## Abstract

Bash script comprehension is challenging due to Bash's syntactic freedom and complex command structures. Despite its critical role in system administration, Bash scripts often lack adequate comments, hindering readability and maintainability. Existing automated comment generation approaches face two main challenges: (1) limited training datasets that inadequately represent real-world Bash usage patterns; and (2) insufficient understanding of Bash-specific concepts by Large Language Models (LLMs). To address these, we propose Bash-Commenter, an advanced comment generation method based on LLaMA-3.1-8B. First, we construct a comprehensive dataset of complex, multi-line Bash scripts with high-quality comments. Second, we conduct Continual Pre-training (CPT) on large-scale Bash data, followed by Supervised Fine-tuning (SFT), strengthening the model's foundational knowledge of Bash syntax and semantics. Finally, we introduce Syntax-Aware Preference Optimization (SAPO), which constructs preference pairs by applying atomic operations to a script's Abstract Syntax Tree (AST), creating minimal pairs of correct and subtly incorrect scripts for fine-grained semantics learning. Our method outperforms state-of-the-art baselines, achieving 33.40% BLEU-4, 58.26% METEOR, and 57.03% ROUGE-L for 1,064 single-line commands, and 22.15% BLEU-4, 43.89% METEOR, and 32.80% ROUGE-L for 1,046 multi-line scripts. Human and LLM evaluations further confirm superior comment quality in correctness, completeness, and naturalness.

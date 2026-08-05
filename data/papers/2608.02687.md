# PolicyGuard: Prompt-Configurable Semantic DLP for LLM Coding Agents

- arXiv ID: `2608.02687v1`
- Authors: Kyutae Park, Jungwon Kim, Daeyeol Shim
- Published: 2026-08-03
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.02687v1) | [pdf](https://arxiv.org/pdf/2608.02687v1)

## Abstract

AI coding agents accept free-form natural language prompts that may inadvertently contain credentials, personally identifiable information (PII), or proprietary business data. Existing data loss prevention (DLP) solutions rely on rigid regex patterns, model fine-tuning, or vendor-managed classifiers with limited customizability. We present PolicyGuard, a pre-model interception framework that classifies user prompts using an LLM guided by a natural language policy file. Our key contributions are: (1) the policy-as-prompt paradigm, where DLP classification criteria are defined entirely in a plaintext policy document editable by non-engineers without code changes or model retraining; (2) a sealed evaluation protocol with template-family-level data splits, hidden holdouts, and frozen test sets to rigorously assess generalization; and (3) a comprehensive empirical evaluation across 2,000 multilingual prompts demonstrating 96.5% effective block rate (EBR) with only 3.0% false positive rate (FPR) on a frozen test set of 927 prompts, and perfect 100% accuracy on a 217-prompt hidden holdout. Information-matched baseline experiments show that PolicyGuard's natural language format significantly outperforms equivalent content in JSON format (McNemar chi-squared = 31.58, p < 0.001) and dramatically outperforms zero-shot classification (Cohen's h = 0.915). Cross-model portability experiments demonstrate that the same policy achieves 86.4-96.5% EBR across four different LLMs without modification.

# Aging of Prompt Engineering Techniques Across LLM Versions

- arXiv ID: `2608.24641v1`
- Authors: Anastasiia Rudyk, Julian Oertel, Regina Hebig
- Published: 2026-08-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.24641v1) | [pdf](https://arxiv.org/pdf/2608.24641v1)

## Abstract

Prompt engineering and prompt engineering techniques (PETs) have become an integral part of software engineering for AI systems. However, new LLMs are released frequently and it remains unclear how the effectiveness of prompt engineering techniques changes across successive generations of Large Language Models (LLMs). To this end, we conduct a partial replication of the study by Khojah et al. (2025). We evaluate five techniques - Zero-Shot, Few-Shot, Chain-of-Thought (CoT), Contrastive Chain-of-Thought (CCoT), and an adapted version of Program-of-Thought (PoT) - on six instruction-tuned models grouped into three version pairs: GPT-3.5-Turbo/GPT-4o, Qwen2 7B Instruct/Qwen2.5 7B Instruct, and Mistral-7B-Instruct/Mistral-Large. We use a cleaned subset of the CodePromptEval dataset with 218 context-rich Python functions and 19,620 total generations assessed via pass@k-based functional correctness to evaluate model pairs on function-level code generation tasks. We show that prompt engineering "ages" in a model-family-specific way: Newer GPT models exhibit diminishing or even negative marginal gains from structured prompting, suggesting that instruction-following and reasoning scaffolds are increasingly internalized, whereas Qwen models continue to benefit substantially from Few-Shot and CCoT. Mistral models show mixed behavior with persistent gains from CCoT but attenuated benefits from CoT and PoT. Our results imply that effective prompting strategies must be adapted per model family and generation rather than transferred unchanged. This motivates future work on adaptive, model-aware prompting and broader, multi-dimensional code quality evaluation.

# Do Machines Struggle Where Humans Do? LLM and Human Comprehension of Obfuscated Code

- arXiv ID: `2606.31725v1`
- Authors: Jack Le, Anh H. N. Nguyen, Tien N. Nguyen
- Published: 2026-06-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.31725v1) | [pdf](https://arxiv.org/pdf/2606.31725v1)

## Abstract

While code obfuscation impairs human code comprehension, it remains unclear if large language models share these failure modes. Building directly on a recent human study of program comprehension under code obfuscation, we evaluate whether large language models share the failure modes that obfuscation induces in human programmers. Evaluating several LLMs with five obfuscation tiers using the Block Model, we localize comprehension failures at the atom, block, relational, and macro levels. We find that reasoning-tuned models demonstrate significant alignment with human difficulty patterns across experience levels, whereas instruction and coder-tuned models show near-zero correlation. Chain-of-Thought trace length tracks task difficulty across tasks. Results indicate that performance under control-flow flattening degrades in proportion to state-space complexity, while adversarial identifier renaming disrupts comprehension through the interaction of semantic displacement and identifier-level interference. These findings suggest that reasoning-tuned LLMs approximate human sensitivity to code complexity more effectively than instruction-tuned variants.

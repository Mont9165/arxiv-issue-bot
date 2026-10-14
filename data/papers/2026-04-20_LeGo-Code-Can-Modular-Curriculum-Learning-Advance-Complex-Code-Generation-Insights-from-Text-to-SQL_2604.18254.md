# LeGo-Code: Can Modular Curriculum Learning Advance Complex Code Generation? Insights from Text-to-SQL

- arXiv ID: `2604.18254v1`
- Authors: Salmane Chafik, Saad Ezzini, Ismail Berrada
- Published: 2026-04-20
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.18254v1) | [pdf](https://arxiv.org/pdf/2604.18254v1)

## Abstract

Recently, code-oriented large language models (LLMs) have demonstrated strong capabilities in translating natural language into executable code. Text-to-SQL is a significant application of this ability, enabling non-technical users to interact with relational databases using natural language. However, state-of-the-art models continue to struggle with highly complex logic, particularly deeply nested statements involving multiple joins and conditions, as well as with real-world database schemas that are noisy or poorly structured. In this paper, we investigate whether curriculum learning can improve the performance of code-based LLMs on Text-to-SQL tasks. Employing benchmarks including Spider and BIRD, we fine-tune models under different curriculum strategies. Our experiments show that naive curriculum, simply ordering training samples by complexity in a single epoch, fails to surpass standard fine-tuning due to catastrophic forgetting. To overcome this, we propose a Modular Adapter Composition (MAC) strategy. By sequentially training tier-specific adapters on incremental complexity levels (Easy to Extra-Hard), we create a scaffolded learning environment that improves performance on complex queries. Our approach not only produces measurable performance gains on the Spider and BIRD benchmarks but also provides a flexible, "Lego-like" architecture, allowing models to be composed and deployed based on specific schema difficulty requirements. These findings demonstrate that structured, modular learning is a superior alternative to monolithic fine-tuning for mastering the syntax and logic of complex code generation.

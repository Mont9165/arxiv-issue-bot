# SQLoom: Set-Contrastive Learning of Syntactic, Semantic, and Logical Dependencies for Text-to-SQL

- arXiv ID: `2611.03298v1`
- Authors: Hao Fu, Degang Sun, Wan Wei, Jinxia Wei, Chun Long, Peng Gao
- Published: 2026-11-02
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.03298v1) | [pdf](https://arxiv.org/pdf/2611.03298v1)

## Abstract

Text-to-SQL translates natural language questions into SQL queries, enabling database access without writing SQL. Fine-tuning open-weight large language models (LLMs) is cost-effective, but existing methods treat SQL as ordinary text and optimize token-level likelihood without explicitly modeling its syntactic, semantic, and logical requirements. Thus, a single incorrect alias or comparison operator can invalidate a query while contributing little to training loss. We propose SQLoom, a constraint-aware fine-tuning framework with supervision at three levels: syntactic validity under SQL grammar and database schema, semantic alignment between query decisions and the question, and logical consistency across dependent clause decisions. SQLoom extends supervised fine-tuning with a unified set-contrastive objective favoring sets of correct outputs over minimally different incorrect ones at each level. LLM agents propose this supervision, which a SQL parser and execution on counterexample databases verify. We also release Spider-Refined, a training dataset correcting 378 flawed Spider annotations and enriching database schemas. Experiments on Spider, BIRD, and three perturbed Spider variants show that SQLoom improves execution accuracy for Qwen3-1.7B from 62.9% zero-shot to 88.7% on Spider development, reaching 89.2% on Spider test and 73.4% on BIRD development. It outperforms fine-tuning, reinforcement learning, and agent-based baselines with up to 70 billion parameters. On question perturbations, SQLoom loses at most 0.6 accuracy points versus up to 12.1 for agent-based methods. It generates SQL in a single pass at 0.42s per query, 23$\times$ faster than a GPT-4-based agent method. These results demonstrate the effectiveness of set-contrastive supervision over token-level training.

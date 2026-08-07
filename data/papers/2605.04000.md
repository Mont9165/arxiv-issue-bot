# Mitigating False Positives in Static Memory Safety Analysis of Rust Programs via Reinforcement Learning

- arXiv ID: `2605.04000v1`
- Authors: P Akilesh, Leuson Da Silva, Foutse Khomh, Sridhar Chimalakonda
- Published: 2026-05-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.04000v1) | [pdf](https://arxiv.org/pdf/2605.04000v1)

## Abstract

Static analysis tools are essential for ensuring memory safety in Rust programs, particularly as Rust gains adoption in safety-critical domains. However, existing tools such as Rudra and MirChecker suffer from high false positive rates, which diminish developer trust, increase manual review effort, and may obscure genuine vulnerabilities. This paper presents a novel reinforcement learning (RL)-based approach for automatically classifying and suppressing spurious warnings in static memory safety analysis for Rust. To achieve this, we design an RL agent that learns a warning suppression policy by extracting contextual features from Rust's Mid-level Intermediate Representation (MIR) and optimizing its decisions through interaction with static analysis outputs. To improve decision quality, we integrate dynamic validation via cargo-fuzz as an auxiliary feedback mechanism, allowing the agent to selectively validate suspicious warnings through targeted fuzz testing. Our evaluation shows that the proposed approach significantly outperforms state-of-the-art LLM-based baselines, achieving 65.2% accuracy and an F1 score of 0.659, an improvement of 17.1% over the best LLM baseline. With a recall of 74.6%, our method successfully identifies nearly three-quarters of true bugs while substantially reducing false positives, improving precision from 25.6% in raw Rudra output to 59.0%. Incorporating dynamic fuzzing further boosts performance, yielding additional improvements of 10.7 percentage points in accuracy and 8.6 percentage points in F1 score over the RL-only variant. Overall, our work demonstrates that combining reinforcement learning with hybrid static-dynamic analysis can substantially reduce false positives and improve the practical usability of memory safety verification tools for Rust.

# Towards LLM-assisted High-Quality Property Generation for Solidity Smart Contracts

- arXiv ID: `2607.23308v1`
- Authors: Muhammad Wahid, Shahzaib Khan, Mashhood Ali, Muhammad Hassan, Muhammad Naiman Jalil, Affan Rauf
- Published: 2026-07-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.23308v1) | [pdf](https://arxiv.org/pdf/2607.23308v1)

## Abstract

The immutable nature of smart contracts makes it challenging to fix and patch bugs once they are deployed to a blockchain. This implies that security vulnerabilities may be exposed to possible exploitation for a longer period, necessitating comprehensive pre-deployment testing. Property-based testing combined with fuzzing has proven itself as a promising technique for uncovering vulnerabilities. Traditionally, system properties are written by human experts, which is time-consuming and consequently expensive.With the recent advancement in Large Language Models (LLMs) and their ability to 'understand' natural language and code semantics, it may be possible to generate effective properties. This study, leverages state-of-the-art LLMs to generate high-quality properties for Soliditybased smart contracts. We measure the quality of the generated properties using mutation testing. Our results show that LLMs have the potential to generate high-quality properties that are close to those written by human experts. We extensively evaluate LLMs using various prompting techniques (e.g., zero shot, few shot, and prompt chaining). Overall, we find that Gemini Pro 1.5, when combined with prompt chaining, achieves the highest average mutation score of 25.99% among all studied configurations, closely approaching the human written benchmark of 31.75%. However, our per contract analysis reveals notable variance, particularly for the LibBit contract, where Gemini Pro 1.5 under prompt chaining achieves a mutation score of 74.34%, which is on par with human written properties (74.83%). This highlights that while average performance is informative, individual contract level results demonstrate that LLMs can, in some cases, match expert level property generation.

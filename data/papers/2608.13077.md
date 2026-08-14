# How Powerful are LLMs in Generating Formal Program Specifications?

- arXiv ID: `2608.13077v1`
- Authors: Fanpeng Yang, Xing Li, Shuling Wang, Jie An, Zeyu Sun, Shenghua Feng, Wenhan Wang, Weiyi Wang, Naijun Zhan, Fanjiang Xu
- Published: 2026-08-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.13077v1) | [pdf](https://arxiv.org/pdf/2608.13077v1)

## Abstract

Formal verification provides strong guarantees of software correctness, but its adoption is limited by the high cost of writing precise formal specifications. While recent large language models (LLMs) have shown strong capabilities in theorem proving and verified code generation, their true ability to generate program specifications remains unclear. Existing evaluations require either verifying implementation conformance or proving semantic equivalence between specifications, both of which are formidably difficult and may conflate proof difficulty with specification quality. To address this problem, we introduce Coins, a Rocq based evaluation framework that assesses specification quality by instantiating specifications under evaluation on trusted test cases and generating concrete proof obligations. This design aligns with the asymmetric nature of formal reasoning, where successful proofs provide reliable evidence while proof failures are inherently ambiguous. Using Coins, we conduct a large scale study on HumanEval with a curated set of human written Rocq specifications. Our results show that specification generation remains a formidable challenge, and that verification complexity can obscure genuine differences in specification quality. Overall, we find that accurate specification evaluation, rather than model scaling alone, is central to understanding the power of LLMs for specification synthesis, and that test case based formal reasoning offers a more faithful and discriminative measure of progress.

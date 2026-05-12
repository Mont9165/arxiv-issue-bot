# ParityFuzz: Finding Inconsistencies across Solidity Compilers via Fine-Grained Mutation and Differential Analysis

- arXiv ID: `2605.09051v1`
- Authors: Bowei Su, Mingxi Ye, Yuhong Na, Peilin Zheng, Zibin Zheng
- Published: 2026-05-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.09051v1) | [pdf](https://arxiv.org/pdf/2605.09051v1)

## Abstract

The Solidity smart contract ecosystem has rapidly grown, leading to multiple compilers targeting different blockchain platforms or improving compilation efficiency. Although many compilers aim to be compatible with the primary Solidity compiler (Solc), significant inconsistencies in compilation and execution remain. These inconsistencies hinder contract migration, mislead developers during debugging, and may introduce exploitable vulnerabilities, causing financial losses. Existing testing techniques mainly focus on bugs within a single compiler or perform differential testing in the same execution environment. However, they are insufficient for detecting cross-compiler inconsistencies, as they lack mechanisms to explore triggering conditions and compare bytecode across environments.
  We propose ParityFuzz, a cross-compiler differential testing framework for Solidity. It operates in three stages. First, it derives mutation rules, including syntax- and boundary-oriented rules, by analyzing compilers and execution environments. Second, it uses reinforcement learning to select effective mutation rules for test generation. Third, it compiles and executes programs across multiple compilers, then normalizes and compares results to detect inconsistencies.
  Our evaluation shows ParityFuzz is efficient and effective. It achieves up to 18x higher compilation success rate and 1.8x higher code coverage than state-of-the-art fuzzers. It uncovers 64 previously unknown inconsistencies across six compilers. Notably, 11 issues have been fixed, and our findings received a bounty from the Polkadot community.

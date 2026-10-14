# Finding and Understanding Miscompilation Bugs in the Solidity Compiler

- arXiv ID: `2607.07217v1`
- Authors: Bhargava Shastry
- Published: 2026-07-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2607.07217v1) | [pdf](https://arxiv.org/pdf/2607.07217v1)

## Abstract

Smart contract compilers are critical to ensuring the correctness of public blockchains whose defining characteristics are open-source and immutable code. We created SolSmith, a semantics-aware differential fuzz testing tool, to improve the quality of the Solidity compiler -- the most popular compiler for the Ethereum blockchain -- and spent over three years finding compiler defects that produce incorrect code. We call these defects miscompilation bugs. During this time period, we have discovered 25 miscompilation bugs that went unnoticed, some for multiple years. Our first contribution is to make compiler testing more rigorous. SolSmith achieves this goal by generating valid test programs that are likely to stress test code generation and optimization components. This helps SolSmith find bugs missed during routine testing that could potentially have serious implications for smart contracts and their users. Our second contribution is a qualitative and quantitative analysis of miscompilation bugs that we found in the Solidity compiler. We classify miscompilation bugs found by SolSmith based on their nature, root-causes, and impact on end-users. This sheds light on some pitfalls of optimizing compilers.

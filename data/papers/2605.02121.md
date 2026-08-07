# SCRIBE: Practical Static Binary Patching via Binary-Aware Recompilation of Decompiled Code

- arXiv ID: `2605.02121v1`
- Authors: Han Dai, Soumyakant Priyadarshan, Abdullah Imran, Ruoyu Wang, Antonio Bianchi
- Published: 2026-05-04
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.02121v1) | [pdf](https://arxiv.org/pdf/2605.02121v1)

## Abstract

When source code or the original toolchain is unavailable, patching binaries is difficult because it requires editing low-level assembly code directly. As an alternative, one can decompile the binary, apply the patch at the source level, and then recompile the modified code. However, as this paper demonstrates, this workflow is hindered by pervasive syntactic and semantic inaccuracies in the output of modern decompilers, many of which prior work has overlooked. To address these challenges, we present SCRIBE, a patching framework that handles syntactic and semantic issues in decompiled code, improving both recompilation success and correctness. SCRIBE's novel "binary-aware" recompilation approach repairs semantic inaccuracies in decompiler output by leveraging information extracted directly from the original binary. In our evaluation, SCRIBE resolved approximately 81% of previously incorrect functions produced by the Hex-Rays decompiler, demonstrating the effectiveness of its approach. Moreover, we show that, using SCRIBE, it is possible to patch 13 of 14 real-world CVEs without access to the original source code and without performing any manual binary editing. To further validate our findings, we conducted a user study with 18 participants. Using SCRIBE, participants achieved 100% patching success, compared to 3.7% without it. Finally, we asked three large language models to generate source-level patches via SCRIBE; all three achieved 100% success when using the framework, demonstrating its potential to enable fully automated patching. Overall, these results indicate that SCRIBE makes source-level patching of binaries accessible and reliable, even without access to the original source.

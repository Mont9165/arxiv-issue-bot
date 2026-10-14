# Behavior Specification-Guided Program Synthesis for Binary Deobfuscation

- arXiv ID: `2608.20628v1`
- Authors: Kangchen Zhu, Shangwen Wang, Zhiliang Tian, Zhouyang Jia, Xiaoling Li, Jun Ma, Jie Yu, Xiaoguang Mao
- Published: 2026-08-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.20628v1) | [pdf](https://arxiv.org/pdf/2608.20628v1)

## Abstract

Deobfuscation is critical to reverse engineering and security analysis because it restores the readability and analyzability of obfuscated code. However, existing research primarily focuses on source-code deobfuscation, while binary-level deobfuscation remains largely underexplored despite its practical importance when source code is unavailable. Existing binary deobfuscation methods typically decompile binaries into pseudocode and then apply structural transformations. However, because compilation discards high-level semantics such as precise type information and source-level structures, this decompilation-based paradigm often produces low-quality code and provides limited assurance that the recovered code preserves the runtime behavior of the original program. To address these limitations, we propose a paradigm shift from structural transformation to behavior-driven synthesis. Our core insight is that although obfuscation distorts a program's internal structure, semantics-preserving transformations must retain its observable execution behavior. Based on this insight, we introduce BinMirror, an approach that reformulates binary deobfuscation as a behavior-specification-guided program synthesis task. By treating dynamic execution traces and interaction snapshots as behavioral specifications, BinMirror synthesizes high-quality source code and validates it against runtime observations collected from heavily obfuscated binaries. Extensive evaluations on 1.5 million synthetically obfuscated binaries show that BinMirror significantly outperforms state-of-the-art baselines, achieving a unit-test Pass@1 of 74.5% under extreme obfuscation. These results demonstrate the practical utility of BinMirror in restoring semantic clarity for real-world security analysis.

# GapForge: Directed Compiler Fuzzing via Coverage-Gap Analysis

- arXiv ID: `2607.15762v1`
- Authors: Mingxuan Zhu, Qingyuan Liang, Junjie Chen, Zhihong Xue, Dan Hao
- Published: 2026-07-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.15762v1) | [pdf](https://arxiv.org/pdf/2607.15762v1)

## Abstract

Modern compiler codebases (e.g., GCC and LLVM) are large and complex, making comprehensive coverage across diverse code regions highly challenging. Most existing test generation techniques ignore characteristics of the target code, producing test programs that exercise only a limited subset of it. Consequently, substantial compiler regions remain insufficiently tested, leaving persistent long-tail coverage gaps that survive across releases. Even existing white-box techniques achieve limited coverage on large-scale compilers. To improve compiler coverage, especially for hard-to-reach edge regions, we present GapForge, a targeted LLM-based test generation technique that reasons about coverage gaps. Unlike program-driven techniques that generate diverse inputs without modeling which regions they exercise, and unlike whole-file summarization that yields coarse guidance, GapForge treats coverage gaps as explicit region-level targets in three steps. First, it prioritizes files via coverage-driven scoring that favors large, undercovered files. Second, it pairs each uncovered line span with its enclosing covered context and performs path-difference analysis to infer fine-grained triggering requirements: the program structures and compilation options needed to reach the uncovered region. Third, it synthesizes prompts from these requirements and previously failed prompts, using coverage feedback to guide next-round selection. On GCC 14.3.0 and LLVM 19.1.0, GapForge significantly outperforms eight state-of-the-art techniques. Within 72 hours, it achieves 68.13% and 69.11% coverage on core compiler modules in GCC and LLVM, surpassing the white-box technique WhiteFox by 24,736 and 19,798 additional lines, respectively. Moreover, GapForge discovers 12 real-world compiler failures (5 in GCC, 7 in LLVM), including 8 crashes and 4 miscompilations, with each component contributing to its performance.

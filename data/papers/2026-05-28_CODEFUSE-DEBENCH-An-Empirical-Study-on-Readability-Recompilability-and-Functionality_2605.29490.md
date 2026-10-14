# CODEFUSE-DEBENCH: An Empirical Study on Readability, Recompilability, and Functionality

- arXiv ID: `2605.29490v1`
- Authors: Puzhuo Liu, Yuhan Huang, Jianlei Chi, Peng Di, Yu Jiang
- Published: 2026-05-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2605.29490v1) | [pdf](https://arxiv.org/pdf/2605.29490v1)

## Abstract

Binary decompilation aims to recover binaries into high-level source code, but existing evaluations mainly rely on syntactic similarity or single-axis readability metrics, which fail to capture practical reusability. We propose a reusability-driven evaluation paradigm that measures decompiler quality along three orthogonal dimensions: readability, recompilability, and functionality. We present DEBENCH, the first automated framework for multidimensional decompilation evaluation. DEBENCH contains 240 atomic test functions, organized into 8 source files and compiled into 640 binaries. It combines LLM-as-judge readability scoring with URAF (18 sub-dimensions), iterative compile-and-repair under a fixed 50-iteration budget, and Frida-based differential dynamic tracing at the program, function, and instruction levels. We evaluate five mainstream decompilers and three repair LLMs. Our study reveals four findings. First, the reusability cliff is steep: the best decompiler-LLM pair reaches 22.3% Exact+Partial program-level behavioral overlap but only 1.2% exact stdout match, nearly 50 points below recompilability. Second, settings that maximize readability do not maximize functionality: -O3 yields the lowest readability but the highest functionality, and Clang gives lower readability than GCC but 2.6x higher functionality. Third, cross-decompiler variation at the functional level is 20x, far larger than the 1.6x cross-LLM variation, showing that progress depends more on decompiler engines than larger repair models. Fourth, failures fall into three categories: syntactic noise, type-system collapse (about 19% of repair errors), and irreversible upstream losses such as ARM64 relocation idioms and C++ ABI features.

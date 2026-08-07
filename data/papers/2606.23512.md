# Source-Free Detection and Impact Analysis of Compiler Optimization Problems in Mobile Applications

- arXiv ID: `2606.23512v1`
- Authors: Han Hu, Xiaoheng Xie, Bo Sun, Jian Gu, Gang Fan, Li Li
- Published: 2026-06-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.23512v1) | [pdf](https://arxiv.org/pdf/2606.23512v1)

## Abstract

Mobile apps frequently suffer from performance issues such as frame drops, overheating, and excessive power consumption. While developers optimize algorithms and debug code, a critical bottleneck often goes unnoticed: native libraries compiled with low optimization levels (O0/O1 instead of O2/O3). Because these libraries execute without functional errors, the resulting performance degradation remains hidden in production apps, affecting millions of users.
  We present \textsc{OptDetect}, a source-free framework that detects compiler optimization problems directly from app binaries without requiring source code or build metadata. \textsc{OptDetect} handles mixed optimization levels within a single binary through a pipeline of binary disassembly, chunk-level classification, and weighted score aggregation, achieving 93.0\% accuracy on controlled datasets and 81.9\% on real-world datasets. Applying \textsc{OptDetect} to 21,972 native libraries from 830 top-ranked Google Play apps, we find that 30.5\% of libraries use low optimization levels, affecting 91.7\% of apps.
  Through case studies on 12 production apps (6 commercial, 6 open-source), we demonstrate that fixing detected issues reduces CPU instructions by 10-63\% (median: 20.5\%) for commercial apps and 15-58\% (median: 32\%) for open-source apps, with performance complaints decreasing by a median of 42\% and ratings increasing by a median of 0.14 points. Further investigation reveals a previously overlooked root cause: widely-used third-party libraries are themselves distributed at low optimization levels, with 49.7\% of 1,073 libraries in a major repository exhibiting this problem. These findings highlight the need for automated detection tools and industry-wide optimization standards.

# An Empirical Analysis of Cross-OS Portability Issues in Python Projects

- arXiv ID: `2609.25531v1`
- Authors: Denini Silva, MohamadAli Farahat, Marcelo d'Amorim
- Published: 2026-09-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.25531v1) | [pdf](https://arxiv.org/pdf/2609.25531v1)

## Abstract

While Python is designed as a cross-platform language, real-world applications encounter portability failures when deployed across different operating systems. We present the first large-scale empirical study of cross-OS portability issues in Python, analyzing 2,042 open-source repositories using two complementary approaches: systematic cross-OS test reexecution and manual analysis of GitHub issues. Our cross-platform testing of 500 projects reveals that 11.2% exhibit OS-dependent test failures. Through systematic analysis of 240 GitHub issues, we confirm 102 genuine portability problems spanning 95 additional projects. We develop a comprehensive taxonomy identifying 7 primary failure categories - with file/directory operations, process management, and library dependencies being most prevalent - along with 24 distinct sub-categories, 15 diagnostic signatures, and 4 systematic repair patterns. Our evaluation reveals that existing static analysis tools provide minimal support for portability detection, while large language models achieve 40-79% accuracy in identifying issues and 50-77% success in generating fixes when provided with structured guidance. Through 33 contributed pull requests, we demonstrate practical applicability and developer acceptance (17 merged, zero rejected) of our findings. This work establishes the first comprehensive baseline for understanding and addressing cross-OS portability issues in Python, providing actionable insights for developers, tool designers, and the broader research community.

# CppPerf: An Automated Pipeline and Dataset for Performance-Improving C++ Commits

- arXiv ID: `2605.10890v1`
- Authors: Tommy Ho, Khashayar Etemadi, Zhendong Su
- Published: 2026-05-11
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.10890v1) | [pdf](https://arxiv.org/pdf/2605.10890v1)

## Abstract

Recent progress in automated repair of performance bugs demands realistic, executable benchmarks. However, existing C++ performance benchmarks are largely built from competitive programming submissions, and recent real-world benchmarks predominantly target Python and .NET. To fill this gap, we present CppPerf-Mine, a configurable pipeline that mines execution-time-improving patches from open-source C++ repositories on GitHub by combining structural commit filtering, an LLM-based commit classifier, and a containerized build & test stage that produces fully reproducible Docker images for each patch. Using CppPerf-Mine, we build CppPerf-DB, a benchmark comprising 347 manually verified patches from 42 mature C++ repositories, 39% of which are multi-file, enabling the evaluation of repository-level repair tools. In our preliminary study, OpenHands correctly fixes only 13.5% of the patches in CppPerf-DB, confirming that real-world C++ performance repair remains an open challenge. CppPerf-Mine and CppPerf-DB are open-source and publicly available at: https://doi.org/10.5281/zenodo.20097425. In addition, a demonstration video is available at: https://www.youtube.com/watch?v=nixlupIgSdM.

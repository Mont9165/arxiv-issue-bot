# Characterizing Real-World Bugs in Tile Programs for Automated Bug Detection

- arXiv ID: `2605.19652v1`
- Authors: Ravishka Rathnasuriya, Zihe Song, Nidhi Majoju, Aaryaa Moharir, Tingxi Li, Wei Yang, Tao Xie
- Published: 2026-05-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.19652v1) | [pdf](https://arxiv.org/pdf/2605.19652v1)

## Abstract

Tile-based programming frameworks are increasingly adopted to write high-performance GPU kernels in domains such as deep learning and scientific computing. While these frameworks enhance productivity and hardware utilization, their multi-stage compilation pipelines introduce distinct code generation bugs that are tightly coupled to input shapes, data types, and backend targets. These bugs often manifest as silent correctness or performance issues, making them difficult to detect using existing compiler testing tools. Additionally, the unique programming conventions of tile domain-specific languages complicate root cause identification, while fixing such bugs demands specialized knowledge of tile abstractions and compilation pipelines. Despite the growing adoption of tile-based systems, their code generation bugs remain largely unexplored. This paper presents the first systematic study of tile-program code generation bugs. We curate 401 bug reports from GitHub and identify 301 tile-program codegen bugs for analysis, categorizing the root causes, symptoms, input patterns, test oracles that trigger these bugs, and the strategies used to fix bugs. Our study provides foundational insights for building debugging, testing, and repair tools tailored to tile-based compiler infrastructures.

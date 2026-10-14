# XRFix: Exploring Performance Bug Repair of Extended Reality Applications with Large Language Models

- arXiv ID: `2608.21718v1`
- Authors: Jingwen Wu, Hanyang Guo, Hong-Ning Dai, Xiapu Luo
- Published: 2026-08-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.21718v1) | [pdf](https://arxiv.org/pdf/2608.21718v1)

## Abstract

As an emerging technology, Extended Reality provides end-users with an immersive experience of interacting with virtual and physical environments. Unlike traditional software, the execution of XR applications involves more computationally complex operations, such as 3D scene rendering, real-time animation, and process simulations. Inefficient coding practices during the software development of XR applications may cause various performance bugs, degrading user experience and even causing motion sickness. Thus, it is an urgent need to develop an automated program repair framework for fixing performance bugs in complex XR programs. However, it is non-trivial to achieve this goal due to several technical challenges: (1) a lack of a real-world XR codebase and bug dataset, (2) no accurate bug detection tool, and (3) no effective bug-fixing tool designed for XR performance bugs. To tackle these challenges, we present a novel large language model-based framework, namely XRFix, to repair performance bugs for open-source XR programs. We first construct a corpus of domain-specific performance bugs built with a codebase from 23 open-source XR projects and a dataset of XR-related bugs containing 104 real-world bugs. Then, we tailor two static analysis tools for accurately detecting bugs in both C# scripts and asset files. Last, we design different prompts to instruct LLMs to fix XR bugs in three types of bug scenarios with different complexities, i.e., single-line level, function level, and class level. We conduct extensive experiments on five off-the-shelf LLMs to evaluate the bug-fixing performance of XRFix. We also compare our XRFix with three SOTA APR approaches. Through static analysis, reference answer comparison, and manual inspection, we demonstrate that our XRFix can effectively fix XR bugs, outperforming SOTA APR methods.

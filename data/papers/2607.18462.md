# Beyond Resolved Rate: A Non-Functional Quality Study

- arXiv ID: `2607.18462v1`
- Authors: Xin Sun, Daniel Ståhl, Kristian Sandahl, Christoph Kessler
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.18462v1) | [pdf](https://arxiv.org/pdf/2607.18462v1)

## Abstract

Repository-level coding benchmarks typically measure progress in model capability by comparing the resolved rates of later and earlier models. However, this focus overlooks whether the non-functional quality of their generated patches has also changed across model generations. This study investigates whether later models produce functionally correct patches with better non-functional characteristics than earlier models on comparable repository-level repair tasks. We conducted two case studies involving four Claude and DeepSeek models on SWE-bench Lite. Using the same SWE-agent functional repair setting, we evaluated the generated patches with CodeQL, CodeScene, CPU time, and peak memory. Our primary analysis compared the models on commonly resolved instances. The static analysis results showed that most CodeQL paired differences were zero and that no CodeQL or CodeScene comparison remained significant after Holm correction. CPU time differences were small and inconsistent across model families, while peak memory usage was slightly higher for the later models under the benchmark test workload, with small absolute differences. Differences in individual CodeQL rules and CodeScene categories varied across model families and did not survive multiple-comparison correction. Overall, later models resolved more instances but showed no consistent improvement in the measured non-functional indicators on tasks solved by both models. Through this study, we hope to encourage a more comprehensive evaluation of models' practical software engineering capabilities.

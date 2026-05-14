# An Extensive Replication Study of the ABLoTS Approach for Bug Localization

- arXiv ID: `2605.11790v1`
- Authors: Feifei Niu, Enshuo Zhang, Christoph Mayr-Dorn, Wesley Klewerton Guez Assunção, Liguo Huang, Jidong Ge, Bin Luo, Alexander Egyed
- Published: 2026-05-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.11790v1) | [pdf](https://arxiv.org/pdf/2605.11790v1)

## Abstract

Bug localization is the task of recommending source code locations (typically files) that contain the cause of a bug and hence need to be changed to fix the bug. Along these lines, information retrieval-based bug localization (IRBL) approaches have been adopted, which identify the most bug-prone files from the source code space. In current practice, a series of state-of-the-art IRBL techniques leverage the combination of different components (e.g., similar reports, version history, and code structure) to achieve better performance. ABLoTS is a recently proposed approach with the core component, TraceScore, that utilizes requirements and traceability information between different issue reports (i.e., feature requests and bug reports) to identify buggy source code snippets with promising results. To evaluate the accuracy of these results and obtain additional insights into the practical applicability of ABLoTS, we conducted a replication study of this approach with the original dataset and also on two extended datasets (i.e., additional Java dataset and Python dataset). The original dataset consists of 11 open source Java projects with 8,494 bug reports. The extended Java dataset includes 16 more projects comprising 25,893 bug reports and corresponding source code commits. The extended Python dataset consists of 12 projects with 1,289 bug reports. While we find that the TraceScore component, which is the core of ABLoTS, produces comparable or even better results with the extended datasets, we also find that we cannot reproduce the ABLoTS results, as reported in its original paper, due to an overlooked side effect of incorrectly choosing a cut-off date that led to test data leaking into training data with significant effects on performance.

# Method-level Change-proneness: A Better Metric for Black-box Test Suite Minimization

- arXiv ID: `2605.15232v1`
- Authors: Md Siam, Kazi Sakib
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.15232v1) | [pdf](https://arxiv.org/pdf/2605.15232v1)

## Abstract

Test Suite Minimization (TSM) reduces the size of test suites while preserving their fault detection capability. In black-box TSM, reduction is performed without analyzing production code. While several black-box TSM approaches have explored metrics like test logs or test similarity, those often suffer from scalability and efficiency issues. On the other hand, change-proneness (CP), recently emerged as an efficient and scalable alternative metric, has only been applied at class level. To accurately identify fault-revealing test cases, we propose CP at finer-grained method-level and implement Method-level Change-proneness based Test-suite Minimization (MCTM). MCTM first calculates CP for each method from version control metadata, then determines the dependency between test cases and methods by analyzing the test-code call-graph. Next, it scores the association between test cases and their invoked methods using statistical measures such as Average, Geometric Mean etc. Finally, test cases with the highest scores are selected to form the reduced suite. Evaluation on 15 open-source Java projects with 635 buggy versions shows MCTM achieves 0.93 accuracy and 0.94 fault detection rate on average, significantly outperforming class-level CP and similarity-based approaches while maintaining superior efficiency.

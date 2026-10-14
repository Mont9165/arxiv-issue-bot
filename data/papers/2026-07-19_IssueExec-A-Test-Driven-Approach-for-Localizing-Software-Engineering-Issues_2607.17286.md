# IssueExec: A Test-Driven Approach for Localizing Software Engineering Issues

- arXiv ID: `2607.17286v1`
- Authors: Jiawei Liu, Yun Lin, Chenyan Liu, Yu Qian, Yiming Liu, Jiaxin Chang, Weinan Zhang, Linpeng Huang
- Published: 2026-07-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.17286v1) | [pdf](https://arxiv.org/pdf/2607.17286v1)

## Abstract

Issue localization, which identifies code locations requiring modification from issue descriptions, is a critical step in automated software maintenance. Existing approaches predominantly attempt to directly align issue descriptions with code elements, yet often struggle due to the inherent abstraction gap between the issue description and code implementation. Seeking alternative signals, our theoretical analysis suggests that test suites can serve as executable proxies for requirements, reducing localization uncertainty by 7.73 bits of entropy on average. A large-scale empirical study on 18 repositories validates this premise: existing tests cover 96.98\% of ground-truth files, and the two-hop pathway yields stronger semantic connectivity than direct matching in 82.4\% of cases. Despite their potential, leveraging tests for localization faces two key challenges: the semantic gap separating issue descriptions from test identifiers, and the substantial noise in execution traces from infrastructure code. To address these, we propose IssueExec, which bridges the semantic gap through domain-knowledge-enhanced test representations and filters noise via hierarchical trace analysis. Experiments on SWE-bench Lite show that IssueExec achieves state-of-the-art performance, improving function-level Recall@1 by 41.57\% over the strongest baseline. When integrated into the Agentless pipeline, IssueExec resolves 17.72\% more issues, demonstrating practical downstream benefits.

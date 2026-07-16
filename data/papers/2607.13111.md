# SemaDiff: Identifying Semantic-Changing Commits with Generated Code and Tests

- arXiv ID: `2607.13111v1`
- Authors: Maha Ayub, Michael Konstantinou, Ahmed Khanfir, Nikolaos Tsantalis, Mike Papadakis
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.13111v1) | [pdf](https://arxiv.org/pdf/2607.13111v1)

## Abstract

Distinguishing semantic-preserving commits from changing ones remains an open challenge in software repository mining. While existing approaches detect refactoring commits accurately, they cannot ensure that a commit is purely semantic-preserving, without any interleaving behaviour-changing modification. This limitation can impact several tasks, such as debugging, fault localisation, bug dataset construction, rollback analysis, and bug fixes backporting. To fill this gap, we propose SemaDiff, a novel approach for identifying semantic-preserving commits through behaviour-based analysis; comparison of similar test execution on pre- and post-commit versions. As code impacted by the refactoring is often hard to test and different accross both versions, we propose generating additional calling methods to that code, which serve as testing target. Given a commit, SemaDiff analyses the diff to identify modified code and extracts unchanged dependent code that calls it. It then generates an additional dependent class using a large language model to exercise the changed code in both versions, and automatically generates tests for the dependent code. This way, we obtain the same tests for the different code versions, enabling the behavioural-difference detection. The commit is classified as semantic-preserving only if all generated tests produce identical outcomes across the two versions. To evaluate SemaDiff, we construct and annotate manually a dataset of 183 commits, gathered from well-known open-source Java projects. The obtained results show that SemaDiff distinguishes accurately semantic-preserving from -- changing commits in about 76% of the cases, with a 100% precision in semantic-changing commit detection.

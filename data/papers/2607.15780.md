# READU: Inconsistency-Driven Just-in-Time Detection and Repair of README Bugs

- arXiv ID: `2607.15780v1`
- Authors: Doehyun Baek, Kilian Krampf, Michael Pradel
- Published: 2026-07-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.15780v1) | [pdf](https://arxiv.org/pdf/2607.15780v1)

## Abstract

Repository-level documentation, such as READMEs, is often the first point of contact between users and a repository. When this documentation is incorrect, users may encounter runtime errors or waste their time debugging. We call such mistakes in repository-level documentation README bugs. Addressing README bugs is challenging because documentation mixes prose with code, its connection to the source of truth is loose, and finding a bug still leaves developers to craft a repair. This paper presents READU, an inconsistency-driven technique for just-in-time detection and repair of README bugs. The key insight behind READU is that README bugs often manifest as inconsistencies between documentation and another source of truth: either repository-internal facts, such as source code, or repository-external facts, such as external dependencies. READU applies a high-recall commit filter, runs internal and external consistency checkers in parallel, uses an alert judge to remove false positives, and automatically synthesizes documentation patches. On 6,000 recent commits from six popular repositories including Linux and Spring Boot, READU detects 244 true positives with 75% precision, while consuming less than $0.01 and less than one minute per commit, on average. Of these true positives, READU correctly repairs 217. We report 66 found README bugs, of which (so far) 44 are confirmed and 26 are fixed.

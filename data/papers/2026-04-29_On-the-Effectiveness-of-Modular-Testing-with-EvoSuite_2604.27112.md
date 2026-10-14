# On the Effectiveness of Modular Testing with EvoSuite

- arXiv ID: `2604.27112v1`
- Authors: Elizabeth Dinella
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.27112v1) | [pdf](https://arxiv.org/pdf/2604.27112v1)

## Abstract

This paper explores the effectiveness of modular randomized testing for object oriented programs in Java. Modular testing involves testing individual components of a program in isolation. Often times, for effective test generation, a series of non-target setup calls must be included to obtain high coverage of the target component. In this work, we evaluate and improve modular testing with the EvoSuite test generator. We find that due to strict restrictions that disallow calls to non-target setup methods, EvoSuite's modular testing mode is ineffective and often results in low branch coverage. We propose \textsc{emote} (Effective Modular Testing with EvoSuite): an enhancement to EvoSuite that relaxes this restriction, allowing non-target methods to be included in the test prefixes. This modification draws inspiration from developer-written fuzz drivers, which often invoke setup methods to properly initialize the state before testing the target method. To ensure meaningful test generation, we modify EvoSuite's fitness function to focus branch coverage contributions on the call chain originating from the target method. \textsc{emote} is evaluated on a subset of the SF100 benchmark, showing a 15.15\% improvement in coverage of the target methods.

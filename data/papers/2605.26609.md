# Energy-Aware Decision Making in Software Stack Upgrades

- arXiv ID: `2605.26609v1`
- Authors: Mirko Stocker, Michael Wahler
- Published: 2026-05-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.26609v1) | [pdf](https://arxiv.org/pdf/2605.26609v1)

## Abstract

Software stack upgrades are a routine part of software maintenance and evolution, typically motivated by improved performance, stability, or functionality. Yet their impact on energy consumption - a growing concern for organizations pursuing sustainability - remains poorly understood. This paper presents a systematic method for measuring how different versions of core software stack components, such as Spring Boot and the Java Virtual Machine (JVM), influence the energy consumption of applications. Our approach evaluates combinations of framework versions, runtime versions, and execution platforms through automated benchmarking. Using a case study based on the Spring Petclinic REST application, we show that energy consumption varies substantially across Spring Boot and JVM versions, in some cases producing unexpected regressions. Notably, newer JVM releases and virtual threads (introduced in Java 21 and 23) yielded significant energy savings without requiring application changes. These results demonstrate that software upgrades can meaningfully affect energy usage and that measuring energy consumption provides valuable evidence for decision making in software maintenance and evolution.

# Intent-Based Mutation Testing: From Naturally Written Programming Intents to Mutants

- arXiv ID: `2607.05149v1`
- Authors: Asma Hamidi, Ahmed Khanfir, Mike Papadakis
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.05149v1) | [pdf](https://arxiv.org/pdf/2607.05149v1)

## Abstract

This paper presents intent-based mutation testing, a testing approach that generates mutations by changing the programming intents that are implemented in the programs under test. In contrast to traditional mutation testing, which changes (mutates) the way programs are written, intent mutation changes (mutates) the behavior of the programs by producing mutations that implement (slightly) different intents than those implemented in the original program. The mutations of the programming intents represent possible corner cases and misunderstandings of the program behavior, i.e., program specifications, and thus can capture different classes of faults than traditional (syntax-based) mutation. Moreover, since programming intents can be implemented in different ways, intent-based mutation testing can generate diverse and complex mutations that are close to the original programming intents (specifications) and thus direct testing towards the intent variants of the program behavior/specifications. We implement intent-based mutation testing using Large Language Models (LLMs) that mutate programming intents and transform them into mutants. We evaluate intent-based mutation on 29 programs and show that it generates mutations that are syntactically complex, semantically diverse, and quite different (semantically) from the traditional ones. We also show that 55% of the intent-based mutations are not subsumed by traditional mutations. Overall, our analysis shows that intent-based mutation testing can be a powerful complement to traditional (syntax-based) mutation testing.

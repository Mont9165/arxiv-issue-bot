# CrossLangFuzzer: Differential Testing of Cross-Language JVM Compilers

- arXiv ID: `2606.28132v1`
- Authors: Xiaotian Ma, Qiong Feng, Yongqiang Tian, Wei Song, Peng Liang
- Published: 2026-06-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.28132v1) | [pdf](https://arxiv.org/pdf/2606.28132v1)

## Abstract

Modern JVM software increasingly integrates multiple programming languages, such as Java, Kotlin, Groovy, and Scala, within a single application. Supporting such interoperability requires JVM compilers to perform cross-language compilation while reconciling subtle semantic differences across language boundaries. Errors in this process can lead to critical miscompilations, yet existing compiler testing techniques focus exclusively on isolated, singlelanguage compilation. To address this gap, we present CrossLangFuzzer, the first differential testing framework for cross-language JVM compilation. CrossLangFuzzer leverages the Kotlin compiler's unified intermediate representation (IR) to synthesize cross-language test programs. It further applies seven mutation operators to diversify generated test programs and improve bug-finding capability. Evaluated on the latest versions of five major JVM compilers, CrossLangFuzzer uncovered 32 confirmed bugs, including 15 in Kotlin, 4 in Groovy, 7 in Scala 3, 2 in Scala 2, and 4 in Java. CrossLangFuzzer is open-source at https://github.com/XYZboom/CrossLangFuzzer

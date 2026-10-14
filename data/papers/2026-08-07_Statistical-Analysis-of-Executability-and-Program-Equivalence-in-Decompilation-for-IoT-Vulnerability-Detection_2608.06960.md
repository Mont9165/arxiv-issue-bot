# Statistical Analysis of Executability and Program Equivalence in Decompilation for IoT Vulnerability Detection

- arXiv ID: `2608.06960v1`
- Authors: Minami Yoda, Jialong Li, Yasuyuki Tahara, Yuichi Sei, Yutaka Matsuno
- Published: 2026-08-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2608.06960v1) | [pdf](https://arxiv.org/pdf/2608.06960v1)

## Abstract

Internet of Things (IoT) devices handle sensitive privacy-related information such as user audio, video, and authentication data, making it essential to detect vulnerabilities in their firmware. Decompilation, a key detection technique, has recently attracted attention because Large Language Models (LLMs) enable high readability and high recompilation success rates. However, because LLM outputs depend on probabilistic token prediction, they tend to prioritize syntactic correctness and may generate plausible-looking code that is semantically different from the original binary. Vulnerabilities often arise in details that are easily lost in this process, such as error-handling flows and boundary checks. Existing evaluation metrics focus mainly on passing test cases and cannot sufficiently identify code whose internal structure has been altered despite appearing behaviorally valid, so a metric that quantifies the internal structure of decompiled code from multiple perspectives is needed. We propose a nine-dimensional quality evaluation metric consisting of three categories: structural, behavioral, and semantic similarity. Targeting 318 programs from OpenWrt, an open-source router platform underlying many commercial routers, we generated 19,625 decompilation results using five methods (one rule-based and four LLM-based) and analyzed them statistically. The recompilation-success group achieved significantly higher overall scores than the failure group (Cohen's d=0.92); behavioral similarity showed d=0.96 and structural similarity d=0.69, demonstrating that these metrics are important predictors of decompilation quality. This study provides a statistical evaluation foundation for quantifying implementation defects in IoT devices and a framework that generalizes to quality evaluation of black-box generative models.

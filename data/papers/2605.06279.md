# Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions

- arXiv ID: `2605.06279v1`
- Authors: Chengjie Wang, Jingzheng Wu, Xiang Ling, Tianyue Luo, Chen Zhao
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.06279v1) | [pdf](https://arxiv.org/pdf/2605.06279v1)

## Abstract

Large language models (LLMs) are now largely involved in software development workflows, and the code they generate routinely includes third-party library (TPL) imports annotated with specific version identifiers. These version choices can carry security and compatibility risks, yet they have not been systematically studied.
  We present the first large-scale measurement study of version-level risk in LLM-generated Python code, evaluating 10 LLMs on PinTrace, a curated benchmark of 1,000 Stack Overflow programming tasks. LLMs tend to specify version identifiers when directly prompted at 26.83%-95.18%, while down to 6.45%-59.19% in creating a manifest file directly. Among the specified versions, 36.70%-55.70% of tasks contain at least one known CVE, and 62.75%-74.51% of them carry Critical or High severity ratings. In 72.27%-91.37% of cases, the associated CVEs were publicly disclosed before the model's knowledge cutoff. The statistics show all models converge on the same small set of risky release versions, indicating a systemic bias rather than isolated model error. Static compatibility rates range from 19.70% to 63.20%, with installation failure as the dominant cause. The dynamic test cases confirm the pattern by 6.49%-48.62% pass rates. Further experiments confirm that these failures are attributable to version selection rather than code quality, and that externally anchored version constraints substantially reduce both vulnerability exposure and compatibility failures. Our findings reveal LLM version selection as a first-class, previously overlooked risk surface in LLM-based development. We disclosed these findings to the community of the evaluated models, and several confirmed the issue. All the code and dataset have been released for open science at https://github.com/dw763j/PinTrace.

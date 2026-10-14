# Cross-Ecosystem Bug Classification in Quantum Software

- arXiv ID: `2608.03173v1`
- Authors: Mir Mohammad Yousuf, Shabir Ahmad Sofi, Bisma Majid
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03173v1) | [pdf](https://arxiv.org/pdf/2608.03173v1)

## Abstract

Quantum software engineering faces unique challenges due to the interaction of classical and quantum components, which produce complex and often poorly understood bug patterns. Characterizing these bugs is essential for advancing testing, debugging, and quality assurance in quantum ecosystems. This paper presents a comparative study of 12,910 issues from Qiskit and 4,613 issues from 11 additional repositories, including Cirq and PyQuil. Using a rule-based classification framework, we analyze bugs by type, category, severity, quality attributes, and quantum-specific subtypes. Results show that classical bugs consistently dominate (67%) across ecosystems, while quantum-specific bugs account for 27-30%. Ecosystem-specific trends emerge: Qiskit repositories exhibit more compatibility related bugs, whereas other ecosystems show higher syntax and quantum-specific bug rates. Across both ecosystems, gate and circuit issues dominate quantum-specific bugs, though non-Qiskit projects reveal broader diversity, including algorithmic, resource, and hybrid-interface issues. Statistical validation confirms that the framework generalizes at the bug-type level while detecting significant variations at finer levels. Benchmarking against four supervised machine-learning baselines further shows that the rule-based framework consistently outperforms data-driven models, particularly for fine-grained quantum-specific subtypes, while longitudinal analysis (2017-2025) indicates that quantum- specific bugs remain relatively stable over time rather than exhibiting a steady increase. This study provides the first cross- ecosystem comparison of bug distributions in quantum software, demonstrating the utility of an interpretable, automation-ready, rule-based framework for guiding testing, debugging, and quality assurance.

# A Hybrid Approach for Automated Security Pattern Recovery

- arXiv ID: `2611.05823v1`
- Authors: Anh Minh Nguyen, Tuan Dat Tran, Alzubair Hassan, Liliana Pasquale
- Published: 2026-11-04
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.05823v1) | [pdf](https://arxiv.org/pdf/2611.05823v1)

## Abstract

Security-by-design emphasises integrating security into software design and development. Security pattern catalogues operationalise this principle by prescribing reusable architectural solutions to recurring security problems. However, recovering their implementations from source code remains challenging because security patterns are abstract, span multiple components, and admit many valid implementations. We present SecPatRec, a hybrid approach for automated security pattern recovery from source code repositories. We treat a security pattern as a reference architecture and frame its recovery as a deductive task: determining which prescribed roles are present, grounding them in code entities, and recovering their interaction sequences. SecPatRec pairs a ReAct-style LLM agent equipped with semantic and lexical code search for role detection and grounding with static code property graph analysis for interaction recovery. We curate a human-validated ground-truth dataset of 100 pattern instances covering five security patterns across 93 open-source Java and Python repositories, and introduce a three-level evaluation framework measuring recovery correctness against this ground truth. We evaluate SecPatRec using four LLMs, including proprietary and open-source models. Averaged over all models and pattern instances, SecPatRec achieves role-detection accuracy of 0.84, role-grounding similarity of 0.84, and an interaction-recovery score of 0.66. Compared to a one-shot end-to-end LLM baseline, SecPatRec achieves higher aggregate recovery scores and lower estimated LLM API costs per run, while processing repositories that exceed the baseline's configured input limit. The recovered role mappings and statically derived interaction sequences provide structural and behavioural evidence that can support inspection of security-pattern implementations.

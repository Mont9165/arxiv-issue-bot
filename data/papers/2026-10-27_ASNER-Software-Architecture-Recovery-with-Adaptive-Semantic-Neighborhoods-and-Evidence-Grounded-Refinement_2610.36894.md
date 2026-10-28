# ASNER: Software Architecture Recovery with Adaptive Semantic Neighborhoods and Evidence-Grounded Refinement

- arXiv ID: `2610.36894v1`
- Authors: Wenhao Wang, Zhi Jin, Jia Li, Dongming Jin, Heng Tian, Yingtao Fang, Wenguang Ye, Tiankuo Zhao
- Published: 2026-10-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.36894v1) | [pdf](https://arxiv.org/pdf/2610.36894v1)

## Abstract

Automated software architecture recovery provides architectural context for software engineering and repository-level LLM agents. Existing methods combine structural and semantic signals, but functional relatedness does not necessarily imply shared architectural responsibility. Fixed thresholds or Top-K neighborhoods also ignore repository scale and local similarity distributions, introducing errors that propagate through clustering. Unconstrained LLM refinement may further alter correct assignments without sufficient evidence. We propose ASNER (Adaptive Semantic Neighborhoods and Evidence-Grounded Refinement for Software Architecture Recovery), based on responsibility-aware, project-adaptive relation modeling and evidence-grounded boundary verification. ASNER derives structured file responsibilities with an LLM, constructs semantic neighborhoods that adapt to repository scale and local similarity distributions, and augments a static dependency graph with selected semantic relations and weak directory cues. Community detection recovers the component backbone. A Responsibility-Ownership-Aware (ROA) Agent then examines uncertain boundary files using project-level responsibilities and traceable code evidence, changing assignments only when supported. Experiments on 12 open-source projects spanning C, C++, Java, and Python show that ASNER achieves the best macro-average on all five metrics on the common benchmark, improving ARI and c2c@66 over GAER-GAT by 19.5% and 32.9%, respectively. A downstream evaluation shows that ASNER-guided LocAgent improves file-, module-, and function-level code localization, demonstrating the value of its architectural context for repository-level software engineering tasks.

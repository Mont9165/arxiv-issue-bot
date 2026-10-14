# Explanation-Guided Metamorphic Testing of Specialized Language Models: An Empirical Study

- arXiv ID: `2608.07076v1`
- Authors: Xingcheng Chen, Mehmet Besenk, Andrea Stocco
- Published: 2026-08-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.07076v1) | [pdf](https://arxiv.org/pdf/2608.07076v1)

## Abstract

\head{Background} Task-specialized language models are increasingly integrated into software engineering workflows to support vertical-domain activities such as issue triaging, document classification, and automated analysis. Despite their adoption, there is limited empirical evidence on how to test their robustness and detect brittle behaviors under semantics-preserving input transformations.
  \head{Aims} This paper investigates whether explainability-guided metamorphic testing can improve the effectiveness and validity of robustness testing for specialized language models compared to heuristic mutation strategies.
  \head{Method} We conduct a large-scale empirical study of explanation-guided metamorphic testing across three datasets, four model architectures, and 20 testing configurations derived from combinations of attribution methods and mutation strategies. The evaluated configurations combine attribution-based token prioritization, LLM-driven mutation, and automated semantic verification to generate linguistically valid test variants. We assess failure discovery capability, semantic validity, and testing efficiency against heuristic baselines.
  \head{Results} Explanation-guided metamorphic testing generates 2.30$\times$ more verified failure-inducing test cases than heuristic mutation strategies. Semantic verification substantially improves mutation validity and achieves high label-preservation precision among gate-accepted variants according to human annotation. The study further reveals systematic shortcut behaviors across models, including over-reliance on named entities and formatting cues.
  \head{Conclusions} The results provide evidence that explanation-guided metamorphic testing is an effective and practical approach for empirically evaluating the robustness of task-specialized language models used in vertical AI applications.

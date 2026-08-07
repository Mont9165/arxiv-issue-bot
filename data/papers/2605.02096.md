# Foundation Models as Oracles for Refactoring Correctness Detection

- arXiv ID: `2605.02096v1`
- Authors: Rohit Gheyi, Rian Melo, Jonhnanthan Oliveira, Marcio Ribeiro, Baldoino Fonseca
- Published: 2026-05-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.02096v1) | [pdf](https://arxiv.org/pdf/2605.02096v1)

## Abstract

Refactoring tools in popular Integrated Development Environments (IDEs) can introduce unintended behavioral changes or compilation errors, a persistent challenge that undermines developer trust in automated transformations. Traditional detection approaches rely on handcrafted preconditions, and static and dynamic analyses, yet remain limited in adaptability and can miss subtle correctness issues. This study examines the potential of foundation models to serve as oracles for detecting refactoring bugs in Java programs. We evaluate zero-shot prompting, without task-specific training, across 226 real refactoring bugs collected over more than a decade from widely used Java IDEs (IntelliJ-IDEA, Eclipse, and NetBeans), spanning 47 refactoring types. Our results indicate that foundation models can be effective for this task, although performance varies across models. In the first-run setting, GPT-OSS-20B achieved 80.5% accuracy, while GPT-5.4 reached 93.8%. We also evaluated other open and proprietary models: Gemma-4-31B achieved the strongest result among open models, and Gemini-3.1-Pro-Preview achieved the best overall result among all evaluated models. Metamorphic testing further shows that model predictions are largely consistent under intended semantics-preserving code variations, suggesting that superficial pattern matching may not fully account for the observed behavior. Beyond detection accuracy, foundation models can provide short explanations that may help support developer inspection, operate across refactoring types without explicitly encoded refactoring-specific rules, and may serve as lightweight triage aids in development workflows. Our findings suggest that foundation models can complement traditional refactoring checks by flagging suspicious transformations for developer inspection.

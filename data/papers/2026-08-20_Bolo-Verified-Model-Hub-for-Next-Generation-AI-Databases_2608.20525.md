# Bolo: Verified Model Hub for Next-Generation AI Databases

- arXiv ID: `2608.20525v1`
- Authors: Yunqi Li, Ila Petrovic, Yongjoo Park
- Published: 2026-08-20
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.20525v1) | [pdf](https://arxiv.org/pdf/2608.20525v1)

## Abstract

Verified, ready-to-use inference pipelines are a cornerstone of future AI databases. They allow multi-modal databases to incorporate specialized language, vision, and tabular models that can deliver both high accuracy and efficiency. Unfortunately, existing model platforms such as Hugging Face fall short of this goal. While they host millions of model repositories, many contain only raw weights without runnable pipelines. Even well-documented models often fail due to missing dependencies, unsupported model classes, or incorrect task assignments. Moreover, different models fail for different reasons, with no uniform solution. Constructing a large-scale, verified model hub is nearly impossible with human effort alone.
  We argue that AI agents can achieve this at scale. We present \system, a model platform that hosts verified, ready-to-use inference pipelines, powered by a multi-stage agentic system for model remediation. For models that fail under standard usage, the agent inspects errors and repairs broken pipelines (Type~I). For models outside the scope of existing interfaces, it synthesizes pipelines from scratch using model metadata and documentation (Type~II \& III). To prevent incorrect pipelines from entering the database, the agent applies multi-stage verification---checking not only program structure but also semantic model behavior, ensuring pipelines produce meaningful outputs rather than merely executing without error. In preliminary experiments, \system achieves 97.27\% and 86.08\% runnable coverage for Type~II and Type~III models, respectively, demonstrating that agentic synthesis with targeted verification can transform large collections of unusable model weights into a verified database of ready-to-use inference pipelines. The preliminary database is open-sourced at \textcolor{blue}{https://bolobao.ai/}.

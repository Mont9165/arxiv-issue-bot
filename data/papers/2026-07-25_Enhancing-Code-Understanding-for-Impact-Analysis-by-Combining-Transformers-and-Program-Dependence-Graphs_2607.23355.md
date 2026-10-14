# Enhancing Code Understanding for Impact Analysis by Combining Transformers and Program Dependence Graphs

- arXiv ID: `2607.23355v1`
- Authors: Yanfu Yan, Nathan Cooper, Kevin Moran, Gabriele Bavota, Denys Poshyvanyk, Steve Rich
- Published: 2026-07-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.23355v1) | [pdf](https://arxiv.org/pdf/2607.23355v1)

## Abstract

Impact analysis (IA) is a critical software maintenance task that identifies the effects of a given set of code changes on a larger software project with the intention of avoiding potential adverse effects. IA is a cognitively challenging task that involves reasoning about the abstract relationships between various code constructs. Given its difficulty, researchers have worked to automate IA with approaches that primarily use coupling metrics as a measure of the "connectedness" of different parts of a software project. Many of these coupling metrics rely on static, dynamic, or evolutionary information and are based on heuristics that tend to be brittle, require expensive execution analysis, or large histories of co-changes to accurately estimate impact sets.
  In this paper, we introduce a novel IA approach, called Athena, that combines a software system's dependence graph information with a conceptual coupling approach that uses advances in deep representation learning for code without the need for change histories and execution information. Previous IA benchmarks are small, containing fewer than ten software projects, and suffer from tangled commits, making it difficult to measure accurate results. Therefore, we constructed a large-scale IA benchmark, called Alexandria, from 25 open-source software projects, that utilizes fine-grained commit information from bug fixes. On this new benchmark, our best-performing approach configuration achieves mRR, mAP, and HIT@10 scores of 60.32%, 35.19%, and 81.48%, respectively. Through various ablations and qualitative analyses, we show that Athena's novel combination of program dependence graphs and conceptual coupling information leads it to outperform a simpler baseline by 10.34%, 9.55%, and 11.68% with statistical significance.

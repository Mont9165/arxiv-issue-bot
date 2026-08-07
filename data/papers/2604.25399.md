# CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction

- arXiv ID: `2604.25399v1`
- Authors: Jun Gao, Yun Peng, Qian Qiao, Changhai Zhou, Yuhua Zhou, Shiyang Zhang, Shichao Weng, Zhenchang Xing, Xiaoxue Ren
- Published: 2026-04-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.25399v1) | [pdf](https://arxiv.org/pdf/2604.25399v1)

## Abstract

Despite strong performance on code generation tasks, it remains unclear whether large language models (LLMs) genuinely reason about code execution. Existing code reasoning benchmarks primarily evaluate final output correctness under a single canonical implementation, leaving two critical aspects underexplored: (1) whether LLMs can maintain consistency to functionally equivalent implementations, and (2) whether LLMs can accurately reason about intermediate execution states. We introduce \textbf{CoRE}, a \textbf{Co}de \textbf{Re}asoning benchmark that evaluates code reasoning through \textbf{implementation invariance} and \textbf{process transparency}. Extensive evaluations on eight frontier LLMs reveal two fundamental limitations. First, models exhibit a substantial \textbf{robustness gap}, with performance varying significantly across equivalent implementations. Second, we observe \textbf{superficial execution}, where models arrive at correct final outputs without correctly reasoning about intermediate execution states. Together, these findings demonstrate that output-only evaluations are insufficient for assessing code reasoning and position CoRE as a necessary benchmark for evaluating robust and faithful code reasoning.\footnote{Data and code are available at https://github.com/ZJUSig/CoRE.}

# SAFEdit: Does Multi-Agent Decomposition Resolve the Reliability Challenges of Instructed Code Editing?

- arXiv ID: `2604.25737v1`
- Authors: Noam Tarshish, Nofar Selouk, Daniel Hodisan, Bar Ezra Gafniel, Yuval Elovici, Asaf Shabtai, Eliya Nachmani
- Published: 2026-04-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.25737v1) | [pdf](https://arxiv.org/pdf/2604.25737v1)

## Abstract

Instructed code editing is a significant challenge for large language models (LLMs). On the EditBench benchmark, 39 of 40 evaluated models obtain a task success rate (TSR) below 60 percent, highlighting a gap between general code generation and the ability to perform instruction-driven editing under executable test constraints. To address this, we propose SAFEdit, a multi-agent framework for instructed code editing that decomposes the editing process into specialized roles to improve reliability and reduce unintended code changes. A Planner Agent produces an explicit, visibility-aware edit plan, an Editor Agent applies minimal, literal code modifications, and a Verifier Agent executes real test runs. When tests fail, SAFEdit uses a Failure Abstraction Layer (FAL) to transform raw test logs into structured diagnostic feedback, which is fed back to the Editor to support iterative refinement. We compare SAFEdit against both prior single-model results reported for EditBench and an implemented ReAct single-agent baseline under the same evaluation conditions. We used EditBench to evaluate SAFEdit on 445 code editing instances in five languages (English, Polish, Spanish, Chinese, and Russian) under varying spatial context variants. SAFEdit achieved 68.6 percent TSR, outperforming the single-model baseline by 3.8 percentage points and the ReAct single-agent baseline by 8.6 percentage points. The iterative refinement loop was found to contribute 17.4 percentage points to SAFEdit's overall success rate. SAFEdit's automated error analysis further indicates a reduction in instruction-level hallucinations compared to single-agent approaches, providing an additional framework component for interpreting failures beyond pass or fail outcomes.

# BT-APE: A Computationally Light Backtracking Approach to Automatic Prompt Engineering for Requirements Classification

- arXiv ID: `2607.00427v1`
- Authors: Mohammad Amin Zadenoori, Waad Alhoshan, Jacek Dąbrowski, Liping Zhao, Alessio Ferrari
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.00427v1) | [pdf](https://arxiv.org/pdf/2607.00427v1)

## Abstract

Large language models (LLMs) are increasingly applied to requirements engineering (RE) tasks, yet the prompts guiding them are typically designed manually through trial and error, yielding inconsistent and suboptimal results. Automated prompt construction remains largely unexplored in RE, leaving its effectiveness unclear. To address this, we propose a lightweight Automatic Prompt Engineering approach, Backtracking APE (BT-APE), and apply it to requirements classification. We frame prompt design as an optimization problem, iteratively refining prompts via LLM-generated candidates, backtracking search, and dynamic example selection. Evaluating BT-APE on three benchmark datasets with five instruction-tuned LLMs, we compare it against four classical prompting baselines (zero-shot, few-shot, chain-of-thought, CoT+few-shot) and a state-of-the-art but resource-intensive APE baseline (PE2). BT-APE and PE2 achieve nearly identical accuracy, both substantially outperforming the classical baselines with large effect sizes; however, BT-APE imposes a far lighter computational footprint, consuming roughly 72% fewer input tokens and 66% less wall-clock time at equivalent accuracy, making it better suited to resource-constrained deployment. Our contributions are threefold: (i) a lightweight APE framework with an open interactive tool and replication package; (ii) the first systematic comparison of APE against classical prompting for requirements classification; and (iii) insights into how class definitions and prompt evolution affect performance.

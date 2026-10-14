# Agentic Cost-Aware Query Planning with Knowledge Distillation for Big Data Analytics

- arXiv ID: `2605.17831v1`
- Authors: Mahdi Naser-Moghadasi
- Published: 2026-05-18
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.17831v1) | [pdf](https://arxiv.org/pdf/2605.17831v1)

## Abstract

Query optimization in big data analytics remains computationally expensive, particularly for resource-constrained environments where traditional optimizers fail to satisfy memory and latency constraints. We present an agentic query planning system that combines a rule-based teacher planner, UCB1 bandit exploration, cost-aware prediction, and knowledge distillation to a lightweight student planner. Our teacher planner generates SQL plans using six key optimization strategies, while UCB1 bandit search efficiently explores the plan space under explicit resource constraints. A Random Forest cost model predicts query latency from plan features, enabling cost-aware decisions. A distilled student planner (Logistic Regression or Gradient Boosting) learns to mimic teacher-bandit decisions for fast inference. Evaluation on NYC Taxi and IMDB datasets demonstrates 23% latency reduction compared to default planners while maintaining 94% constraint satisfaction. The student planner achieves 89% accuracy in replicating optimal plans with 15x faster inference time. Our single-file implementation enables reproducible big-data analytics on resource-limited machines and is publicly available at https://github.com/mahdinaser/agentic-kd-planner.

# Beyond Accuracy: Measuring Logical Compliance of Predictive Models

- arXiv ID: `2606.20208v1`
- Authors: Guillaume Olivier Delplanque, Pierre Genevès, Nabil Layaïda, Zephirin Faure
- Published: 2026-06-18
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `cs.NE`
- Links: [abs](http://arxiv.org/abs/2606.20208v1) | [pdf](https://arxiv.org/pdf/2606.20208v1)

## Abstract

Machine learning models are predominantly evaluated through predictive performance metrics such as ranking quality, prediction error, or classification accuracy. While these metrics effectively quantify how closely predictions match the ground truth, they do not assess whether model outputs respect predefined logical or domain-specific constraints. In high-stakes applications, including healthcare, finance, and autonomous systems, logical consistency can be as critical as predictive accuracy, yet no standard metric captures this dimension. We introduce the Rule Violation Score (RVS), a complementary evaluation metric that quantifies the extent to which a predictive model respects a given set of logical rules, independently of predictive accuracy. RVS treats hard rules (strict constraints) and soft rules (statistical regularities) differently, can be evaluated on any dataset and on any predictive model expressed over a relational vocabulary, and can be computed using SQL queries that are automatically generated for Horn rules. Beyond evaluating models, RVS can also evaluate the logical consistency of training datasets and help identify poorly defined rules. We evaluate RVS on three benchmarks covering knowledge graph link prediction and relational regression, including rule-based, embedding-based, and neuro-symbolic predictive models. Our results demonstrate that two models achieving comparable predictive accuracy can exhibit substantially different levels of logical compliance, revealing differences in model behavior that standard metrics fail to capture.

# STEER: Reducing Inference Cost in Relational Foundation Models through Semantically Informed Sampling

- arXiv ID: `2610.00907v1`
- Authors: Abdalla Mohamed, Ashraf Aboulnaga
- Published: 2026-10-01
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.00907v1) | [pdf](https://arxiv.org/pdf/2610.00907v1)

## Abstract

Relational foundation models (RFMs) are pretrained once on a collection of relational databases and prediction tasks, and then applied zero-shot to previously unseen databases and tasks. To make a prediction for a target row, an RFM samples a neighborhood of rows linked to that row through foreign keys and uses this neighborhood as its inference context. Lowering inference cost is an important goal for any foundation model, and for RFMs this cost grows with the size of the context. The simplest ways to shrink the context is to drop some of the sampled rows, but this ignores the semantics of the database schema, so it is as likely to discard informative rows as uninformative ones. We propose STEER, a sampling approach that shrinks the inference context by concentrating it on the tables most relevant to the prediction task at hand. STEER obtains relevance information by prompting a large language model to rank the foreign-key edges of the database schema into relevance tiers for the given task, and then maps each tier to a probability of following that edge during traversal. Because the ranking uses only the schema, it is computed once per task and reused across all subsequent predictions, amortizing its cost. We evaluate STEER on three state-of-the-art RFMs (RT, RT-J, and Griffin) and show that it reduces inference context size by about 40% on average while maintaining, and in some cases improving, prediction accuracy.

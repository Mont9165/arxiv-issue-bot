# Single-Database Rewards Are Hackable: Counterfactual Execution for Trustworthy Text-to-SQL RL

- arXiv ID: `2611.34363v1`
- Authors: Shreshth Rai, Rishii Kumar Singh, Aksh Aggarwal
- Published: 2026-11-25
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.34363v1) | [pdf](https://arxiv.org/pdf/2611.34363v1)

## Abstract

Reinforcement learning (RL) for text-to-SQL agents pays a query when its result matches the reference on one database. However, a wrong query can match by luck when the data lack the rows that expose its bug. We study a counterfactual-database (CF) reward that also runs the final query on a few hidden, code-generated copies of the database and pays only if all results match (strict form) or by the share matched (mean form). On 1,302 synthetic audit questions, the strict form lowers the share of buggy queries paid in full from 29.5% to 16.8% and of reward hacks from 54.1% to 1.9%, rejecting 0 of 2,847 correct queries; copies from a family-blind generator do about as well. In a controlled GRPO comparison on a 3.35B model with three seeds per arm, training on the mean form did not improve in-domain accuracy (8.4% vs 11.7%), because the two rewards disagreed on only 5-7% of rollouts; on Spider it gained 1.6 points. One seed reverses both signs, so single-seed reward comparisons mislead. Code: https://github.com/RishiiGamer2201/counterfactual-sql-rewards ; data, models, demo: https://huggingface.co/counterfactual-sql

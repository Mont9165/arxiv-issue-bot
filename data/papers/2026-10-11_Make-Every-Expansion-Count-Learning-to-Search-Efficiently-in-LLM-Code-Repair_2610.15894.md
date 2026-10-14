# Make Every Expansion Count: Learning to Search Efficiently in LLM Code Repair

- arXiv ID: `2610.15894v1`
- Authors: Elad Sharony, Ido Greenberg, Jialin Song, Shie Mannor, Gal Chechik, Eli Meirom
- Published: 2026-10-11
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.15894v1) | [pdf](https://arxiv.org/pdf/2610.15894v1)

## Abstract

Large language model (LLM) code-repair systems fix faulty programs by repeatedly generating and testing revisions. Each revision is costly, making the choice of which repair to pursue important for efficiency. Existing search policies rely on test pass rates and search statistics, ignoring the details of test failures and proposed edits. We introduce CodeTriage, a learned policy that prioritizes edits before their revised programs are generated and tested. Its 0.6B-parameter model reads the test output, failure diagnosis, and proposed edit, then predicts a distribution over the number of repair steps needed to reach a fix through that edit. These predictions prioritize all pending edits across programs before generating and testing the revised code. On held-out repair tasks, CodeTriage finds fixes with 21% fewer program revisions and 12% fewer output tokens than the strongest baseline on each metric. Without retraining, it achieves the highest average success across search budgets for each of 11 unseen repair LLMs. Ablations show that both the failure context and edit text, as well as comparisons across programs, improve search. We also release a corpus of 12.2 million program versions from four LLMs, organized into repair trees with proposed edits and test results.

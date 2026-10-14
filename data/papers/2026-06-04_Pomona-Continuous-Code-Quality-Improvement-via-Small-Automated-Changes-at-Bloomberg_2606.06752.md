# Pomona: Continuous Code Quality Improvement via Small, Automated Changes at Bloomberg

- arXiv ID: `2606.06752v1`
- Authors: David Williams, Angelos Evripiotis, Serkan Kirbas, Harry Morgan, Sergey Magidovich, Peter Wainwright, Federica Sarro
- Published: 2026-06-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.06752v1) | [pdf](https://arxiv.org/pdf/2606.06752v1)

## Abstract

In this short experience paper, we present Pomona, a lightweight agentic tool that utilises agent skills for continuous automated code quality improvement. Inspired by the philosophy of Kaizen(TM), Pomona automates a cycle of discovery and incremental repair: a Scanning skill identifies improvement tasks (e.g., linting violations, technical debt markers, and test gaps) and prioritises them in a structured backlog, while a Repair skill generates tiny pull requests (PRs) targeting ~10 lines of diff. This human-in-the-loop design enables frequent, low-risk improvements while maintaining engineer trust and productivity and reducing technical debt. We evaluated Pomona through a one-month deployment in a team and a questionnaire distributed to 10 senior engineers. Our preliminary results are promising: 15 of 17 generated PRs were successfully merged with a median time-to-close of under 2 hours. Furthermore, 8/10 of surveyed engineers expressed a desire to adopt Pomona, praising small diff sizes and Pomona's focus on improving code quality. We conclude by discussing actionable insights for researchers and practitioners on strategies for effective agentic deployment in industry.

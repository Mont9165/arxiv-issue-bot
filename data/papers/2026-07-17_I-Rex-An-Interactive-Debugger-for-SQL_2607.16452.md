# I-Rex: An Interactive Debugger for SQL

- arXiv ID: `2607.16452v1`
- Authors: Yihao Hu, Zian Chen, Zhiming Leong, Sharan Sokhi, Zachary Zheng, Alex Chao, Kristin Stephens-Martinez, Sudeepa Roy, Jun Yang
- Published: 2026-07-17
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.16452v1) | [pdf](https://arxiv.org/pdf/2607.16452v1)

## Abstract

SQL is declarative in nature and rich in its features. Writing semantically correct SQL queries and finding logical bugs in SQL are not easy, even for experienced programmers, who are often used to the mindset of working with general-purpose programming languages (GPLs). While there are many GPL debuggers, SQL debugging has received much less attention. In this paper, we present I-Rex, a SQL debugger that enables users to inspect the logical execution of SQL queries visually and interactively to identify and potentially fix logical bugs in the queries. I-Rex draws analogies to the debugging paradigm of GPLs (e.g., stepping, watchpoints, etc.), making it easier for programmers to adopt. However, unlike debugging GPLs, which involves executing the underlying program in full to the point of interest, I-Rex allows users to jump to arbitrary points of interest by leveraging the power of the database systems, through selective materialization and query rewrites. To simplify deployment, I-Rex acts as a lightweight middleware on top of the database system; it imposes no overhead to prepare a database for debugging and maintains no state in the database systems during debugging sessions. We demonstrate the effectiveness of I-Rex through performance experiments as well as a user study in an educational setting.

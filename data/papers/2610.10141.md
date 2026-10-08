# AdaT$^2$: Adaptive Test Transformations for Black-Box Boundary Testing of Conversational Agents

- arXiv ID: `2610.10141v1`
- Authors: Liting Lin, Boxi Yu, Qinghua Xu, Yuzhong Zhang, Lionel Briand, Emir Muñoz
- Published: 2026-10-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.10141v1) | [pdf](https://arxiv.org/pdf/2610.10141v1)

## Abstract

Conversational agents based on large language models (LLMs) must comply with policies. Each condition in a policy draws a boundary between user requests, and the agent must behave differently on its two sides. We present AdaT$^2$, which extracts statements from the agent's replies in exploratory conversations with an LLM acting as the user, and uses the statements to guide boundary test generation. Each statement describes one condition and the behavior expected when the condition holds. Besides plain tests guided by single statements, AdaT$^2$ writes transformed tests guided by pairs of a statement and a test transformation instruction, such as "omit one required input". The instruction of a pair can move a test to the other side of the statement's boundary or to another boundary. The statements and instructions form far more pairs than a run can try, and many pairs are not applicable. Adaptive pair selection therefore chooses the statement of each pair by novelty and the instruction with the bandit algorithm Bayes-UCB, which learns from whether earlier pairs yielded a test and whether the agent passed it according to an LLM judge. Our benchmark counts the two sides of each boundary separately and distinguishes boundaries explicitly defined by the agent's prompt, tool code, or knowledge base from boundaries that the agent's LLM infers from domain knowledge. On four domains of $τ^3$-bench, 62.7% to 83.3% of AdaT$^2$'s tests are valid boundary tests whose expected behavior is explicitly defined, higher in every domain than AgentEval's (47.7% to 68.1%). Transformed tests add 13 to 46 explicitly defined boundaries that plain tests miss. As regression tests, AdaT$^2$'s test suites detect all eight seeded policy faults in the airline domain and four of eight in the retail domain, and AgentEval's test suites, with fewer than a third as many tests, detect five and two, respectively.

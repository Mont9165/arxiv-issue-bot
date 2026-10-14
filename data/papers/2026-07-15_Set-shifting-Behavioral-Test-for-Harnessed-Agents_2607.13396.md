# Set-shifting Behavioral Test for Harnessed Agents

- arXiv ID: `2607.13396v1`
- Authors: Ziwei Ye
- Published: 2026-07-15
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.13396v1) | [pdf](https://arxiv.org/pdf/2607.13396v1)

## Abstract

What happens to an LLM agent's tool choice when the reliable tool silently changes within an ongoing session? We borrow set-shifting from cognitive psychology to study how well agents adapt to hidden reliability shifts. Our benchmark mounts tool-skill libraries with redundancies, where many tools solve the same task but differ in hidden reliability. In our evaluation framework, a branched schedule shifts the reliable tool group at hidden boundaries and pairs every shift with a no-shift control. We find that agents, by default, settle on a small recurring routine within a few turns of each boundary, with call shares concentrating on a few discrete values after each reliability shift. We score the set-shifting accuracy for each agent trajectory: the joint probability of routing to the target tool group in every post-shift window. We test open-weight LLMs in an open-source agentic harness and find qualitatively distinct failure modes across the same set of routines. We also find that set framing, how the toolset presents the alternatives as competing or complementary, shifts the routing dynamics.

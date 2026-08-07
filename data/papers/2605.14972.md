# Viverra: Text-to-Code with Guarantees

- arXiv ID: `2605.14972v1`
- Authors: Haoze Wu, Rocky Klopfenstein, Keith Farkas, Nina Narodytska
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.HC`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2605.14972v1) | [pdf](https://arxiv.org/pdf/2605.14972v1)

## Abstract

A fundamental limitation of Text-to-Code is that no guarantee can be obtained about the correctness of the generated code. Therefore, to ensure its correctness, the generated code still has to be reviewed, tested, and maintained by developers. However, parsing through LLM-generated code can be tedious and time-consuming, potentially negating the productivity gains promised by AI-coding tools. To address this challenge, we present Viverra, a system that automatically produces formally verified annotations alongside generated code to aid user's understanding of the generated program. Given a natural-language task description, Viverra prompts an LLM to synthesize a C program together with candidate assertions expressing safety and correctness properties. It then verifies those assertions in a compositional and best-effort manner via a portfolio of bounded model checkers. Evaluation on 18 diverse programming tasks suggests that Viverra can efficiently generate code with verified assertions, and that these assertions improve users' performance on code-comprehension tasks in a user study with more than 400 participants.

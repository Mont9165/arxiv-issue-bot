# Simulating Students' Java Programming Errors with Large Language Models

- arXiv ID: `2606.14113v1`
- Authors: Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi
- Published: 2026-06-12
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2606.14113v1) | [pdf](https://arxiv.org/pdf/2606.14113v1)

## Abstract

Understanding student errors in the programming is a cornerstone of programming education, yet obtaining a representative set of student errors for any newly designed task remains slow and costly, since authentic submissions only accumulate after extensive classroom deployment. This paper explores whether large language models (LLMs) can serve as scalable proxies for students by simulating realistic logical errors in code submissions. Using the CodeWorkout dataset of 74,000+ unique student Java submissions across 37 problems, we evaluate five LLMs under three mainstream prompting strategies: Input-Output (IO), Chain-of-Thought (CoT), and iterative Self-Refine. We assess performance along two key dimensions: diversity (the range of distinct error patterns) and alignment (alignment with authentic student mistakes), and examine how these vary by struggling level of programming tasks. Our quantitative findings reveal that while all models generate diverse errors, their alignment to human submissions diverges: Claude Sonnet 4 achieves the most balanced performance. In addition, we conducted a blinded expert annotation study (N = 401) comparing synthetic and authentic errors. This qualitative analysis confirms that the generated errors are functionally indistinguishable from authentic student errors. Moreover, higher-struggling-level problems elicit more diverse but less student-like errors. These results highlight trade-offs in using LLMs to simulate human learners and suggest design considerations for integrating synthetic errors into teachable agents, intelligent tutoring systems, and large-scale learning analytics.

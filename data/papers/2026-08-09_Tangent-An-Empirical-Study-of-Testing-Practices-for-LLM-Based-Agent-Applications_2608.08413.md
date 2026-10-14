# Tangent: An Empirical Study of Testing Practices for LLM-Based Agent Applications

- arXiv ID: `2608.08413v1`
- Authors: Rangeet Pan, Tyler Stennett, Divya Sankar, Bridget McGinn, Alessandro Orso, Raju Pavuluri, Saurabh Sinha, Maja Vukovic
- Published: 2026-08-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.08413v1) | [pdf](https://arxiv.org/pdf/2608.08413v1)

## Abstract

Agents built on large language models (LLMs) are increasingly used to build applications that perform complex, multi-step tasks involving reasoning, tool use, and interaction with external environments. Despite rapid progress in benchmarking LLM-based agents, very few studies have attempted to understand how such systems are tested in practice. In particular, testing levels, objectives, data patterns, test complexity, and validation strategies for agent applications remain underexplored. In this paper, we present an empirical study of testing practices in LLM-based agent applications using a large corpus of mined open-source projects. We construct a large-scale dataset of agent applications, tools, and tests, and manually label 2,572 test methods from 240 modules. From this analysis, we derive a taxonomy of 23 testing patterns across test fixtures, data, objectives, and assertions, and characterize tests by level (unit, module, integration). We complement this with structured interviews of 10 senior industry practitioners building agentic systems. Our results show that testing of LLM-based agent applications is dominated by narrowly scoped unit tests, with limited coverage of complex interactions, realistic scenarios, and non-functional requirements. Tests frequently rely on simplistic inputs, heavy mocking, and shallow validation, and agent-related tests exhibit low structural complexity. While industry practice places greater emphasis on non-functional testing than open-source projects, both reveal common gaps, including the lack of formal testing foundations, unclear test objectives, and challenges in generating high-quality test data. Based on these findings, we outline research directions toward more systematic and rigorous testing of agent applications, including foundations for agent testability, formalized test objectives, and fault-based testing techniques.

# SmartHomeSecure: Automated Detection and Repair of Smart Home Configuration Errors Using Large Language Models

- arXiv ID: `2607.06748v1`
- Authors: Yizhi Wang, Xinghua Gao, Reachsak Ly, Alireza Shojaei
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.06748v1) | [pdf](https://arxiv.org/pdf/2607.06748v1)

## Abstract

Smart home automation platforms increasingly rely on user-authored YAML configuration files to define device behaviors, but these files are prone to syntax, formatting, and semantic logic errors that can cause automation failures and safety risks. Existing YAML validators, static analysis tools, and general-purpose large language models offer limited support for end-to-end diagnosis and repair because they lack domain-specific understanding and validated correction workflows. This paper presents SmartHomeSecure, a prototype for automated detection and repair of Home Assistant configuration errors using lightweight program analysis and constraint-guided large language model generation. SmartHomeSecure parses YAML files, detects syntactic and common semantic errors, normalizes error context, applies deterministic auto-fixes for routine defects, and constructs constrained prompts that guide LLMs toward minimal and structurally valid repairs. The system is implemented as a modular web application with four layers: UI Shell, Feature Orchestrator, Domain Engine, and Integration Layer. Its repair pipeline was evaluated on 100 real-world Home Assistant YAML files with manually injected errors across five categories: syntax/parsing, indentation, mapping, sequence, and scalar quoting errors. Four models were tested: gpt-oss-20b, gpt-oss-120b, llama-3.1-8b, and llama-3.3-70b. Results show that three models achieved 100% error detection accuracy, with repair success rates ranging from 87% to 93%. Manual verification found no hallucinated or incorrect repairs among successful outputs. These findings suggest that combining domain-aware program analysis with constrained generative AI is a feasible approach for improving the reliability and usability of smart home configuration repair.

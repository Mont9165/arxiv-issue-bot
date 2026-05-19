# LLM-Based Static Verification of Code Against Natural-Language Requirements: An Industrial Experience Report

- arXiv ID: `2605.17926v1`
- Authors: Zhi Quan Zhou, Dave Towey, Tsong Yueh Chen
- Published: 2026-05-18
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.17926v1) | [pdf](https://arxiv.org/pdf/2605.17926v1)

## Abstract

Large language models (LLMs) are increasingly used to generate requirements specifications, design documents, code, and test cases. In contrast, much less attention has been given to a more difficult assurance problem: statically verifying whether implemented code satisfies requirements written in natural language. Conventional static analysis tools are effective at detecting coding defects and known vulnerability patterns, but they cannot determine whether program behavior matches intended business logic. Detecting such defects requires reasoning over the specification rather than the code alone. Software testing can expose some of these mismatches, but its effectiveness depends heavily on test design, executable artifacts, and runtime environments. This article presents a two-stage LLM-based workflow for addressing this challenge in an intelligent-vehicle cybersecurity case study. In the first stage, an AI-based rule miner extracts verifiable rules from natural-language requirements while explicitly identifying ambiguity, self-contradiction, and other non-verifiable statements. In the second stage, an AI-based code auditor checks implementation evidence against the extracted rules. Instead of asking a single LLM to directly verify code against lengthy natural-language specifications, the workflow introduces a structured intermediate representation to reduce hallucination, output variability, limited explainability, and context loss. The resulting approach is a requirement-aware and semantics-aware form of static analysis that complements software testing. By analyzing requirements and source code without requiring compilation, execution, or runtime environments, the method shifts verification and validation activities left in the development lifecycle. This LLM-based static analysis is also a new approach to addressing the test oracle problem.

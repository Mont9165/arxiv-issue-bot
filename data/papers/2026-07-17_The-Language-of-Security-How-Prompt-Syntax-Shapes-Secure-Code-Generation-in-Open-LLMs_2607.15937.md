# The Language of Security: How Prompt Syntax Shapes Secure Code Generation in Open LLMs

- arXiv ID: `2607.15937v1`
- Authors: Matteo Cicalese, Antonio Della Porta, Stefano Lambiase, Emanuele Iannone, Torge Hinrichs, Riccardo Scandariato, Fabio Palomba
- Published: 2026-07-17
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.15937v1) | [pdf](https://arxiv.org/pdf/2607.15937v1)

## Abstract

Large Language Models (LLMs) are increasingly used for source code generation despite their outputs often exhibiting security vulnerabilities. Prior work shows that prompt engineering can mitigate such risks, yet (1) they focused on high-level prompting strategies, neglecting recent evidence that fine-grained syntactic variations can substantially alter model behavior; and (2) predominantly evaluate proprietary LLMs, limiting the applicability of their findings in industrial settings where self-hosted, open models are preferred for privacy, compliance, and deployment control. In this paper, we study how fine-grained syntactic constituents of prompts influence the security of open LLM-generated code. Using a parser-driven approach, we systematically generate syntactic variants of security-relevant code generation prompts and evaluate their impact on code security across multiple open LLMs and programming languages. Our results show that specific syntactic elements, such as constraints, guards, conditions, and concept bindings, and their position within the prompt consistently affect the likelihood of generating insecure code. These findings identify prompt syntax as a concrete security control surface and provide actionable guidance for reducing vulnerability risk in LLM-assisted development.

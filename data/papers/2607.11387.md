# From GUI Tests to Conversational Interaction: A New Perspective on App-Specific Voice Assistants

- arXiv ID: `2607.11387v1`
- Authors: Xue Qin, Sumesh Surendran Letha
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.11387v1) | [pdf](https://arxiv.org/pdf/2607.11387v1)

## Abstract

Voice assistants are widely deployed on mobile platforms, yet most are designed as system-level services that remain poorly aligned with application-specific behavior. As a result, enabling voice interaction at the app level requires developers to manually reimplement application logic, leading to high development and maintenance costs.
  We propose an LLM-driven approach to automating the development of app-specific voice assistants by repurposing GUI test code, which encodes behavior-preserving, executable specifications of application functionality. In this paper, we present a perspective in which large language models reinterpret GUI tests as bridges between application behavior and conversational interaction. By transforming test methods into app-specific VA artifacts, such as voice intents, capability descriptions, and executable action plans, our approach grounds voice assistants directly in existing application logic rather than external specifications.
  We illustrate this vision through AppVA, a research prototype on Android. Our preliminary results across five open-source applications suggest that GUI test code can be reused beyond testing, enabling the synthesis of app-specific voice assistants and highlighting a broader research direction at the intersection of software testing, interaction design, and LLM-enabled automation.

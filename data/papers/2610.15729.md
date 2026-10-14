# LLM-based Code Auditing by Inferring and Evaluating Developer Assumptions

- arXiv ID: `2610.15729v1`
- Authors: Junming Liu, Marcel Böhme
- Published: 2026-10-11
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.15729v1) | [pdf](https://arxiv.org/pdf/2610.15729v1)

## Abstract

When we see a null pointer check, we know that the developer believes that the pointer may not be initialized. If the same pointer is later used without a null pointer check, we may consider this a violation of the developer's belief and ultimately a bug. We develop such a belief-guided program analysis for vulnerability detection (VD). For example, when an authentication function returns the same error for both, a wrong user name and a wrong password, an auditor may infer that the developer believes that both cases are indistinguishable, mitigating a user enumeration attack. This belief is reasonable, as it follows standard security practice. Yet, a function call inducing a difference in response time for both cases, contradicts this belief. This contradiction uncovers a timing side-channel that syntactic analysis tools would miss. Existing static analysis tools struggle with this type of flaw because they require them to be expressible by general, syntactic patterns. Our belief-guided approach detects such domain-specific, high-level semantic security flaws that remain elusive.
  Given a function, our approach, Creed, infers the developer's security-related beliefs, evaluates how reasonable each one is, and derives the conditions under which it is violated. In contrast to existing ML-based VD techniques, Creed explains the root cause, the symptoms, and the conditions under which each issue is exploitable. To address the context-dependency problem in the evaluation, we introduce two measures for explanation-based VD: recall quantifies how effectively an approach correctly explains a known vulnerability, and overhead quantifies the effort of inspecting its reports. On a recent real-world vulnerability benchmark, Creed detects both semantic and syntactic vulnerabilities more effectively than existing explanation-based VD tools, achieving the best effectiveness-effort trade-off.

# Reparo: Synthesizing and Validating Access Control Policies

- arXiv ID: `2610.41800v1`
- Authors: Ayesha Binte Mostofa, Gehao Zhang, Sam Stern, Juan Zhai, Pubali Datta
- Published: 2026-10-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2610.41800v1) | [pdf](https://arxiv.org/pdf/2610.41800v1)

## Abstract

Writing correct access control policies for software applications is difficult because it requires expertise in the authorization language and a thorough understanding of the application's authorization requirements. Existing synthesis and mining approaches assume explicit authorization inputs and a trusted reference policy. However, authorization logic is often distributed across code, comments, and documentation rather than captured in a single artifact, and developer-defined policies in real-world application repositories are often incomplete, outdated, or incorrect. We present Reparo, an LLM-aided pipeline for access control policy synthesis, repair, and validation. Reparo collects repository evidence for authorization intent and uses it to guide an LLM in generating an initial policy. It then uses official policy-language validation tools to identify and automatically repair errors. For semantic validation, a different LLM derives a behavioral oracle from the same repository evidence, consisting of concrete authorization requests with expected allow or deny decisions, which Reparo executes against the generated policy. We manually assess the oracle on a statistically sized sample of 390 test cases. We evaluate Reparo on 228 real-world GitHub repositories that use Cedar, OpenFGA, or Rego. In these repositories, 40.6-55.7% of the repository policies fail their language's validation tool, whereas Reparo produces 99.0-100% valid policies after repair. Agreement with the oracle is 98.2-99.6% for OpenFGA, 82.0-86.5% for Cedar, and 76.3-80.2% for Rego. Manual review confirms 91.5-96.9% of the sampled test cases as correct. Synthesizing and validating the policy for one repository takes about five minutes and costs $0.55-$1.57. These results show that repository evidence can support both access policy synthesis and independent validation, even when no reliable reference policy exists.

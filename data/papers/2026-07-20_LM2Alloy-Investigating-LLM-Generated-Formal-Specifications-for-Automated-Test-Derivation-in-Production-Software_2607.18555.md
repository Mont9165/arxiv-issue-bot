# LM2Alloy: Investigating LLM-Generated Formal Specifications for Automated Test Derivation in Production Software

- arXiv ID: `2607.18555v1`
- Authors: Tasmim Rashid, Muhammad Zubair Malik
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.18555v1) | [pdf](https://arxiv.org/pdf/2607.18555v1)

## Abstract

We present an exploratory study on using Large Language Models (LLMs) to generate Alloy formal specifications from both requirements documentation and production source code, and to derive executable test cases from those specifications. We evaluate on two real open-source Python libraries: Flipper, a feature flag management system, and Cerberus, a data validation library.
  In both cases, the LLM produced workable Alloy specifications and executable tests without any manual correction. For Flipper, our pipeline uncovered a genuine bug that the existing test suite had missed: the library silently accepts duplicate flag names, directly contradicting its documented uniqueness requirement. A direct LLM baseline--generating tests from the same README but skipping the Alloy step--achieved 68% branch coverage yet failed to catch this bug across all three independent runs. This suggests that introducing a formal intermediate representation can surface constraint-level defects that coverage-oriented generation may miss.
  For Cerberus, the code-derived specification captured an implicit abstraction over sized types that the documentation-derived spec omitted, producing two additional tests. Across both libraries, code-based specifications showed lower variance in test generation (mean SD = 2.15) than documentation-based ones (mean SD = 5.0), though whether this generalises remains an open question.
  Index Terms--formal specifications, Alloy, large language models, automated testing, specification drift, software validation.

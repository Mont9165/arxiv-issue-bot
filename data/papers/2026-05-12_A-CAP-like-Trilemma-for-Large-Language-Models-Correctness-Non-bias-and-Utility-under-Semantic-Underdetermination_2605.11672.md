# A CAP-like Trilemma for Large Language Models: Correctness, Non-bias, and Utility under Semantic Underdetermination

- arXiv ID: `2605.11672v1`
- Authors: Vinu Ellampallil Venugopal
- Published: 2026-05-12
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.11672v1) | [pdf](https://arxiv.org/pdf/2605.11672v1)

## Abstract

The CAP theorem states that a distributed system cannot simultaneously guarantee consistency, availability, and partition tolerance under network partition. Inspired by this result, this paper formulates a CAP-like conjecture for Large Language Models (LLMs). The proposed trilemma states that, under semantic underdetermination, an LLM cannot always simultaneously guarantee strong correctness, strict non-bias, and high utility. A prompt is semantically underdetermined when the given premises do not determine a unique answer. In such cases, a useful and decisive response requires the model to introduce a selection criterion, preference, prior, or value ordering. If this criterion is not supplied by the user or justified by the available premises, the response becomes biased in a broad selection-theoretic sense. Conversely, if the model avoids unsupported preferences, it may preserve correctness and non-bias but may reduce utility through refusal, hedging, or clarification. The paper formalizes this correctness--non-bias--utility trilemma, develops examples, and argues that certain LLM failures arise not merely from model limitations but from the structure of underdetermined decision requests.

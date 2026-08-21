# Escaping the Quicksand: A Call to Arms

- arXiv ID: `2608.19674v1`
- Authors: Peter Sewell, Jean Pichon-Pharabod
- Published: 2026-08-20
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.19674v1) | [pdf](https://arxiv.org/pdf/2608.19674v1)

## Abstract

Computing has been an astonishing success - but the accumulated technical debt exposes us all to huge costs in business and societal risk. For 75 years, we've built systems to prose specifications with test-and-debug development. That works well enough for industry to thrive, but it's an expensive and ineffective feedback loop, and leaves everyone relying on shaky foundations. Now, AI-enabled engineering is amplifying the success by reducing coding costs, but also amplifies the risks, by rapidly increasing technical debt, and by automating detection of the vulnerabilities therein.
  How can we do better? Research has long pursued mathematical proof of correctness, which, unlike testing, can cover all cases. This too has advanced massively, but it remains hard to apply, both technically and because of a deep-seated cultural disconnect.
  Instead, we argue for a pragmatic approach to flexible combinations of testing, *specification*, and proof, that provides more effective feedback loops for both AI and human development.
  Most simply, one can incrementally co-develop executable-as-test-oracle partial specifications alongside conventional prose descriptions, code, and tests. This clarifies design and makes testing much more discriminating. Developers can and should do it today.
  Or, even better, one can use specifications that support the full gamut of testing, property-based testing, symbolic execution, and proof. This enables a range of intertwined feedback loops, again both for AI and humans, from cheap testing to more expensive proof. However, making it really practical needs *semantics infrastructure*: specifications and tooling for the main programming languages and other abstractions, which we now more-or-less know how to build, but which is not yet in place. We call the community to arms to create and deploy it - to enable a future built on firmer ground.

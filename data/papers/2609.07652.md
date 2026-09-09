# RefVerifier: Semi-Automated Reference Claim Verification for Scientific Manuscripts

- arXiv ID: `2609.07652v1`
- Authors: Stefania Mocan, Florian Angermeir, Mark Kreitz
- Published: 2026-09-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.07652v1) | [pdf](https://arxiv.org/pdf/2609.07652v1)

## Abstract

As software engineering research submission counts surge, peer reviewers face severe time constraints, making systematic verification of citation-supported claims prohibitively expensive. Consequently, unsubstantiated claims and semantic drift can propagate undetected across scientific literature. Existing approaches such as fact-checking and retrieval-augmented generation tools operate on open-domain web data or evaluate claims in isolation without processing complete manuscripts. To address this gap, we present RefVerifier, a semi-automated, citation-bounded reference verification prototype designed to support in academic peer review. RefVerifier extracts citation-bearing sentences from manuscripts, checks bibliography metadata against scholarly databases, resolves references to full-text open-access PDFs, localizes relevant evidence passages, and generates verdicts with natural language explanations. Evaluating RefVerifier on public benchmarks shows claim detection at an F1 score of 0.990, open-access resolution of 57.6% of references, and evidence localization with a hit rate of 98% on abstracts and 68% on complete cited papers. In an end-to-end test with eight manuscripts, RefVerifier achieves a verdict accuracy of 71%. By automating document retrieval and evidence localization while preserving reviewer oversight, RefVerifier provides first indicators for the feasibility of semi-automated integrity checks in scholarly publishing.

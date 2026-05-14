# Finding a Crab in the C: Assured Translation via Comparative Symbolic Execution

- arXiv ID: `2605.12731v1`
- Authors: Caleb Helbling, Graham Leach-Krouse, Michael Crystal
- Published: 2026-05-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.12731v1) | [pdf](https://arxiv.org/pdf/2605.12731v1)

## Abstract

Modern high-assurance software systems development favors memory safe languages such as SPARK (ADA) or Rust. However, developers often encounter non-memory safe code (e.g., C) in legacy systems and libraries which would be prohibitively expensive or risky to re-write. In response, developers have begun turning to machine learning/AI systems and other automated code translators. Automated translation comes with its own risks, however. The original and ported code are not precisely the same, semantically - otherwise there would be no point in performing the translation. To reduce these risks, we have developed cozy, a comparative binary analysis tool that simultaneously analyzes a binary compiled from "unsafe" source code and a binary compiled from a translation of the source code to a memory safe language. cozy walks the developer through differences in the behavior of the two binaries, presenting each difference and asking the user to assess whether the difference is intentional (good) or erroneous. Outside of the flagged differences, the binaries are formally verified to be equivalent. Consequently, the review process guarantees equivalence modulo changes approved by the developer. cozy has applications to automated translation, bug correction, code reviews, operation authorization, and automatic translation.

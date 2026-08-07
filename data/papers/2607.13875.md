# Lexicographic Direct Access with Functional Dependencies

- arXiv ID: `2607.13875v1`
- Authors: Florent Capelli, Nofar Carmeli, Stefan Mengel
- Published: 2026-07-15
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.13875v1) | [pdf](https://arxiv.org/pdf/2607.13875v1)

## Abstract

We study the complexity of lexicographic direct access to join query answers over databases that satisfy functional dependencies (FDs). More precisely, we give fine-grained lower and upper bounds on the preprocessing time required to achieve polylogarithmic access time. We start by considering the simple approach of a reordered extension, which first incorporates the FDs in the query and order, and then ignores the FDs during evaluation. We show that this simple approach gives tight bounds for unary FDs but fails for general FDs. We then consider a second approach, inspired by size bounds for query answers using information theory, that takes the FDs into account while materializing the bags of a decomposition tailored to the direct access task at hand. Interestingly, we show that the same reordering is also useful while constructing the decomposition in this second approach for reducing the complexity. While the obtained upper and lower bounds are generally not tight, we show that they yield a complete characterization of lexicographic direct access with linear preprocessing time. All lower bounds in this paper apply only to queries without self-joins and rely on the Zero-Clique Conjecture.

# Complexity Theory of Randomised Testing

- arXiv ID: `2607.11811v1`
- Authors: Pingshi Yu, Chengsong Tan, Nicolas Wu, Alastair Donaldson
- Published: 2026-07-13
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.CC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.11811v1) | [pdf](https://arxiv.org/pdf/2607.11811v1)

## Abstract

Randomised testing is a widely-used approach to software validation, yet its theoretical foundations remain thin. In particular, the fundamental question of what it means for a set of inputs to be \emph{generable} has gone unanswered in both the literature and folklore. We present the first complexity-theoretic foundations for random generators in software testing. We model generators as Turing transducers that consume random bits and produce string-encoded outputs, and show that the theoretically generable languages coincide exactly with the recursively enumerable languages. This has direct implications for testing at the boundaries of decidability, such as compiler testing. For \emph{efficient} generation, we show that the polynomial-time generable languages lie within \textit{NP}, that certain \textit{NP}-complete languages admit efficient generators, and that -- under standard cryptographic assumptions -- there are languages in \textit{P} for which no efficient generator exists: the complexity of efficienct generation and of efficient decision are not the same. We show space-bounded complexity is the natural framework for generators producing \emph{correlated} samples, capturing methodologies such as coverage-guided fuzzing and symbolic execution. Beyond classification, we characterise efficient generability: a language has a polynomial-time generator iff it admits a \emph{certificate scheme} over a verifier -- so witness planting, the folklore technique behind generators to test SAT solvers, is in a sense the only route to efficient generation. On the design of property-based testing libraries, we prove no library can compositionally derive efficient generators from logical predicates involving conjunction or negation, under standard assumptions. However, restricted classes like \textit{NL} (equivalently, linear Datalog predicates) would admit such a compilation.

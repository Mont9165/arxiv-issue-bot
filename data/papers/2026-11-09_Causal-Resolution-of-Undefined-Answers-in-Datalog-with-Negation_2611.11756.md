# Causal Resolution of Undefined Answers in Datalog with Negation

- arXiv ID: `2611.11756v1`
- Authors: Ratan Bahadur Thapa
- Published: 2026-11-09
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.11756v1) | [pdf](https://arxiv.org/pdf/2611.11756v1)

## Abstract

Unstratified negation may leave the answer to a Boolean Datalog query undefined under the well-founded semantics. We study database causality in this setting by asking which fact insertions and deletions realize a prescribed transition and which other changes preserve the observed query answer while making a designated fact pivotal. Such a set of changes to other facts is a contingency for the designated fact and the prescribed transition. Our game representation assigns one shared move to each mutable fact and preserves query values and intervention distances. Pairing source and target certificates characterizes all minimum contingencies for the six transitions among true, false, and undefined. When inserting or deleting a move resolves a draw, a directed tree traces the newly winning and losing positions along alternating paths to the source of that move. For the fixed one-rule win--move program, deciding whether a contingency of size at most $k$ exists is $\mathrm{NP}$-complete for each transition, even on bounded-degree graphs. Computing the minimum size is $\mathrm{FP}^{\mathrm{NP}[\log]}$-complete, and counting minimum contingencies is $\#\mathrm{P}$-hard under polynomial-time Turing reductions. When only one of true and false is reachable, the prime implicants of undefinedness satisfied at the observation cover every undefined state, and their supports induce nonempty subtrees of a common tree, we compute a minimum resolving intervention in polynomial time from the game instance. From the explicit tree and these implicants, we construct an equally large family of disjoint supports, certifying optimality.

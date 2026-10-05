# Look Here or Look Across: Unified Cardinality Constraints for N-ary Relationships

- arXiv ID: `2610.02603v1`
- Authors: Huanyi Chen
- Published: 2026-10-01
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.02603v1) | [pdf](https://arxiv.org/pdf/2610.02603v1)

## Abstract

A cardinality constraint written on an edge of an entity-relationship diagram admits two opposite readings. Under the reading used by UML and by Chen's original model, the label is read with the entity set on the same side of the relationship; under the reading used by standard database textbooks, it is read with the entity set on the opposite side. The two readings are exact opposites, so a reader who assumes the wrong one takes away the opposite of what the designer meant. For binary relationships the difficulty is confined to interpretation, because the two constraints a binary relationship set admits can both be drawn. For relationships among three or more entity sets the picture is worse: a ternary relationship set admits twelve cardinality constraints, and a diagram with three edges can carry at most three of them. This paper presents a notation, Card(R; p; q) = (lower, upper), that removes the ambiguity without taking a side in it, and that is not limited to one constraint per edge. We give the number of constraints an n-ary relationship set admits, show which of them a design determines without ever writing them down, and state two inference rules, decomposition and augmentation, that derive one constraint from another, together with the side conditions under which each is sound. We close with a worked case study that turns three business requirements into three explicit constraints and nine more that the design decides on its own.

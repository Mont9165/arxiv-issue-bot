# Inconsistent Databases and Argumentation Frameworks with Collective Attacks

- arXiv ID: `2605.03954v1`
- Authors: Yasir Mahmood, Jonni Virtema, Timon Barlag, Axel-Cyrille Ngonga Ngomo
- Published: 2026-05-05
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.03954v1) | [pdf](https://arxiv.org/pdf/2605.03954v1)

## Abstract

The connection between subset-maximal repairs for inconsistent databases involving various integrity constraints and acceptable sets of arguments within argumentation frameworks has recently drawn growing interest. In this paper, we contribute to this domain by establishing a new connection when integrity constraints (ICs) include denial constraints and local-as-view tuple-generating dependencies. It turns out that SET-based Argumentation Frameworks (SETAFs), an extension of Dung's argumentation frameworks (AFs) allowing collective attacks, are needed. It is known that subset-maximal repairs under denial constraints correspond to the naive extensions, which also coincide with the preferred and stable extensions in the resulting SETAFs. Our main findings establish that repairs under the considered fragment of tuple-generating dependencies correspond to the preferred extensions. Moreover, for these dependencies, additional preprocessing allows computing a unique extension that is stable and naive. Allowing both types of constraints breaks this relationship, and even the pre-processing does not help as only preferred semantics captures these repairs. Finally, while it is known that functional dependencies do not require set-based attacks, we prove the same regarding inclusion dependencies. Thus, one can translate inconsistent databases under these restricted classes of ICs to plain AFs with attacks only between arguments.

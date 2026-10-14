# Detecting Rendering Bugs in Imperative Data Visualization Libraries via Equivalent Mutations

- arXiv ID: `2607.12363v1`
- Authors: Weiqi Lu, Yongqiang Tian
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.12363v1) | [pdf](https://arxiv.org/pdf/2607.12363v1)

## Abstract

Imperative data visualization libraries construct plots through a sequence of stateful API calls that incrementally create and update graphic elements. Rendering bugs in these libraries often manifest as incorrect visual outputs rather than crashes or exceptions, making them difficult to detect automatically. A fundamental challenge is the lack of an oracle that specifies the expected rendering of an arbitrary plotting script. Furthermore, an update to one graphic element may inadvertently affect other elements or properties, leading to subtle inconsistencies in the final rendered image.
  This paper presents VIZDETOUR, an automated testing approach for detecting rendering bugs in imperative data visualization libraries via equivalent mutations. The key idea is to transform the oracle problem into an equivalence-checking problem. Starting from a seed plotting script, VIZDETOUR appends a short sequence of semantically equivalent API calls that temporarily modify the visualization state and then restore it to its original state. Although these mutations exercise different execution paths, they should preserve the final rendering. Any visual discrepancy between the original and mutated scripts therefore indicates a rendering bug. To generate such mutations, VIZDETOUR constructs a render tree from the seed script, identifies traceable graphic elements and mutable properties, and synthesizes endpoint-preserving mutation sequences. It then compares the rendered outputs using perceptual hashing. We evaluate VIZDETOUR on matplotlib, bokeh, and plotly using scripts collected from their official example galleries. VIZDETOUR discovers 47 previously unknown bugs, of which 39 are confirmed and 18 are fixed.

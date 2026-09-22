# Goal-driven Variant Categorization

- arXiv ID: `2609.22475v1`
- Authors: Daniel Calegari, Daniel Amyot
- Published: 2026-09-18
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.22475v1) | [pdf](https://arxiv.org/pdf/2609.22475v1)

## Abstract

Process discovery rarely yields a single coherent process structure. For analysis, a common step is to cluster process variants based on structural similarity and then assign business meaning to the resulting groups. Since these partitions are not derived from the organization's goals, analysts must manually interpret and consolidate variants into business-meaningful categories. This judgment-intensive step becomes increasingly difficult as the number and complexity of variants grow. In this paper, we propose a goal-driven approach to variant categorization that reverses this workflow. We first author an organization's goal model that predefines the categorization axis. Each variant is transformed into a textual narrative describing its behavior, and a Large Language Model (LLM) interprets it in the context of the goal model and assigns the variant to the most appropriate category. LLM-based semantic reasoning connects low-level process behavior with analyst-defined business goals. We instantiate this approach end-to-end and evaluate it on three public logs differing substantially in scale and behavioral diversity. Goal-model guidance yields partitions that differ from those produced by unguided induction and respond to controlled edits to the declared alternatives, at the cost of authoring a goal model.

# ReConMem: A Graph-Based Dual Memory System for Repository-Oriented Conversations

- arXiv ID: `2611.07759v1`
- Authors: Zhishuo Yang, Li Zhang, Yang Liu, Donghao Yang, Fang Liu
- Published: 2026-11-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.07759v1) | [pdf](https://arxiv.org/pdf/2611.07759v1)

## Abstract

LLM-based code assistants are increasingly used in iterative repository-level development, where effective assistance requires jointly leveraging evolving conversational history and repository context. Existing memory systems, however, are primarily designed for general-purpose conversations and do not sufficiently coordinate conversational information with the structured code entities to which it refers. We propose ReConMem, a graph-based dual memory system for repository-oriented conversations. ReConMem organizes distilled conversational memories and conversation-relevant code entities into interconnected semantic and structural memory graphs, while maintaining their cross-graph associations as interactions evolve. For memory recall, ReConMem combines natural-language and code-aligned retrieval through code-draft-based query grounding, expands retrieved information over intra- and inter-graph relations, and compresses retrieved code according to its structural granularity. We evaluate ReConMem on two repository-oriented conversational benchmarks spanning long-horizon context management and realistic project-grounded multi-turn assistance. On LoCoEval, ReConMem improves Pass@1 over the strongest baseline by 7.917 and 7.292 percentage points on single-hop and multi-hop subsets, respectively, with comparable context compression. On CodeAssistBench, it achieves 27.61% Correct and 44.03% Partially Correct, exceeding Full History by 4.10 and 7.09 percentage points, respectively, while improving interaction quality. These results demonstrate that aligning conversational memory with repository structure improves context management for repository-oriented multi-turn interactions.

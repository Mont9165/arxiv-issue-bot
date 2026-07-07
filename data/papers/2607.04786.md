# An Exploration of Agentic Information Fusion for Test Maintenance Prediction

- arXiv ID: `2607.04786v1`
- Authors: Jingxiong Liu, Nasser Mohammadiha, Gregory Gay
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2607.04786v1) | [pdf](https://arxiv.org/pdf/2607.04786v1)

## Abstract

Test maintenance is a critical, yet costly, activity - particularly as codebases rapidly evolve. To assist, we present MAST, a multi-agent framework that predicts which test cases require maintenance following changes to the production code. This identification task is necessary as a precondition to any subsequent maintenance activities, but remains challenging due to the complex relationships between production and test code. MAST advances the state-of-the-art by integrating multiple analyses -- including static, lexical, and semantic analyses - through an intelligent fusion and post-check procedure and by focusing on a realistic use and evaluation setting - i.e., standardized input formats, repository-level analyses, and the ability to infer relations between test and production artifacts rather than assuming a pre-existing mapping.
  We evaluated MAST on 21 industrial Java repositories from Ericsson AB, considering situations where test maintenance both was and was not required in the ground truth. MAST yielded superior precision to a state-of-the-art baseline - resulting in a higher accuracy, F1, and F2 score - with only some loss in recall. Our ablation study demonstrates the value of each analysis in producing the final recommendations. MAST illustrates the potential of multi-agent systems that can fuse multiple information sources when performing software testing tasks.

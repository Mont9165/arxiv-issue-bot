# LITMUS - Literature Informed Testbed for Mapping Usecases and Synthesizing Risk-Cards

- arXiv ID: `2611.29034v1`
- Authors: Seshu Tirupathi, Elizabeth M. Daly, Radu Marinescu, Javier Carnerero Cano, Yannis Belkhiter
- Published: 2026-11-21
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.29034v1) | [pdf](https://arxiv.org/pdf/2611.29034v1)

## Abstract

The proliferation of large language models (LLMs) and Artificial Intelligence (AI) in real-world applications has heightened the need for systematic, safety-oriented deployment frameworks. Existing approaches typically prioritize the construction of datasets and risk cards around the LLM and AI architecture itself, yet they provide scant consideration for the specific use-case that drives model selection. This omission is problematic because any practical AI deployment begins with a detailed use-case description that informs the assessment of contextual hazards. In this paper, we introduce a structured pipeline that, given a use-case, automatically produces a tailored dataset and an accompanying risk card. The process ensures that identified risks are tightly coupled to the use-case, and it offers traceable evidence from peer-reviewed literature to substantiate each risk to use-case relationship. Prior claim-verification methods (FActScore, FactReasoner) have been validated for factual claims. Risk-relevance is a hypothetical claim about possible harm, and whether evidence retrieval can meaningfully assess such claims remains untested. Literature-Informed Testbed for Mapping Use-cases and Synthesizing (LITMUS) risk cards are the first systematic attempt to characterize this adaptation. We evaluated the pipeline using the MIT Risk Taxonomy and achieved a 0.91 F1-score with a list of 320 samples from the benchmark risk dataset that was considered. These results demonstrate the effectiveness of our approach in generating robust, evidence-based risk assessments for LLM deployments.

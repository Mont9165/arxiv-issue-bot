# Semi-Automatic Quantification of Bayesian Networks for Software Decision Support: Comparing WSA and RNM in a Software R&D Organization

- arXiv ID: `2609.31275v1`
- Authors: Mirko Perkusich, João Nunes, Emilia Mendes, Emanuel Dantas, Ademar Sousa, Danyllo Albuquerque, Kyller C. Gorgônio, Angelo Perkusich
- Published: 2026-09-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.31275v1) | [pdf](https://arxiv.org/pdf/2609.31275v1)

## Abstract

Expert-driven Bayesian networks can support recurring software decisions when historical data are limited, but quantifying their conditional probability tables (CPTs) requires many probability judgments. Semi-automatic methods reduce direct elicitation, yet practitioners have little comparative evidence from operational decision processes. We report an embedded case study comparing the Weighted Sum Algorithm (WSA) and Ranked Nodes Method (RNM) as complete elicitation-and-quantification pipelines in two contexts within a single software research and development (R&D) organization: feature selection for Internet of Things projects and user interface design selection. Within each context, the pipelines shared the graph, root priors, and decision evidence. We evaluated them through 15 expert-defined model-walkthrough scenarios and retrospective reconstructions of alternatives recorded in decision meetings. WSA matched 7/7 and 6/8 walkthrough expectations, whereas RNM matched 4/7 and 4/8. Both pipelines placed the selected alternatives near the top of the retrospective rankings. Their complete distributions nevertheless differed: the median total variation distance was 0.304 across four distinct feature patterns and 0.340 across seven distinct design patterns, rising to 0.890 for one design pattern. These results concern two ordinal value-estimation models in one organization. They show that similar shortlist behavior does not imply equivalent representations of uncertainty. For comparable software decision-support models, method selection and validation should consider node semantics, the judgments experts can provide, calibration requirements, complete output distributions, and the intended downstream use of the probabilities.

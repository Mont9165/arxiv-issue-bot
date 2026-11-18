# Growing Clusters Lower the Bar: Profile Accretion in LLM-Based Incremental Entity Resolution

- arXiv ID: `2611.22485v1`
- Authors: Huixue Han, Shangzhi Xu, Anqi Xiong, Yu-Chu Tian
- Published: 2026-11-17
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.22485v1) | [pdf](https://arxiv.org/pdf/2611.22485v1)

## Abstract

Incremental entity resolution pipelines ask a large language model (LLM) whether a new record belongs to an existing cluster and show it the records already linked. Analyses of matching oracles assume that the answer depends only on the records compared. For the LLM matchers we test, it depends on cluster size, and the model lowers its bar for joining a cluster as the cluster grows. On French procurement suppliers from FOPPA, with SIREN identifiers as ground truth, we hold the new record fixed and vary only the number of verified members shown. Sixteen members instead of one raise the false match rate on similarly named companies by \dfmrMin--\dfmrMax{} percentage points in six open-weight models, while their area under the ROC curve rises by only \aucGainMin--\aucGainMax. In Claude Sonnet~5 and Haiku~5.5 the rise is \clSonD{} and \clHaiD{} points. The shift persists with street addresses, prompt variants and the BatchER and ComEM formats, and one false merge raises acceptance of the intruder's other records in every open model. It does not arise on Czech and Bulgarian TED notices, where one record with its full address already identifies the company. In online linking on confusable blocks, a single threshold set on labelled data raises recall by a factor of \fxRRmin--\fxRRmax{} for five models with no detectable loss of precision and no extra LLM calls.

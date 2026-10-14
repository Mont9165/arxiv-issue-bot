# Mind the Gaps: From Failure Attribution to Closed-Form Repair of Code Language Models

- arXiv ID: `2610.05277v1`
- Authors: Jian Gu, Hongyu Zhang, Chunyang Chen, Aldeida Aleti
- Published: 2026-10-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.05277v1) | [pdf](https://arxiv.org/pdf/2610.05277v1)

## Abstract

Code language models must be maintained like the software around them: when a library evolves, a model keeps writing the interface that it saw during training. Repairing the model itself lets one correction reach all downstream uses. Existing repair methods attribute a failure to neurons, select the highest-ranked ones, and apply a generic update. This pipeline assumes that the attributed neurons are the ones to patch and that a generic update fits every failure, and neither assumption has been examined. We examine both on executable API evolution tasks in Python and Rust with three code models and identify two gaps. The targeting gap separates the neurons that failure attribution targets from the neurons that can carry a patch: their top sets have a Jaccard overlap of only 0.15 to 0.20. The tailoring gap separates a generic update from a patch built for the failure: the patches that different carrier neurons need are nearly orthogonal. To address both gaps, we propose ASTRA. It targets neurons by contrastive semantics, an attribution that scores a neuron by its contribution to the logit contrast between the target token and the produced token. It then tailors the patch by solving one small linear system in closed form, which corrects all failing tokens of a sample jointly and needs neither an optimizer nor a backward pass. Contrastive semantics selects significantly better carrier neurons than gradient-based attributions in 3 of 6 settings and comparable ones in the others. On average, ASTRA reaches 66.7 percent Pass@1, against 48.4 percent for the best of AlphaEdit, STAR and low-rank adaptation, and repairs a sample in 2.7 seconds. It is the best method in all 6 settings and for every type of API change, and this advantage persists under an unseen phrasing of the test prompt. Its side effects on unrelated code are small on the large models and larger on the small one.

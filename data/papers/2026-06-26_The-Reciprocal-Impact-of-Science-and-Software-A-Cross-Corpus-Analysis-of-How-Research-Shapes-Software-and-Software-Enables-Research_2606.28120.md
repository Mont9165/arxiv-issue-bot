# The Reciprocal Impact of Science and Software: A Cross-Corpus Analysis of How Research Shapes Software and Software Enables Research

- arXiv ID: `2606.28120v1`
- Authors: Audris Mockus
- Published: 2026-06-26
- Primary category: `cs.DL`
- Categories: `cs.DL`, `cs.SE`, `cs.SI`
- Links: [abs](http://arxiv.org/abs/2606.28120v1) | [pdf](https://arxiv.org/pdf/2606.28120v1)

## Abstract

Software and scientific knowledge co-evolve, yet they are catalogued in separate corpora that rarely speak to one another. We bridge them at global scale by linking World of Code (a near-complete mirror of public version-control history) to Semantic Scholar and OpenAlex through a typed cross-corpus graph of 69.8M edges over eight relation types (paper-to-software mentions, software-to-paper citations, software dependencies, authorship, affiliation, and identity bridges). Anchoring on 18,247 curated science repositories, we ask two reciprocal questions: what is the impact of science on software, and of software on science? To test whether this Science-Software Supply Chain (S3C) view is feasible, we run basic investigations rather than claim a definitive measurement. The two directions appear to illuminate different, complementary strata: the literature's reach into software is dominated by a reproducibility and packaging layer (nf-core, Nextflow, Bioconda) and sequence-analysis tools, whereas software's reach back into science is proxied by a largely invisible machine-learning and data-science infrastructure tier (PyTorch, seaborn, NLTK). The direct paper-names-software channel is too sparse to rank: a human-curated gold benchmark links none of its 65 in-scope cases. Dependency reuse stands in as a proxy and is at most weakly coupled to citation count and to stars (Spearman rho=0.36). Our most cautionary finding is about measurement itself: the reuse-citation coupling flips sign and confidence across two reasonable ways of pairing a repository with a citation count, through papers that name it (n=137, rho=0.05, CI straddling zero) versus DOIs a repository declares for itself (n=1,067, rho=0.13, CI [0.07,0.19]). With linkage this sparse, the sign of a headline correlation depends on which gap one tolerates, so we report both and refrain from a strong decoupling claim.

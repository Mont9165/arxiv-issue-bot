# Can LLMs Reliably Annotate Bioassay Metadata to Improve Data Readiness?

- arXiv ID: `2610.01616v1`
- Authors: Laura van Weesep, Riccardo Tedoldi, Jens Sjölund, Hossein Azizpour, Susanne Winiwarter, Ola Engkvist, Jon Paul Janet, Samuel Genheden, Juan Viguera Diez
- Published: 2026-10-01
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`, `q-bio.QM`
- Links: [abs](http://arxiv.org/abs/2610.01616v1) | [pdf](https://arxiv.org/pdf/2610.01616v1)

## Abstract

The emergence of foundation models for molecular property prediction requires a high degree of AI data readiness, including reliable metadata annotation. However, both public repositories and industrial screening databases suffer from missing, inconsistent, or conflated assay annotations. In this work, we quantify the extent of missing annotations in PubChem for the BioAssay Ontology (BAO) assay format and physical detection method fields and investigate whether open-source and proprietary large language models (LLMs) can reliably predict and audit metadata annotations directly from the assay text. In our assessment, we found that the annotation coverage across PubChem's $\sim$2 million bioassays is critically sparse, 36\% lacking an assay format, 89\% a BioAssay type, and >99.9\% any BAO-mapped assay format or detection technology term. This motivates the need for automated test-metadata curation. Using evaluation sets derived from PubChem and ChEMBL, we assess the agreement of seven open-source and proprietary LLMs with existing silver labels. Recall is at least 0.96 for biochemical and cell-based assay formats, with a similar pattern for detection technology, although disagreements increase on under-represented classes. Manual inspection shows that many of these disagreements trace back to inconsistencies between silver sources rather than to LLM error. Moreover, in a qualitative study with a senior industrial curator, LLM-generated evidence prompted the expert to revise some of their own labels, showing LLMs can flag potentially mislabeled assays. Across the study, performance differences between proprietary and open-source models were small. Together, these results suggest LLMs can support the large-scale annotation and auditing of assay metadata, though per-class reliability estimates and targeted human review remain necessary before such labels enter downstream ML pipelines.

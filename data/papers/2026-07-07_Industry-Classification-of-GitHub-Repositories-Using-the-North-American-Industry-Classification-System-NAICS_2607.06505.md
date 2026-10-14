# Industry Classification of GitHub Repositories Using the North American Industry Classification System (NAICS)

- arXiv ID: `2607.06505v1`
- Authors: Kevin Xu, Alexander Quispe
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.06505v1) | [pdf](https://arxiv.org/pdf/2607.06505v1)

## Abstract

GitHub hosts hundreds of millions of public repositories, but the platform exposes no native mapping from repositories to standardized industry sectors. This gap limits empirical work on the geography of innovation, the industrial composition of open-source production, and the diffusion of new technologies across economic sectors. We present NAICS-GH, a publicly released corpus of 6,588 GitHub repositories drawn from source pools covering the United States, the European Union, and Australia, each labeled with a 2-digit sector from the North American Industry Classification System (NAICS 2022). Labels are produced by a retrieve-and-verify pipeline that combines BAAI/bge-large-en embeddings, FAISS retrieval, and GPT-4.1 rubric scoring. The pipeline narrows about 1.37 million source repositories to 31,178 candidate repository-sector pairs and retains 6,588 high-confidence labels with score at least 8. Re-running the retrieval pipeline end to end reproduces the candidate set to within 0.03 percent. On a 2,421-repository human-validated random sample, the released labels attain 96.98 percent precision, with Wilson 95 percent confidence interval [96.23, 97.59]. We benchmark six pretrained encoders on the released corpus; RoBERTa-large reaches 86.45 percent F1 and 86.35 percent accuracy on a held-out 20 percent test set. The dataset, Croissant metadata, pipeline code, prompts, and fine-tuned checkpoint are released under CC-BY-4.0 and MIT licenses.

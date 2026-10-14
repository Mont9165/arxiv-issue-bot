# Smart Contracts Claimed Vulnerable by the CVE Database, with Labels and Source Locations

- arXiv ID: `2609.01186v1`
- Authors: Monika di Angelo, Gernot Salzer
- Published: 2026-09-01
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.01186v1) | [pdf](https://arxiv.org/pdf/2609.01186v1)

## Abstract

The Common Vulnerabilities and Exposures (CVE) database catalogs vulnerability claims in hard- and software, among them those pertaining to blockchain programs a.k.a. smart contracts. We present CVE-Smart-Contracts, a curated dataset of CVE records up to July 2026 referring to Ethereum smart contracts. The dataset contains the vulnerable artifacts (source code and runtime bytecode), labels according to three taxonomies, and function-level locations. The retrieval of CVE records, collection of additional evidence, validation of the correspondence between records and artifacts, label assignment, and vulnerability localization are automated, leaving 15% to manual analysis. The dataset does not validate the original vulnerability claims, but marks a few records obviously wrong as `refuted'. For the sake of reproducibility, all external inputs are retained, so that rerunning the pipelines results in the same outputs. The dataset comprises 491 records linked to deployed contracts, 26 referring to projects (mostly libraries), 45 without validated artifacts, and six records with refuted claims. The dataset supports empirical security research, in particular the evaluation of code analysis and repair techniques.

# Value-level data provenance in an electronic laboratory notebook used by humans and language-model agents: An experience report

- arXiv ID: `2610.27859v1`
- Authors: Oleksiy V. Penkov, Boyang Shen
- Published: 2026-10-20
- Primary category: `physics.app-ph`
- Categories: `physics.app-ph`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.27859v1) | [pdf](https://arxiv.org/pdf/2610.27859v1)

## Abstract

A published laboratory number can be verified only when its raw file and extraction method are known. This paper presents the value-level provenance architecture of APS ELN, an electronic laboratory notebook used by both researchers and language-model agents. The architecture was motivated by a production audit in a materials laboratory covering projects performed over almost 5 years. Tracing eight baseline studies from sample to stored value showed that the initial ELN structure preserved the link from sample to raw file. Still, the link from raw file to stored value was lost, mainly due to human factors: manual entries carried no file reference or extractor version. To close this gap, the database design and workflow were reworked so that every stored value records its source file, the data file reader/viewer (DFR) plugin and version, any interactive analysis selection, or the server-side formula for derived quantities. An automated drift check re-runs each DFR on the stored files. In two end-to-end validation studies recorded by agents in X-ray reflectivity and tribology, all stored values retained verifiable provenance with zero drift. A comparison with five other platforms shows that none binds individual stored numbers to both their source files and extractor versions.

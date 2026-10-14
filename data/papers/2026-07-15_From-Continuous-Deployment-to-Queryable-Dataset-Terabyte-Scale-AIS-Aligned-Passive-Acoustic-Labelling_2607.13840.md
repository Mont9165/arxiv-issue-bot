# From Continuous Deployment to Queryable Dataset: Terabyte-Scale AIS-Aligned Passive Acoustic Labelling

- arXiv ID: `2607.13840v1`
- Authors: Wayne Renaud, Priyanka Aravindan, Gabriel Spadon
- Published: 2026-07-15
- Primary category: `cs.SD`
- Categories: `cs.SD`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.13840v1) | [pdf](https://arxiv.org/pdf/2607.13840v1)

## Abstract

Long-duration passive acoustic deployments produce large archives of recordings that are not linked to vessel tracks or encounter structure, leaving range and contact conditions unavailable as variables and requiring manual selection for analysis. To address this limitation, we propose a database-native workflow that aligns hydrophone recordings with Automatic Identification System (AIS) position reports to produce distance-resolved data. Fixed-duration recording windows and AIS messages are stored as persistent geospatial tables and associated through an indexed spatiotemporal join, replacing in-memory nested iteration with a single scalable set-based database process capable of handling continuous, multi-year, million-window archival deployments without exhausting available memory. In this study, the approach processes approximately 9.5x10e5 recording windows and 6.9x10e6 AIS position reports, producing a structured table that separates no-contact, single-contact, and two-contact windows, with the closest point of approach computed directly where applicable and background conditions characterized via deterministic spectral ranking. This formulation enables a GeoAI framework in which spatially indexed, queryable data become directly usable for machine learning. The resulting data product reveals predominantly noise-dominated conditions, with vessel contributions emerging mainly at shorter ranges, indicating that the task lies in extracting structure under background-limited regimes. Spectrogram and quantitative analyses show weak tonal signatures embedded in noise and a consistent decay of signal-to-noise ratio with distance, supporting the use of this representation for scalable machine learning, similarity analysis, and predictive acoustic modelling in real maritime environments.

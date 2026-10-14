# STRATOS: Bridging the Symbolic-to-Numeric Gap in Spatio-Temporal Text-to-SQL for Meteorological Data

- arXiv ID: `2607.03501v1`
- Authors: Yi Zhang, Farhad Nooralahzadeh, Jonathan Fürst, Fabio Scherrer, Antonis Bezes, Vassiliki Kotroni, Kurt Stockinger
- Published: 2026-07-03
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2607.03501v1) | [pdf](https://arxiv.org/pdf/2607.03501v1)

## Abstract

Copernicus, the European Union's Earth observation program, produces petabytes of Earth observation and climate data, offering immense potential for research, policy, and applications. However, access to these datasets requires advanced programming skills and familiarity with domain-specific formats such as NetCDF or GRIB. Moreover, general-purpose Text-to-SQL systems fail when applied naively to the meteorological domain due to a profound ``Symbolic-to-Numeric'' gap. To overcome these limitations, we present an end-to-end Text-to-SQL framework specifically engineered for real-world, scalable meteorological data exploration. Our system intercepts natural language to resolve spatial and semantic ambiguities \textit{before} SQL generation. We design STRATOS, a Spatio-Temporal Resolution Agent for Text-to-SQL to dynamically bridge the symbolic-to-numeric gap by mapping fuzzy concepts to a localized ontology and resolving spatial entities via external knowledge bases. Further, our complexity-aware query rewriter rewrites expensive spatial predicates, reducing execution times from hours to seconds. Last, we introduce the STRATOS Evaluation Workload, comprising 7,520 complex query pairs explicitly designed by domain experts to test scalability and symbolic-to-numeric translation across challenging spatio-temporal dimensions previously unexplored by Text-to-SQL systems.

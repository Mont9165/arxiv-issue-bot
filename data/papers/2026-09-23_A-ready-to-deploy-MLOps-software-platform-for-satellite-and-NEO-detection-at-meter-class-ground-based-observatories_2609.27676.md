# A ready-to-deploy MLOps software platform for satellite and NEO detection at meter-class ground-based observatories

- arXiv ID: `2609.27676v1`
- Authors: Rafael Carrillo Navarro, Pablo García-Martín, René Duffard, Juan Luis Orellana Montes de Oca, Oscar Ortega Ríos
- Published: 2026-09-23
- Primary category: `astro-ph.IM`
- Categories: `astro-ph.IM`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.27676v1) | [pdf](https://arxiv.org/pdf/2609.27676v1)

## Abstract

Ground-based astronomical observations frequently contain streaks produced by artificial satellites, space debris, and potentially Near-Earth Objects (NEOs). While machine-learning models can reliably detect these features, their practical adoption in observatory operations is often limited by the lack of integrated tools for visual inspection, validation, workflow management, and structured data storage.
  This paper presents the StreakMind Workbench, a framework that applies MLOps practices to bridge research-oriented machine-learning pipelines with routine observatory operations. Rather than introducing new detection algorithms, the Workbench addresses a software-engineering challenge in astronomical computing: maintaining a single authoritative source of scientific processing code while providing astronomers with an operational environment for workflow execution and result inspection.
  Integrated with the reference StreakMind AI model of Carrillo et al. (2026) and implemented in Python using PyQt5, the Workbench supports the complete workflow from FITS ingestion to database storage, including inference, result inspection, database exploration, training management, and Minor Planet Center formatted observations. Validation on 273 images from La Sagra Observatory demonstrates successful end-to-end workflows while maintaining consistency with the underlying StreakMind scientific code. The platform facilitates operational use of a research ML pipeline in meter-class observatories and moderate-scale campaigns, supporting Space Situational Awareness and planetary defence.

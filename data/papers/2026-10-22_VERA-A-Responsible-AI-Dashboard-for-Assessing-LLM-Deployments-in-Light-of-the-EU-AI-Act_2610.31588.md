# VERA: A Responsible AI Dashboard for Assessing LLM Deployments in Light of the EU AI Act

- arXiv ID: `2610.31588v1`
- Authors: Robin Quériaux, Solveig Bachellery, Léa Déléris, Saurabhsingh Rajput, Mariam Barry, Tushar Sharma, Jérôme Lebecq
- Published: 2026-10-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CY`
- Links: [abs](http://arxiv.org/abs/2610.31588v1) | [pdf](https://arxiv.org/pdf/2610.31588v1)

## Abstract

Institutions that deploy large language models in regulated settings often need technical evidence of responsible AI practices before approving a deployment. COMPL-AI provides a technical interpretation of the EU AI Act that organises this evidence under six principle groups and eighteen technical requirements, twelve of which current benchmarks can measure. The benchmark suites that produce this evidence are typically operated from a command line, while the staff who approve deployments are non-engineers. We present VERA, an open-source self-hosted dashboard deployed to facilitate responsible AI processes within a large European bank. A reviewer selects a model and runs public benchmarks against it. VERA scores the twelve requirements that current benchmarks can measure and instruments the energy consumed by each evaluation, adding run-level evidence for environmental impact. We run four served open-weight models through the requirement pipeline, and the dashboard displays a score for each measurable requirement. A within-subject study then compares how participants read these benchmark results: from the raw output files in one condition, and through the VERA dashboard in the other. The dashboard reduced the time needed to perform the responsible AI assessment, reducing the time required from 56 seconds using raw files to 30 seconds using our dashboard, on average. Our dashboard scored highly (4.36 out of 5) on usefulness in the survey conducted within the organization. The dashboard and the study material are released publicly to promote replicability and reproducibility in different organisational contexts.

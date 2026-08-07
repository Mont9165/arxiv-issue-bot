# CURATE: Leveraging LLM Agents to Compose, Catalog, and Deploy Reproducible Workflows

- arXiv ID: `2608.04270v1`
- Authors: Nolan Cutler, Chia-Chen Kuo, Nanda Velugoti, Kathryn Newhart, Renato Figueiredo
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2608.04270v1) | [pdf](https://arxiv.org/pdf/2608.04270v1)

## Abstract

Agentic code generation has shown promise in automating and accelerating software development by utilizing Large Language Models (LLMs) to generate, test, and deploy code. For engineers and scientists, such systems have the potential to accelerate the development of applied and scientific workflows while reducing barriers to entry in domains that have yet to fully realize their benefits. However, a key gap remains: existing coding agents primarily focus on code generation and do not address the entire workflow lifecycle, including deployment and sharing. As a result, users develop and stitch modules independently while managing deployment on their own. To address this gap, we propose CURATE - Composition, User-in-the-loop, Reuse, and Automated Task Execution - a novel human-in-the-loop multi-agent system that uses LLM agents to manage and develop composable workflows across their entire lifecycle. A key feature of the system is a catalog that allows for the storage and reuse of modules across workflows. Module catalogs provide a foundation that can be expanded to support FAIR principles by facilitating the sharing and reuse of curated modules and subgraphs. We demonstrate the feasibility of our system with an initial prototype using Claude Opus 4.8, comprising 6 experiments: reproducing and adapting 4 workflows derived from the SeBS-Flow benchmark suite, and automating the development and scaling of a workflow that leverages a complex mechanistic model in environmental engineering used to simulate anaerobic digestion.

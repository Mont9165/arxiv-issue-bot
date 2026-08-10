# Taxonomy-Driven Analysis of Open-Source AI Risk Mitigation Tools

- arXiv ID: `2608.07446v1`
- Authors: Afreen Alam, Evgenija Popchanovska, Ana Gjorgjevikj, Maryan Rizinski, Lubomir T. Chitkushev, Irena Vodenska, Dimitar Trajanov
- Published: 2026-08-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CY`
- Links: [abs](http://arxiv.org/abs/2608.07446v1) | [pdf](https://arxiv.org/pdf/2608.07446v1)

## Abstract

Rapid adoption of large language models (LLMs) in enterprise settings has introduced operational, security, and governance risks. As generative AI applications move from pilot to production, manual harm identification and mitigation are becoming difficult to scale. Although many tools support model evaluation, adversarial testing, runtime guardrails, and observability, the tooling landscape remains fragmented. Tools are typically designed for specific engineering tasks and described in technical terms that do not align with governance frameworks or risk taxonomies, making it difficult to determine which tools address which risks and where critical gaps remain. This paper proposes a structured protocol to automate AI risk mitigation through a taxonomy-driven analysis of open-source LLM evaluation and security tools. We map the capabilities of 21 prominent open-source tools to the 32 subcategories of the extended MIT AI Risk Mitigation and Response Taxonomy. An LLM-assisted retrieval-augmented generation pipeline analyzes source code and documentation to extract capabilities for each taxonomy category. Reliability assessment yielded moderate agreement (Fleiss' Kappa = 0.509) among three independent reviewers. The analysis reveals a highly skewed landscape in which tools cluster around technical and operational controls, while governance, legal and regulatory, and financial and market controls remain largely unaddressed. This motivates a layered risk-mitigation architecture combining tool-based controls with organizational and regulatory processes. The mapping protocol achieved an F1 score of 75.5% after majority voting. Overall, the study provides a practical mapping between enterprise AI risk categories and open-source mitigation capabilities, identifies where human oversight remains necessary, and presents a taxonomy-driven framework applicable to open-source and proprietary solutions.

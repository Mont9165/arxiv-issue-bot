# Tytan: Interactive Neurosymbolic Construction of Analytic Semantic Schemas from Relational Data

- arXiv ID: `2608.06331v1`
- Authors: Donna Hooshmand, Shubham Shahi, Cameron Barrie, Abhratanu Dutta, Marko Sterbentz, Harper Pack, Kristian J. Hammond
- Published: 2026-08-06
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.06331v1) | [pdf](https://arxiv.org/pdf/2608.06331v1)

## Abstract

From natural-language query interfaces to automated report generation, data analysis tools need a description of the data: the real-world entities it contains, which columns function as measures or identifiers, and how tables connect into units of analysis. Today, this semantic layer is usually written by hand. This is a knowledge-acquisition bottleneck that limits the scalability of analytic systems, keeps non-technical users dependent on experts, and is itself error-prone. We present TYTAN, a system for automatically constructing an analytic semantic schema from a relational database and, when available, a short user-provided description. TYTAN combines symbolic analysis of the database with LLM-based semantic inference for entity proposal, role assignment, and naming. When the evidence leaves a decision ambiguous, TYTAN asks the user a targeted natural-language question. We evaluate TYTAN on eight databases spanning real-world and benchmark domains along the three axes that define a schema's functional utility: (i) coverage, are all important entities and features captured?; (ii) retrieval correctness, do the schema's instructions actually reach the data; and (iii) characterization accuracy, are semantic types correct? Across the seven reference domains, TYTAN reaches every entity, attribute, and aggregable feature of the expert-corrected reference schemas (100% coverage). Additionally, 100% of its retrieval instructions execute correctly (1,678 of 1,678 self-generated claims), and semantic roles agree with the reference on 92-100% of matched attributes. Checking the underlying data showed the small disagreement is in the reference, not in TYTAN. On a held-out blind test (a live, ten-table database with no declared keys), TYTAN recovers the full entity structure with verified keys and satisfies 100% of the satisfiable expectations of five independent blind annotators.

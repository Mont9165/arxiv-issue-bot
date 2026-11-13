# HeriKGQA: Grounded Knowledge-Graph Question Answering over Cultural Heritage Sensor Data

- arXiv ID: `2611.15904v1`
- Authors: Lingxiao Kong, Vasileios Arampatzakis, Vasileios Sevetlidis, George Pavlidis, Zeyd Boukhers
- Published: 2026-11-11
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2611.15904v1) | [pdf](https://arxiv.org/pdf/2611.15904v1)

## Abstract

Cultural heritage sites are increasingly monitored by sensor networks, but querying their data requires database expertise. Large Language Models (LLMs) offer a natural-language interface, yet over raw sensor records they lose track of which sensor, site, and time each value belongs to, and silently miscompute. We present HeriKGQA, a knowledge-graph question-answering method that confines the LLM to interpreting questions and phrasing answers, leaving computation to SPARQL and deterministic code. Questions are parsed into intents constrained by a heritage ontology aligning W3C SOSA/SSN with CIDOC-CRM, compiled into SPARQL, and answered from query results and temporal, spatial, and anomaly facts derived by a grounding layer, with error correction guarding each LLM step. On 500 questions over real data from five heritage sites, HeriKGQA reaches 99.0% accuracy, 18.2 points above the strongest of three baselines using the same LLM and receiving the same anomaly rules and answer conventions, with comparable answer quality while running almost four times faster. Without grounding, accuracy drops by 12.2 points and on anomaly questions from 99% to 66%. We report lessons from development and live deployment.

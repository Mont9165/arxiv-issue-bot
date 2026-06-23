# Identifying Quality Indicators in Student Self-Reflections in Software Engineering

- arXiv ID: `2606.22683v1`
- Authors: Matthew Minish, Matthias Galster, Fabian Gilson
- Published: 2026-06-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.22683v1) | [pdf](https://arxiv.org/pdf/2606.22683v1)

## Abstract

Context: Reflection is a fundamental skill in software engineering education, particularly in project-based courses where students learn through extended group work and need to develop their ability to reflect iteratively throughout their work. For students to benefit from reflection, their written reflections need to be assessed so that feedback can guide and improve their reflective practice. However, manually assessing written reflections to guide reflections is time-consuming, and often results in broad, non-specific feedback for a student to improve. Objective: This study builds on reflective writing frameworks to produce an eight-indicator scheme for assessing student reflections in software engineering. Furthermore, this study validates an automated classifier for assessing reflections against the framework, enabling scalable and structured feedback whilst reducing instructor workload. Method: We adapted existing reflection frameworks through iterative refinement to create our eight-indicator framework. Three annotators labelled student reflection texts, establishing moderate to reliable inter-rater agreement. We then trained and evaluated multiple encoder-only transformer models and compared them with decoder-only large language models using zero-shot prompting. Results: The fine-tuned RoBERTa model achieved the strongest performance, substantially outperforming decoder-only models in both accuracy and speed. The classifier demonstrated human-level agreement on most indicators whilst enabling near-instantaneous classification. We provide two model variants optimised for different assessment priorities. Conclusions: Our fine-tuned encoder-only models enable efficient automated assessment of reflective writing. The framework and automated classifier offer a means to provide timely, structured feedback on student reflections in software engineering.

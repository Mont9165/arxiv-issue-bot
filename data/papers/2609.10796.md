# DR-LabStack: Design and Implementation of a Clinician-Facing Web System for Diabetic Retinopathy Prediction

- arXiv ID: `2609.10796v1`
- Authors: Yingfan Xu, Tieming Liu, Ye Liang
- Published: 2026-09-09
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.10796v1) | [pdf](https://arxiv.org/pdf/2609.10796v1)

## Abstract

Pretrained diabetic retinopathy (DR) prediction models differ in their input fields, serialization formats, preprocessing requirements, and output semantics. Making these models accessible through a common clinical interface therefore requires explicit coordination between the user interface and the inference service. We designed and implemented DR-LabStack, a React-Flask web system integrating four externally developed pretrained models: RuleFit, Pruned RuleFit, Elaborative XGBoost, and Two-level Ensemble. A shared form retrieves ordered model features, renders model-specific numerical and categorical controls, and constructs a positional input vector. Backend adapters load heterogeneous artifacts and apply the ensemble's accompanying scaler, while a common JSON response supports binary classification display alongside method and source information. Functional evaluation on September 8, 2026 used copied application files and real model artifacts in a documented isolated environment. All four models loaded and exposed their 14-, 6-, 8-, and 25-field contracts. Sixty-two Flask test-client requests characterized service behavior; 12 limited-vector checks confirmed invocation-path and threshold consistency. Twenty-four browser-component scenarios with mocked transport verified input ordering and result rendering and characterized input-validation behavior. The resulting system demonstrates a reusable interaction and serving workflow for heterogeneous DR models. The contribution is web-system design, integration, and software functionality; clinical effectiveness and clinician usability require separate evaluation.

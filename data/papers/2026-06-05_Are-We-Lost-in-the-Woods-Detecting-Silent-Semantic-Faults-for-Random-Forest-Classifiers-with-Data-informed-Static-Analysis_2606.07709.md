# Are We Lost in the Woods? Detecting Silent Semantic Faults for Random Forest Classifiers with Data-informed Static Analysis

- arXiv ID: `2606.07709v1`
- Authors: Willem Meijer, Louis Ohl, Kristian Sandahl, Daniel Varro
- Published: 2026-06-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.07709v1) | [pdf](https://arxiv.org/pdf/2606.07709v1)

## Abstract

While machine learning (ML) software necessitates effective quality assurance, ML engineers still encounter silent semantic faults, such as imbalanced datasets, that degrade prediction performance without apparent symptoms. These faults are typically detected after expensive training cycles, causing significant resource waste. We propose a data-informed static analysis technique to detect silent semantic faults in ML scripts that use the popular random forest classifier. Our approach extracts ML pipelines into directed acyclic graphs and evaluates them against formalized API contracts to detect structural, data, and hyperparameter faults. Our analysis uses aggregated data properties, enabling fault detection even when datasets are inaccessible due to confidentiality restrictions. We implemented this technique in an open-source tool, dille, and evaluated it on real-world Kaggle notebooks that use the random forest classifier. Our results demonstrate that the tool identifies relevant semantic faults with 91% precision and sub-second runtime overhead, making it suitable for integration into integrated development environments, agentic workflows, and continuous integration pipelines. Our empirical study reveals that 12% to 18% of existing ML notebooks that use the random forest classifier are affected by silent semantic faults, highlighting the immediate practical utility of data-informed static analysis in reducing the burden of ML debugging.

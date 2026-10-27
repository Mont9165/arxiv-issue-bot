# ComBeautify: Leveraging Code Change Summaries for Conventional Commit Generation

- arXiv ID: `2610.34374v1`
- Authors: Rishi Raj, Aashray Tandon, Nikolay Matyunin, Jibesh Patra
- Published: 2026-10-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.34374v1) | [pdf](https://arxiv.org/pdf/2610.34374v1)

## Abstract

Modern software development relies on version control systems such as Git to track changes and facilitate collaboration. While commit messages are crucial for conveying developer intent, they do not affect program functionality; as a result, developers often lack motivation to write meaningful ones. The Conventional Commits Specification (CCS) addresses this with a structured format and guidelines that help developers express the intent of a change, improving clarity and enabling automation. Yet, developers frequently struggle to express intent while adhering to the format. In particular, they may misclassify commits due to the large number of possible categories or the lack of project-specific guidance. We introduce ComBeautify, an approach that automatically generates CCS-compliant commit messages. Our hybrid approach leverages context-preserving summarization of Git diffs with large language models (LLMs) to improve commit classification accuracy under CCS. Rather than relying on manually curated category definitions, we learn them from historical commits. We also propose a method for automatically generating the CCS description component.
  Our empirical evaluation across 13 languages, 6,500 open-source repositories, and over 20 million commits provides long-term insights into CCS adoption, revealing increasing compliance. Our evaluation on twenty popular repositories reveals the limitations of approaches guided by generic category definitions, and shows that ComBeautify, when trained on project-specific data, outperforms baselines by up to 3x. Additionally, using a dataset of 2,000 manually curated commits, we validate our summarization approach, achieving up to 95.25% accuracy and surpassing baselines. These findings emphasize the need for adaptable, context-aware AI methods for commit classification and CCS-compliant commit message generation.

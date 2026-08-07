# A comparative analysis of automated techniques for security bug report identification

- arXiv ID: `2607.27893v1`
- Authors: Muhammad Laiq
- Published: 2026-07-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.27893v1) | [pdf](https://arxiv.org/pdf/2607.27893v1)

## Abstract

Timely identification of security-related bug reports is essential to minimize the window of vulnerabilities in software systems. Manually screening incoming bug reports to identify security-related issues is time-consuming, error-prone, and non-scalable for large-scale software systems. Thus, a variety of automatic techniques, including traditional machine learning (ML) techniques and large language models, have been proposed to facilitate this task. However, the literature remains fragmented. Most studies introduce or optimize a particular technique and evaluate it against a limited set of baselines, often under different experimental setups. As a result, it is difficult to compare their results and draw reliable conclusions about the effectiveness of existing approaches, leaving researchers and practitioners without clear guidance on which techniques are most suitable for the task.
  To address this gap, we conducted a comparative analysis of several promising automated techniques to identify security-related bug reports using benchmark datasets. We evaluated Logistic Regression, Support Vector Machines, Random Forest, OpenAI's GPT-5.2, BERT-base, RoBERTa, and SetFit (a state-of-the-art few-shot learning framework).
  Our results indicate that SetFit achieves the best overall performance, achieving an F1-score of 0.80 and outperforming other techniques on three of the four datasets. RoBERTa performs competitively and approaches SetFit in some projects, while traditional ML techniques, particularly Logistic Regression, remain a strong baseline in certain contexts. In contrast, GPT-5.2 performs poorly in both zero-shot and few-shot settings. In addition, cross-project experiments demonstrate that transfer learning can improve performance for projects with limited data, but may degrade results for projects with strong project-specific characteristics.

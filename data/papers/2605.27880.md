# Confident Learning-based Network for Detecting Bug-Inducing Commits on SZZ with Noisy Labels

- arXiv ID: `2605.27880v1`
- Authors: Weihao Sun, Qiyun Zhao
- Published: 2026-05-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.27880v1) | [pdf](https://arxiv.org/pdf/2605.27880v1)

## Abstract

The Just-In-Time (JIT) defect prediction model serves as a critical tool for ensuring the quality of software development and enhancing software performance. It assists development teams in promptly identifying and addressing potential issues by predicting whether code submissions may introduce defects. However, due to the existence of data noise and insufficient semantic connections in real-world scenarios, existing approaches face challenges in accurately identifying the code commits that introduce defects and capturing the potential semantic relationships. To address these challenges, we propose the BIC- Hunter(Bug-Inducing Commits Hunter) model, which mitigates data noise and improves semantic understanding, thereby enhancing the accuracy of bug-inducing commit identification. BIC - Hunter model consists of two components: a data denoising component and a semantic relationship capturing component. Specifically, the data denoising component addresses the challenges posed by inaccurate annotations and inconsistencies in real-world data, enhancing the reliability of training data and improving overall model robustness. The semantic relation- ship capturing component constructs homogeneous graphs and applies graph convolutional networks to facilitate a more comprehensive analysis of code context, enabling the identification of defects caused by code commits and enhancing the confidence in pinpointing their root causes. Experimental studies on a large-scale dataset integrated from three open-source datasets show that BIC- Hunter exhibits outstanding performance. BIC- Hunter outperforms the state-of-the-art by 6.16%, 7.13%, and 5.53% on Recall@1, Recall@2, and Recall@3, respectively, while the MFR index increases by 8.43% to 32.82%. These results demonstrate the superior capability of our method in identifying bug-inducing commits.

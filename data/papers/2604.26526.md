# Identifying and Characterizing Semantic Clones of Solidity Functions

- arXiv ID: `2604.26526v1`
- Authors: Ermanno Francesco Sannini, Francesco Salzano, Simone Scalabrino, Rocco Oliveto, Remo Pareschi, Corrado Aaron Visaggio, Andrea Di Sorbo
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.26526v1) | [pdf](https://arxiv.org/pdf/2604.26526v1)

## Abstract

Smart Contracts are essential blockchain components, mainly written in Solidity. The high availability of public Solidity code leads to frequent reuse and high clone ratios. Since cloning can propagate vulnerabilities and flaws, effective detection is crucial. Although existing techniques work well in detecting syntactic clones, the identification of semantic clones is an open problem. To address this challenge, in this paper, we present and empirically assess a scalable methodology, based on analyzing code and comments, to spot semantically equivalent Solidity functions. We first collected an up-to-date dataset of about 300,000 Ethereum smart contracts, 82.07% of which are compliant with modern Solidity version 0.8. Manual validation of a statistically significant sample comprising 1,155 function pairs confirms the effectiveness of our solution, achieving an overall precision of 59% (rising to 84% for homonymous functions) and a recall of 97%. Besides, we explore the structural differences occurring on semantically equivalent Solidity functions, demonstrating that they often represent design alternatives focused on security choices, modularization, and gas optimization. Finally, we investigate the use of Large Language Models (LLMs) as documentation engines in scenarios where code comments are poor or absent. Our results show that LLM-generated summaries, combined with sentence transformers like BERT, can bridge the documentation gap, enabling the identification of semantic clones in uncommented code with 75% precision. This work establishes a modern benchmark for Solidity clone detection and provides a foundation for the automated discovery of secure and efficient code alternatives.

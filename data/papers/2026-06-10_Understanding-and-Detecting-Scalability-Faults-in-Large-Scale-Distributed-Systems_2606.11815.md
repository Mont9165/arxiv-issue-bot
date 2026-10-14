# Understanding and Detecting Scalability Faults in Large-Scale Distributed Systems

- arXiv ID: `2606.11815v1`
- Authors: Hao-Nan Zhu, Goodness Ayinmode, Cesar A. Stuardo, Haryadi S. Gunawi, Cindy Rubio-González
- Published: 2026-06-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.11815v1) | [pdf](https://arxiv.org/pdf/2606.11815v1)

## Abstract

Scalable distributed systems form the backbone of modern computing infrastructure. However, as scale grows, system complexity may lead to scalability faults. Scalability faults are challenging to uncover and diagnose, as they are often latent and only manifest at large-scale deployment. In this paper, we present the first comprehensive study on scalability faults and propose an approach for their detection. First, we systematically investigate 444 scalability issue reports from 10 large-scale distributed systems to understand the common anti-patterns and root causes of scalability faults. We found that the majority of these faults are caused by the synergy between dimensional code fragments and anti-patterns associated with them. Second, based on our findings, we design and implement ScaleLens, a novel approach to detect scalability faults. ScaleLens combines dynamic and static analyses to pinpoint dimensional code fragments and match them with anti-patterns. Our evaluation shows that ScaleLens detects 4.2x more dimensional code fragments associated with known scalability faults compared to the baseline. On the latest stable versions of Cassandra, HDFS, and Ignite, ScaleLens detects 334 dimensional code fragments with confirmed problematic behavior.

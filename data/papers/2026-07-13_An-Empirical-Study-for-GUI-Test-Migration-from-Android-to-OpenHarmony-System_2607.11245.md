# An Empirical Study for GUI Test Migration from Android to OpenHarmony System

- arXiv ID: `2607.11245v1`
- Authors: Yakun Zhang, Xinjia Chen, Yiyun Chen, Yuxia Zhang, Mingyi Zhou, Xiang Gao, Shaokun Zhang, Li Li, Yunming Ye
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.11245v1) | [pdf](https://arxiv.org/pdf/2607.11245v1)

## Abstract

To reduce the substantial engineering effort required to test the corresponding applications from Android to OpenHarmony, migrating existing GUI test cases has become a critical problem. However, current research neither proposes solutions tailored for OpenHarmony nor provides a systematic evaluation of migration approaches on this system, leaving developers with limited empirical guidance in practice. In this paper, we present the first systematic empirical study of test migration from Android to OpenHarmony. Specifically, we first construct a dataset referred to as the ATH Benchmark, comprising 36 commercial applications with an average of over 9 billion downloads, along with 108 manually designed test cases. Second, we select two state-of-the-art test migration approaches (i.e., ReSPlay and ITeM) and adapt these two approaches to enable their execution on OpenHarmony. Third, we use the preceding infrastructure to evaluate these two approaches from three perspectives, including testing performance, root causes of failures, and the impact of OpenHarmony characteristics. Our results reveal that existing test migration approaches are less effective (15% success-rate on ReSPlay and 26% success-rate on ITeM) in Android-to-OpenHarmony scenarios. Through an in-depth analysis of failed cases, we identify that test performance is primarily hindered by OpenHarmony-specific characteristics, including technical architecture differences and unique ecosystem traits. Utilizing these findings, we propose an enhanced approach based on ITeM, referred as ITeM-HM, which incorporates specific OpenHarmony system features. As a result, ITeM-HM successfully achieves a 214% success-rate relative improvement over the original ITeM (from 26% to 81%).

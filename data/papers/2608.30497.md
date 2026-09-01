# Bridge: Automatically Mining Ecosystem-Scale API Update Mappings and Client Update Instances

- arXiv ID: `2608.30497v1`
- Authors: Kai Gao, Yu Sun, Chang-ai Sun
- Published: 2026-08-31
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.30497v1) | [pdf](https://arxiv.org/pdf/2608.30497v1)

## Abstract

Library updates often require adapting client code to API changes. API update mappings that identify relations between legacy and replacement APIs, version transitions that these mappings apply, and client update instances that capture concrete API call changes are essential for developing and evaluating automated library update techniques. Existing library evolution datasets capture only subsets of this information and typically cover few third-party libraries. In this paper, we present Bridge, a client-driven framework for automatically constructing ecosystem-scale library update datasets that connect API update mappings, version transitions, and client update instances. Bridge first mines candidate update instances from client dependency update commits at scale, validates them using library-side evidence, and then derives API update mappings from validated instances. This design grounds each retained mapping in at least one client update instance. On a manually annotated ground truth dataset, Bridge achieves 91.6% precision and 88.7% recall for Java and 90.1% precision and 64.0% recall for Python. Applied to WoC V3, Bridge mines 381,661 Java and 277,259 Python client update instances, representing 18,900 and 4,456 API update mappings across 2,557 and 999 libraries, respectively. The mined mappings exhibit a pronounced long-tail distribution, with most appearing in only a few client update instances. As one application of the dataset, we evaluate four large language models on replacement API recommendation, a key step in library updates. The best recommendation accuracy reaches only 37.1% for Java and 44.4% for Python, and all evaluated models perform substantially better on frequently observed mappings than on mappings observed in only a few client update instances, highlighting the difficulty current LLMs face in recommending replacements for mappings in the long tail.

# MADE: Belief-Driven Dual-Agent Coordination for Autonomous Model Deployment

- arXiv ID: `2608.01189v1`
- Authors: Yicheng Liu, Bolin Zhang, Weiran Liu, Yakun Zhang, Yangqin Jiang, Zhiying Tu, Dianhui Chu
- Published: 2026-08-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.01189v1) | [pdf](https://arxiv.org/pdf/2608.01189v1)

## Abstract

LLM-based agents now have strong general capabilities. However, they still struggle with domain-specific tasks, motivating the integration of external tools to broaden their capabilities. The open-source community offers a vast array of AI models typically released as heterogeneous research artifacts, whereas transforming them into ready-to-call APIs is costly and labor-intensive. Automated model deployment is therefore essential for bridging the gap between model resources and tool usability, yet it remains a long-horizon, multi-stage task that has not been sufficiently explored. To tackle this challenge, we introduce Model Automated Deployment Engine (MADE), a dual-agent coordination system. Specifically, given a model resource, MADE iteratively constructs and validates the deployment artifacts, updates its deployment belief based on execution feedback, and revisits invalid upstream artifacts until the model is successfully served as a ready-to-call API that can then be used by other agents. We further introduce M2ABench, a benchmark for the task of transforming Models to ready-to-call APIs. M2ABench comprises 122 real-world models with standardized test cases for evaluation. Experimental results demonstrate that MADE achieves a deployment success rate of 68.85%, outperforming SWE-agent and OpenHands by 13.93 and 44.26 percentage points, respectively. Our code and dataset are publicly available at https://github.com/HITDiSC/MADE.

# LLM-Assisted Model-Based GUI Testing for Vue.js Web Applications

- arXiv ID: `2606.27665v1`
- Authors: Tao Li, Chenhui Cui, Rubing Huang, Dave Towey, Shikai Guo, Lei Ma
- Published: 2026-06-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.27665v1) | [pdf](https://arxiv.org/pdf/2606.27665v1)

## Abstract

Vue.js is a popular framework for building modern web applications. As Vue.js functionality and tooling support grow, ensuring its reliability (through automated testing) is becoming increasingly important. Although model-based testing has been successfully used to automate graphical user interface (GUI) testing on other platforms, its application to Vue.js remains challenging: Transition candidates, which are spread across router configurations and single-file components (SFCs), must be concretized and normalized into an executable page transition graph (PTG) for testing. To address this, we propose the LLMVue framework, which uses a large language model (LLM) to generate a PTG from Vue.js source code. LLMVue infers component hierarchies and route transitions, merging them into a unified PTG across multiple SFCs. We evaluated LLMVue on a collection of ten open-source Vue.js projects from GitHub, using GPT-4o as the LLM backbone. The constructed graphs demonstrate high precision and recall, with low graph edit distance. LLMVue -guided testing also significantly improves the coverage and exploration efficiency, compared to a random exploration baseline (with the same time constraints). To the best of our knowledge, this is the first use of LLMs for model-based GUI testing of Vue.js applications using source-level PTG extraction.

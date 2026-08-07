# Can Large Language Models Assist the Comprehension of ROS2 Software Architectures?

- arXiv ID: `2604.21699v1`
- Authors: Laura Duits, Bouazza El Moutaouakil, Ivano Malavolta
- Published: 2026-04-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.21699v1) | [pdf](https://arxiv.org/pdf/2604.21699v1)

## Abstract

Context. The most used development framework for robotics software is ROS2. ROS2 architectures are highly complex, with thousands of components communicating in a decentralized fashion. Goal. We aim to evaluate how LLMs can assist in the comprehension of factual information about the architecture of ROS2 systems. Method. We conduct a controlled experiment where we administer 1,230 prompts to 9 LLMs containing architecturally-relevant questions about 3 ROS2 systems with incremental size. We provide a generic algorithm that systematically generates architecturally-relevant questions for a ROS2 system. Then, we (i) assess the accuracy of the answers of the LLMs against a ground truth established via running and monitoring the 3 ROS2 systems and (ii) qualitatively analyse the explanations provided by the LLMs. Results. Almost all questions are answered correctly across all LLMs (mean=98.22%). gemini-2.5-pro performs best (100% accuracy across all prompts and systems), followed by o3 (99.77%), and gemini-2.5-flash (99.72%); the least performing LLM is gpt-4.1 (95%). Only 300/1,230 prompts are incorrectly answered, of which 249 are about the most complex system. The coherence scores in LLM's explanations range from 0.394 for "service references" to 0.762 for "communication path". The mean perplexity varies significantly across models, with chatgpt-4o achieving the lowest score (19.6) and o4-mini the highest (103.6). Conclusions. There is great potential in the usage of LLMs to aid ROS2 developers in comprehending non-trivial aspects of the software architecture of their systems. Nevertheless, developers should be aware of the intrinsic limitations and different performances of the LLMs and take those into account when using them.

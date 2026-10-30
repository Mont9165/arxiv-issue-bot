# Unraveling the Efficacy of Neuron Coverage Criteria on Testing Large Language Models

- arXiv ID: `2610.40234v1`
- Authors: Xiaoning Ren, Jiayang Song, Chongyang Liu, Jie Li, Lei Ma, Yinxing Xue
- Published: 2026-10-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.40234v1) | [pdf](https://arxiv.org/pdf/2610.40234v1)

## Abstract

Neuron coverage criteria aim to assess test suite quality and guide test input generation, but their effectiveness for Transformer-based language models remains unclear. We evaluate six criteria, including four established and two recent criteria, across encoder-only, decoder-only, and encoder-decoder models. Our evaluation examines error-revealing capability, distribution diversity, sample fairness (category diversity), and guidance for test input generation. The results reveal uneven effectiveness. Erroneous samples provide only 0.32% additional coverage over noise samples, indicating limited sensitivity to adversarial errors. By contrast, coverage criteria effectively assess distribution diversity and sample fairness in 26 and 30 of 33 configurations, respectively. Incorporating neuron-wise coverage guidance into test input generation increases adversarial sample production by only 4.56%. These findings suggest that existing coverage criteria can serve as an antidote for assessing diversity but remain largely a placebo for revealing adversarial errors, particularly when used individually. Their practical value therefore depends on whether these limited benefits justify the computational overhead of testing large Transformer-based models. Our study highlights the need for more robust and efficient coverage criteria tailored to these models, with stronger error-revealing capability and greater value for test generation.

# The Hidden Environmental Cost of Poor Coding Practices in TensorFlow and Keras Applications: A Study on Resource Leaks and Carbon Emissions

- arXiv ID: `2606.19799v1`
- Authors: Bashar Abdallah, Gustavo Santos, Rola Al Bataineh, Alain Abran, Mohammad Hamdaqa
- Published: 2026-06-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.19799v1) | [pdf](https://arxiv.org/pdf/2606.19799v1)

## Abstract

Efficiency and sustainability are critical considerations in the development and deployment of machine learning (ML) applications. Among the factors influencing sustainability, resource leaks in ML code can introduce hidden inefficiencies that elevate energy consumption and CO2 emissions. Despite this, empirical evidence quantifying their environmental impact remains limited. This emerging results paper presents an initial empirical investigation of two common resource-leak smells, namely Improper Model Reuse (IMR) and Unreleased Tensor References (UTR), and their impact on energy consumption and CO2 emissions in TensorFlow and Keras workloads. Controlled experiments were conducted for each smell by executing identical training tasks while comparing against a smell-free baseline. Our preliminary results show that both smells consistently increase estimated electricity usage and carbon emissions. IMR and UTR increased electricity consumption by approximately 32% and 46%, respectively, with proportional increases in CO2 emissions. Paired statistical tests indicate that these differences are systematic and statistically significant, providing initial empirical evidence that resource-leak smells may degrade ML energy efficiency and environmental sustainability. These findings suggest that resource-leak smells pose measurable risks to both software quality and sustainability, emphasizing the importance of integrating resource-lifecycle management and energy-efficiency considerations into ML development.

# Is Model Instability just Noise to be Tolerated or a Property that can be Managed?

- arXiv ID: `2607.10420v1`
- Authors: Amirali Rayegan, Lunxiao Li, Tim Menzies
- Published: 2026-07-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.10420v1) | [pdf](https://arxiv.org/pdf/2607.10420v1)

## Abstract

In software analytics, rerunning the same analysis twice often yields different models and conclusions. This reduces trust in the model and limits its use. We find that model instability is a major problem. Across 127 multi-objective SE optimization problems (12,700 test cases), repeated runs of a state-of-the-art optimizer agree on only 13.7% of test cases, even under improved settings. We argue that this instability is not merely noise to tolerate, but a property that can be measured and managed. By adjusting how labels are spent, how complex the models become, and how splits are scored, we obtain models that agree 4.8 times as often as the default configuration. The standard deviation of optimization error falls by 22% on average (mean std 17.4 to 13.6), while recommendation quality improves rather than degrades. In terms of quality, the refined settings are statistically top-ranked on 119 of 127 datasets, compared to 74 for the defaults. We then test causal and data-locality interventions and find that they help only partially, suggesting a residual stability floor. Our evidence suggests there are fundamental limits to stability set by the data itself (noise, scarce labels, proxy objectives, and the many near-equivalent models a dataset admits). We conclude that instability should be treated as a standard evaluation axis in SE optimization, which should be routinely measured, reported alongside performance, and used to calibrate trust in any single run. The methods in this paper provide a baseline against which future efforts to reduce SBSE instability can be judged.
  To support open science, we offer the following reproduction package: https://tinyurl.com/Model-Instability

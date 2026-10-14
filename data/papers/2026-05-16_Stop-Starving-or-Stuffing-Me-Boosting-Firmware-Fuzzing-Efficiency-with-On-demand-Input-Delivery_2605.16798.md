# Stop Starving or Stuffing Me: Boosting Firmware Fuzzing Efficiency with On-demand Input Delivery

- arXiv ID: `2605.16798v1`
- Authors: Shandian Shen, Wei Zhou, Keming Zhao, Peng Liu, Chung Hwan Kim, Le Guan
- Published: 2026-05-16
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.16798v1) | [pdf](https://arxiv.org/pdf/2605.16798v1)

## Abstract

Firmware fuzzing has gained attention for identifying firmware bugs. However, current approaches often directly integrate fuzzing tools for general software. General software receives input as it encounters I/O functions, but firmware input can be received asynchronously and independently of the firmware's execution, with uncertain timing and quantity. Without full awareness of firmware's exceptions, existing solutions often imprudently deliver fuzzer-generated input to the firmware in an ad-hoc way. This either overwhelms the processing function of the firmware (stuffing) or fails to deliver enough input data to trigger input processing functions (starving). In both cases, fuzzing capability is weakened.
  In this paper, we comprehensively investigate the input delivery issue. To determine the optimal timing and quantity for delivering test cases, we leverage the fact that firmware has to check input availability before using data. So we employ static and dynamic analysis to map each input processing route into three stages: input retrieval, availability check, and processing. This recovered semantic information allows the fuzzer to accurately deliver input at the availability check points within the expected length range. For multiple input routes problem, we also optimize the scheduling algorithm to reach more diverse routes. Our prototype, named FIDO, can serve as an add-on to existing firmware fuzzers to enhance their test-case delivery effectiveness. Compared to ad-hoc input delivery methods used in Fuzzware and MULTIFUZZ, FIDO increases their median code coverage by up to 115% and 54%, respectively. Compared to SEmu, which requires humans to manually specify input delivery points, FIDO still improves its coverage by up to 19%. As a result, FIDO discovers known bugs significantly faster and also identifies five previously unknown bugs.

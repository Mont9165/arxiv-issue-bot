# PuzzleMark: Implicit Jigsaw Learning for Robust Code Dataset Watermarking in Neural Code Completion Models

- arXiv ID: `2604.27677v1`
- Authors: Haocheng Huang, Yuchen Chen, Weisong Sun, Peizhuo Lv, Yuan Xiao, Chunrong Fang, Yang Liu, Xiaofang Zhang
- Published: 2026-04-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.27677v1) | [pdf](https://arxiv.org/pdf/2604.27677v1)

## Abstract

Constructing and curating high-quality code datasets requires significant resources, making them valuable intellectual property. Unfortunately, these datasets currently face severe risks of unauthorized use. Although digital watermarking offers a post hoc mechanism for copyright authentication, existing methods are predominantly based on the co-occurrence pattern, which is not robust and is susceptible to watermark detection and removal attacks. In this paper, we propose PuzzleMark, a robust watermarking method for code datasets. To reduce the risk of watermark exposure, PuzzleMark introduces a carrier selection strategy that leverages code complexity to evaluate the suitability of code snippets as watermark carriers, and selects those with high suitability for watermarking. To enhance the robustness of the watermark, PuzzleMark proposes a novel concatenation pattern to replace the traditional co-occurrence pattern, and implements two watermarking strategies through variable name concatenation. PuzzleMark adaptively embeds watermarks based on the inherent characteristics of the code, making it more stealthy while maintaining design simplicity. For watermark verification, PuzzleMark employs Fisher's exact test to verify suspicious models under a black-box setting. Experimental results demonstrate that PuzzleMark achieves a 100% verification success rate and a 0% false positive rate, with negligible impact on model performance. Both our human study and our evaluation using four state-of-the-art watermark detection methods show that PuzzleMark exhibits strong imperceptibility, with an average suspicious rate $\leq$ 0.24 and an average recall $\leq$ 30.41%, respectively. As a practical digital watermarking method, PuzzleMark provides strong protection for the intellectual property of code datasets and offers new insights for future research.

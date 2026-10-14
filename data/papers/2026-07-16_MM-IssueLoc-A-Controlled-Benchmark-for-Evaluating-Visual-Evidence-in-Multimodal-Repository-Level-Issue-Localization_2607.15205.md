# MM-IssueLoc: A Controlled Benchmark for Evaluating Visual Evidence in Multimodal Repository-Level Issue Localization

- arXiv ID: `2607.15205v1`
- Authors: Shaoxiong Zhan, Shi Hu, Boyu Feng, Hai Lin, Andrew Gong, Zhengda Zhou, Jiaying Zhou, Yunyun Hou, Hao Su, Hai-Tao Zheng
- Published: 2026-07-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.15205v1) | [pdf](https://arxiv.org/pdf/2607.15205v1)

## Abstract

Real repository issues routinely include visual evidence such as screenshots, error dialogs, rendered UI states, and logs, yet repository-level issue localization is evaluated mostly as a text-only task. Existing multimodal SE benchmarks evaluate end-to-end repair, entangling localization with patch synthesis and obscuring whether visual input helped, hurt, or was ignored. We introduce \textbf{MM-IssueLoc}, a controlled benchmark and evaluation protocol for repository-level localization with visual evidence. MM-IssueLoc contains 652 issue-PR instances across 23 languages, with annotations for 7 image categories and 4 relevance levels. It provides file-level and function-level gold labels, paired text-only and with-image evaluation, and VCE-based diagnostics that convert images into structured textual evidence. We evaluate LLM-based and retrieval-based systems, including MM-IssueLoc-VL-Emb as a controlled multimodal retriever. Results show that existing systems remain far from reliable multimodal repository localization: the strongest agent reaches 38.96 file Acc@5 and 22.45 function Acc@10, while the strongest retriever reaches 33.86 function Acc@10. Cross-benchmark comparisons show that high localization scores on text-dominant SWE benchmarks do not transfer cleanly to multimodal issue localization. MM-IssueLoc turns visual evidence into an explicit evaluation variable, enabling future work to test whether systems improve by using visual evidence for localization, rather than by relying on text-only cues or downstream patch-generation effects.

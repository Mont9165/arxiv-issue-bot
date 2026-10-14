# KQFuzz: Knowledge-Guided Fuzzing for Quantum Libraries via Large Language Models

- arXiv ID: `2607.25647v1`
- Authors: Fuyuan Xia, Qixin Zhang, Chenhao Ying, Haojin Zhu, Shuai Wang, Yuan Luo, Pingchuan Ma, Yuxuan Du
- Published: 2026-07-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.MA`, `quant-ph`
- Links: [abs](http://arxiv.org/abs/2607.25647v1) | [pdf](https://arxiv.org/pdf/2607.25647v1)

## Abstract

As quantum computing continually improves, ensuring the reliability and correctness of quantum libraries has become increasingly critical. To this end, many LLM-based fuzzing approaches towards quantum libraries have been proposed to uncover potential bugs. However, these methods still suffer from limitations such as insufficient flexibility and low efficiency, which hinder the progress of the quantum computing field. To address these challenges, we propose KQFuzz, a novel knowledge-guided fuzzer for quantum libraries. It leverages comprehensive codebase knowledge to ground LLM-based test generation, synergizing this with fitness-guided evaluation and two-level mutations to explore complex execution paths and trigger potential bugs. Firstly, KQFuzz introduces a novel prompting scheme tailored to quantum programs, which strategically incorporates knowledge of the codebase to efficiently generate high-quality quantum seed programs. Moreover, we develop evaluation and mutation strategies to handle the generated seed programs, facilitating efficient fuzzing execution while further enriching the diversity of the resulting test cases. We implement KQFuzz and conduct fuzzing on three popular quantum libraries, including Qiskit, PennyLane, and Cirq. Experimental results demonstrate that our approach significantly outperforms other state-of-the-art methods, with coverage improved by up to 18.44%. During the development of KQFuzz, we discovered 13 bugs, all of which have been confirmed and 12 have already been fixed by the developers.

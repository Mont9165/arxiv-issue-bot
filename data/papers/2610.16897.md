# DeepGroundRepair: From API-Grounded Generation to Shape-Aware Repair for Deep Learning Programs

- arXiv ID: `2610.16897v1`
- Authors: Xiangyue Ma, Zhen Wang, Xuhui Lu, Xiaoting Du, Chenglong Li, Jun Li, Haotian Li, Zheng Zheng
- Published: 2026-10-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.16897v1) | [pdf](https://arxiv.org/pdf/2610.16897v1)

## Abstract

Deep learning programs are fundamental to modern AI applications, and automatically generating them from natural language requirements can substantially reduce DL development effort. Large language models have demonstrated promising capabilities for this direction. However, generated DL programs often remain unreliable because they must satisfy domain specific API usage constraints and tensor shape dependencies, violations of which can cause API level syntactic issues and runtime failures. Existing retrieval augmented generation and feedback guided code repair methods do not adequately address these DL specific constraints.
  In this paper, we propose DeepGroundRepair, a three stage framework that establishes a generation localization repair workflow to improve the reliability of LLM-generated DL programs. Its key idea is to progressively narrow the generation and repair spaces using DL specific knowledge and runtime tensor information. Specifically, it grounds generation in task-relevant API knowledge, localizes the upstream causes of tensor shape mismatch failures, and uses runtime tensor shapes to guide parameter repair.
  We evaluate DeepGroundRepair on the 100 model-level DL programming tasks in DeepEval using six open-weight LLMs across TensorFlow, PyTorch, and PaddlePaddle. We compare it with four baselines: two generation-only methods and their counterparts incorporating traceback guided self debugging. The results show that, relative to these baselines, DeepGroundRepair reduces the combined number of API-level syntactic issues by an average of 5.4 per 10 program files and achieves an average relative improvement of 85.3% in code executability. Compared with the two self debugging baselines, it improves semantic consistency by an average of 18.1% and reduces token cost by an average of 28.4%.

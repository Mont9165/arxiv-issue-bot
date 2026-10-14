# Kozuchi Agent: A Language-Agnostic Open-Weight Agent for Software Repair

- arXiv ID: `2608.15579v1`
- Authors: Mehdi Bahrami, Kosaku Kimura, Satoshi Munakata, Satoshi Nakashima, Yu Ishikawa, Kosuke Maeda, Nao Soma, Kenichi Kobayashi, Keisuke Miyazaki, Keizo Kato, Shigeki Fukuta, Tatsuo Kumano, Nobutaka Imamura, Kevin Musgrave, Shahbaz Abdul Khader, Kwun Ho Ngan, Joe Townsend, Fayas Asharindavida, Matthieu Parizy, Akira Sakai, Yuma Ichikawa, Yang Zhao, Michiaki Takizawa, Taku Fukui, Hiroki Ohtsuji, Wei-Peng Chen, Hiromichi Kobashi
- Published: 2026-08-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.ET`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2608.15579v1) | [pdf](https://arxiv.org/pdf/2608.15579v1)

## Abstract

Industrial software-engineering teams increasingly need LLM agents that turn bug reports into correct patches, yet benchmark-scale operation adds long horizons, tool-use discipline, context persistence, heterogeneous clusters, and evaluation reuse. We present Kozuchi Agent, a language-agnostic open-weight repair agent and CI-operated evaluation pipeline. Explicit phases, persistent state, deterministic tools, a model-independent action interface, and cross-agent test-time selection make runs auditable and repeatable. With locally hosted Qwen3.5-27B, no fine-tuning, and TTS@8, Kozuchi resolves 374/500 SWE-bench Verified instances on the official evaluator. Unchanged on Multi-SWE-bench Java, the same 27-billion-parameter agent resolves 41/128 instances (32.03%), ranking first among strict open-weight submissions and fourth of 42 overall; on Python it ranks 12th of 135 and first among open-weight systems. Per-phase behavior remains within +/-5 percentage points across languages. Remaining failures mainly reflect semantic correctness, Java-specific harness issues, and selection errors. Across both tracks, results compare favorably with open/local peers by parameter count. Analysis of candidate diversity, selector regret, and patch reliability shows that the remaining gap is primarily semantic correctness and selection rather than edit formatting or proprietary-model access. Operationally, reusable CI stages reduce operator touch-points from five to one across heterogeneous internal clusters.

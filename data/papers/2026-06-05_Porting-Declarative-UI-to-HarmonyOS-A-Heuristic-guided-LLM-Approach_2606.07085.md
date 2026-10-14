# Porting Declarative UI to HarmonyOS: A Heuristic-guided LLM Approach

- arXiv ID: `2606.07085v1`
- Authors: Kunwu Zheng, Pengyu Xue, Zhen Yang, Xiran Lyu, Peishi Lai, Mengying Zhao, Yutian Tang, Huizhi Zhang, Xianhang Li, Linhao Wu, Chengyi Wang
- Published: 2026-06-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.07085v1) | [pdf](https://arxiv.org/pdf/2606.07085v1)

## Abstract

As an emerging operating system, HarmonyOS has a significant demand for software migration from platforms such as Android and iOS, where the User Interface (UI) translation accounts for a critical link. However, the latest UI development has shifted to declarative paradigms, e.g., Kotlin Jetpack Compose (KJC) for Android, SwiftUI for iOS, and ArkUI for HarmonyOS, rendering prior translation approaches inapplicable, as they target either backend logic or legacy imperative UIs.
  As such, this paper targets ArkUI and proposes an automatic translation approach, namely ArkTrans, to port UI files from Android and iOS to HarmonyOS.
  ArkTrans overcomes two salient challenges during the translation: (1) Programming Language (PL) unfamiliarity, and (2) severe syntactic chaos. Towards the first challenge, ArkTrans heuristically constructs ArkUI skeletons by extracting metadata from source PL, thereby guiding LLMs' initial translation. As for the second challenge, ArkTrans executes empirically revealed post-fixing rules via pattern matching to repair most of the remaining syntactic errors. To examine the effectiveness of ArkTrans, we construct a 100-sample parallel UI page translation benchmark from KJC/SwiftUI to ArkUI at the file level. Extensive experiments demonstrate that LLMs with direct/one-shot prompting cannot translate a single compilable UI page. In contrast, at most 90.67\% ArkTrans-translated files can be successfully compiled with high visual fidelity.

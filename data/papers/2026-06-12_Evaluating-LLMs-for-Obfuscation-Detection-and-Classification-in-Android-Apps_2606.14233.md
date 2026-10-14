# Evaluating LLMs for Obfuscation Detection and Classification in Android Apps

- arXiv ID: `2606.14233v1`
- Authors: Luca Ferrari, Marco Alecci, Jordan Samhi, Tegawende' F. Bissyande', Jacques Klein, Mariano Ceccato, Luca Verderame
- Published: 2026-06-12
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2606.14233v1) | [pdf](https://arxiv.org/pdf/2606.14233v1)

## Abstract

Android applications (apps) developers increasingly rely on code obfuscation techniques to hinder reverse engineering and protect intellectual property. However, obfuscation also reduces the effectiveness of static analysis and vulnerability detection tools, creating challenges for Android security analysis. Existing approaches for detecting obfuscation in Android apps predominantly rely on handcrafted heuristics, engineered features, or task-specific learning pipelines, which may struggle to generalize across evolving obfuscation strategies.
  This paper presents a large-scale empirical study investigating the capability of Large Language Models (LLMs) to detect obfuscation in Android apps through semantic reasoning. Our study evaluates whether off-the-shelf LLMs can identify obfuscated code without relying on handcrafted rules, predefined signatures, or dedicated model training. The empirical evaluation is conducted on both a controlled benchmark containing an app obfuscated with multiple techniques and a real-world dataset of Android apps collected from Google Play. The study further examines the impact of prompt design, model selection, and decision thresholds across several open-weight and proprietary LLMs. Finally, the analysis compares LLM-based reasoning with existing SAST-based obfuscation-detection approaches and discusses the broader implications and limitations of applying LLMs to Android security analysis.

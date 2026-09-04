# Can LLMs Extract Architectural Design Decisions from Source Code Commits? - A Preliminary Exploratory Study

- arXiv ID: `2609.03721v1`
- Authors: Amey Karan, Rudra Dhar, Mohamed Soliman, Karthik Vaidhyanathan
- Published: 2026-09-03
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.03721v1) | [pdf](https://arxiv.org/pdf/2609.03721v1)

## Abstract

Context: Architectural Design Decisions (ADDs) capture the rationale behind the structure and evolution of software systems but are rarely documented explicitly, and are often hidden inside source code commits. Recovering them is important for Architectural Knowledge Management (AKM). Problem: Extracting ADDs from commits is challenging due to their implicit and unstructured nature. Large Language Models (LLMs) have shown strong capabilities in understanding code and text, yet their effectiveness for this task remains underexplored. Study: We present a preliminary study using four LLMs (Gemini 3 Pro, DeepSeek R1, Kimi K2, Qwen3) with zeroshot and fewshot prompting on 30 developer-written ADDs from open-source projects. We score outputs with ROUGE-L, BLEU, METEOR, and BERTScore, and one author manually reviews the Gemini outputs. Results: All models reach a BERT-F1 above 0.81, and fewshot prompting improves alignment (Gemini BERT-F1: 0.828 to 0.847). However, the generated ADDs are often too long, implementation-focused, and miss the rationale behind the decision. This highlights opportunities for architecture-aware LLM systems and automated AKM.

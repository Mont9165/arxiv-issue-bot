# Will AI mess my RTL? A snapshot-based approach to verifying AI-written RTL

- arXiv ID: `2611.12712v1`
- Authors: Bernat Homs, Oscar Palomar, Miquel Moreto, Marcelo Orenes-Vera
- Published: 2026-11-09
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AR`
- Links: [abs](http://arxiv.org/abs/2611.12712v1) | [pdf](https://arxiv.org/pdf/2611.12712v1)

## Abstract

With the growing interest in using AI (Artificial Intelligence) for RTL (Register-Transfer Level) hardware development, robust and comprehensive verification has become more important than ever. As Large Language Models (LLMs) increasingly assist in creating and modifying RTL designs, ensuring that these changes preserve existing functionality is paramount for building trust in AI-driven workflows. We present SVApshot, a fully automated framework that leverages LLMs to generate and systematically attempt to correct SystemVerilog Assertions (SVA) for RTL modules, completely removing the human from the generation loop. SVApshot introduces a novel snapshot methodology that captures the current functionality of a design as a comprehensive set of formal assertions, creating a regression suite for validating future changes--whether made by humans or AI. The framework features automated duplicate detection, assertion set expansion, and iterative repair of failing assertions using LLM-guided debugging with formal verification feedback. Our experimental evaluation across diverse RTL modules demonstrates high coverage for complex modules, with successful detection of both manually-injected and AI-introduced bugs. Additionally, this framework opens the door for automatic generation of formal testbenches to benchmark LLMs for hardware design, moving beyond binary pass/fail metrics towards nuanced assertion-based scoring.

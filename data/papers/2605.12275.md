# Minimalistic Terminal Editor for Julia Programming -- MinTEJ: A Friendly Approach for a Scientific Programmer

- arXiv ID: `2605.12275v1`
- Authors: Poornachandratejasvi Laxman Bhattar, Payal V. Dahiwale, Krishnarjunulu Thota, Anurag Sharma
- Published: 2026-05-12
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2605.12275v1) | [pdf](https://arxiv.org/pdf/2605.12275v1)

## Abstract

Developers rely on lightweight, terminal-centric workflows for rapid code iteration. However, within a unified environment for Julia programming language, existing tools provide limited support for integrated workflow such as editing, execution, file management, and debugging. As a result, developers frequently incur context-switching overhead and fragmented tool interactions. Therefore, the proposed work predominantly focuses on the minimalistic approach for developing native terminal editor for Julia programming language. This paper introduces MinTEJ, a terminal-based editor built in Julia, and proposes a Sequential Modal Interaction Architecture (SMIA) that unifies file management, code editing, execution, and debugging through a command-oriented workflow. The presented work formalizes model interaction and reduces cognitive load & errors while transitioning among different modes. In SMIA, buffer is the central data structure that persists across all modes. Each mode interprets and manipulates the buffer according to mode-specific rules. The central controller mediates access to the buffer and enforces sequential transitions between modes. To evaluate the approach, the performance benchmarking of MinTEJ is compared against existing tools i.e., VS code and Notepad++. The effectiveness of the proposed MinTEJ is evaluated based on memory consumption and CPU utilization demonstrating that it has less resource overhead. Findings suggest that integrated terminal-based editor environment is a practical lightweight software tool enabling efficient iterative development.

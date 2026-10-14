# Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis

- arXiv ID: `2606.25863v1`
- Authors: Felipe de Sant'Anna Paixão, Joanna C. S. Santos, Paulo Anselmo da Mota Silveira Neto, Daniel Sadoc Menasche, Gustavo Bittencourt Figueiredo, Eduardo Santana de Almeida
- Published: 2026-06-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2606.25863v1) | [pdf](https://arxiv.org/pdf/2606.25863v1)

## Abstract

We study how security patches in highly configurable C/C++ systems map onto the space of compile-time variants. We formalize the Vulnerability Impact Condition (VIC) - a Boolean predicate over configuration options that denotes all variants that contained the original flaw - and introduce PatchLens, a purely static technique that recovers VICs by aligning AST-level patch hunks with source-level presence conditions and resolving file inclusion via lightweight build system analysis. Evaluating PatchLens on 1,192 Linux kernel, 289 FFmpeg, and 100 PHP patches, we compute precise, human-readable VICs without the need to compile any system variant. The resulting predicates are compact (avg. 1.84 variables for Linux, 3.23 for FFmpeg, 1.04 for PHP) and show that only a small fraction of vulnerabilities are system-wide, which carry higher CVSS scores; meanwhile, CVE texts almost never encode the required options ($\approx$ 1% average recall), motivating automated enrichment of CVE descriptions with VICs. PatchLens and the accompanying dataset enable immediate applications in CI (variant-aware triage and test selection), targeted sampling and fuzzing, and feature risk scoring, offering a scalable, explainable path to vulnerability assessment in highly configurable software.

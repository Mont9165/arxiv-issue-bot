# Mostly Automatic Translation of Language Interpreters from C to Safe Rust

- arXiv ID: `2606.27122v1`
- Authors: Bo Wang, Brandon Paulsen, Joey Dodds, Daniel Kroening, Umang Mathur, Prateek Saxena
- Published: 2026-06-25
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.27122v1) | [pdf](https://arxiv.org/pdf/2606.27122v1)

## Abstract

Translating C programs to safe Rust is challenging owing to significant differences in typing constraints, ownership, and borrowing rules. Interpreter programs are particularly important targets for such translation, as they often handle untrusted inputs and suffer from memory-related vulnerabilities. We present Reboot, a mostly-automatic technique that translates real-world interpreter programs from C to safe Rust. Using Reboot, we have translated six interpreters ranging from 6k to 23k lines of C code to safe Rust, with each translation requiring only 1 to 11 brief user interventions. All translations pass 100% of the provided test suites, and achieve 62%--92% pass rates on separately created validation tests that were never exposed to the system. A security case study on mujs shows that memory vulnerabilities such as heap buffer overflows and use-after-free present in C are eliminated in the safe Rust translation. Two ideas underpin Reboot. First, feature reduction decomposes the translation by program features, creating a sequence of milestones where each is a complete, testable program; the translation starts from the simplest version and incrementally restores features, with each milestone validated before proceeding. Second, a multi-agent architecture orchestrates inherently unreliable coding agents through automated validation and feedback, keeping long-running translation workflows on track with minimal human involvement. An ablation study confirms that feature reduction improves translation correctness compared to using multi-agent translation alone, with 6%--20% improvements in pass rates on validation test suites.

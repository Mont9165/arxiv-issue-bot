# Documentation-Guided Agentic Codebase Migration from C to Rust

- arXiv ID: `2605.14634v1`
- Authors: Minh Le-Anh, Anh Nguyen Hoang, Bach Le, Nghi D. Q. Bui
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.14634v1) | [pdf](https://arxiv.org/pdf/2605.14634v1)

## Abstract

Migrating legacy C repositories to Rust promises stronger memory safety, but existing translators often work at the level of files or functions and miss architectural intent. We present RustPrint, a documentation-guided agentic framework for repository-level C-to-Rust migration. RustPrint first converts the source repository into architecture-aware documentation and treats it as a migration blueprint capturing module structure, data flow, APIs, and design rationale. Coding agents then use this blueprint to plan crates, implement modules, check compilability, reduce unsafe code, and iteratively refine the translated repository. RustPrint next compares documentation from the Rust output against the source documentation and uses mismatches as repair signals. It also translates and runs source test suites so runtime failures can guide targeted fixes. Experiments on eight real-world C repositories ranging from 11K to 84K LoC show that RustPrint compiles every target under both an open-weight (Kimi-K2-Instruct) and a closed-weight (GPT-5.4) backbone, while prior LLM-based translators (Self-Repair, EvoC2Rust) fail repository-wide. With the open-weight Kimi-K2-Instruct backbone, RustPrint exceeds an agentic Claude Code baseline on feature preservation (93.26% vs. 52.52%) and on cross-evaluation test pass rate (95.17% vs. 79.85%). These results suggest that documentation-guided coordination is a useful direction for scalable codebase migration.

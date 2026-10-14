# Metamorphic Testing of Transpilers via Mutation Consistency of Programs

- arXiv ID: `2607.29247v1`
- Authors: Enea Raffaele Ilario Papaleo, Luca Guglielmo, Giovanni Denaro
- Published: 2026-07-31
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.29247v1) | [pdf](https://arxiv.org/pdf/2607.29247v1)

## Abstract

Transpilers are increasingly used for software development, especially in industrial domains that rely on domain-specific languages (DSLs), to allow engineers to work with familiar concepts and appropriate abstractions. Ensuring the correctness of these instruments is therefore critical in many industrial settings. This paper observes that existing approaches for compiler testing hardly generalize to transpilers. Differential testing approaches are hindered as multiple equivalent implementations of the transpiler under test are seldom available in practice. The approaches based on metamorphic testing assume the ability to execute the compiled binaries, an assumption that cannot be always made for transpilers, which oftentimes produce results expressed as source code, requiring complex toolchains, hardware-in-the-loop setups, and depending on non trivial inputs. This paper introduces a novel metamorphic testing technique tailored to transpilers. Instead of reasoning about the runtime behavior of compiled programs, our approach defines metamorphic relations directly over the source code produced by the transpiler. These relations capture a property that we call mutation consistency of the (transpiled) programs: mutation-style changes in the input DSL program must induce predictable and structurally consistent changes in the generated output. We implemented this idea in a tool, MCP-Tester, and evaluated it through a case study conducted in the context of a technology-transfer project. Our current empirical results indicate that the proposed approach can effectively reveal faults that would remain undetected with pure fuzzing.

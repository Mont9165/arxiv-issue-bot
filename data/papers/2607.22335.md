# LinkML-Scala: a Robust, Fast, and Portable Implementation of LinkML

- arXiv ID: `2607.22335v1`
- Authors: Piotr Sowinski, Kacper Grzymkowski, Andriy Plokhotnyuk
- Published: 2026-07-24
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.22335v1) | [pdf](https://arxiv.org/pdf/2607.22335v1)

## Abstract

LinkML is a unified framework for data and domain modeling that spans diverse formats and ecosystems: JSON, RDF, CSV, SQL, spreadsheets and more. However, until now it had only one fully-featured implementation, written in Python, which is limited in terms of performance, portability, and behavior consistency. This restricts LinkML's usability in settings such as real-time schema editing and enterprise server applications. To address these issues, we present LinkML-Scala: a robust, fast, and portable implementation of LinkML that covers the metamodel, runtime support, schema derivation, and generators for JSON Schema, SHACL, RDFS, and Table Schema. Written in Scala 3, it runs in the browser (JavaScript transpilation), on the JVM, and as native binaries. LinkML-Scala is distributed as an in-browser playground, a CLI application, a GitHub CI Action, and JVM / JavaScript libraries. In our benchmarks, it outperforms the Python implementation in every tested scenario, on average by 22.9--38.5x. We consider LinkML-Scala an important contribution toward increasing LinkML's adoption and we outline a plan for further work to ensure implementation interoperability and stability.

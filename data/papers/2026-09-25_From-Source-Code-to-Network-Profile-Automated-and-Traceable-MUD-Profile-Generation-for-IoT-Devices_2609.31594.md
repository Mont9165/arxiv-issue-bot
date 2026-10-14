# From Source Code to Network Profile: Automated and Traceable MUD Profile Generation for IoT Devices

- arXiv ID: `2609.31594v1`
- Authors: Alessandro Lotto, Abdulla R. A. Almenhali, Savio Sciancalepore, Alessandro Brighente, Mauro Conti
- Published: 2026-09-25
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.31594v1) | [pdf](https://arxiv.org/pdf/2609.31594v1)

## Abstract

The Manufacturer Usage Description (MUD) standard allows IoT manufacturers to define expected network behaviors in a MUD file. This file can be translated into enforceable access-control policies, restricting compromised devices to operate solely through manufacturer-defined communication patterns. However, practical adoption of MUD depends on profiles that are accurate, complete, and maintainable. Existing approaches use traffic-based automation but require device deployment and prolonged monitoring, capturing only behavior exercised during observation. Rare, failure-triggered, or configuration-dependent communications may remain absent, producing incomplete policies that disrupt legitimate operation and offer limited insight into the software components responsible for each rule. We present AutoMUD, a source-code-driven tool that generates traceable MUD profiles for IoT devices from their firmware and software source code. AutoMUD combines static and syntactic extraction, retrieval-grounded language-model reasoning, and deterministic validation and compilation to recover the communication behavior characterizing an IoT device and translate eligible endpoints into policy rules. By analyzing code-level evidence, AutoMUD exposes rarely exercised and conditional communication paths, links every generated rule to its source-level provenance, and preserves excluded findings with explicit reasons for review. Our evaluation on a Linux-based repository demonstrates that AutoMUD recovers complete communication behavior, consolidates validated behavior into semantic endpoint groups, and generates structurally valid MUD profiles. Through a controlled semantic fault-injection campaign, we demonstrate that AutoMUD enables analysts to detect, localize, explain, and correct propagated errors, recovering policies semantically identical to their clean counterparts.

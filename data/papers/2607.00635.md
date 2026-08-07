# Checked Program Recovery from Execution Video: A Sound Oracle for Untrusted Generators

- arXiv ID: `2607.00635v1`
- Authors: Yuan Si, Jialu Zhang
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.00635v1) | [pdf](https://arxiv.org/pdf/2607.00635v1)

## Abstract

A growing class of tools recovers a program from observations of its behavior using an untrusted generator, a neural model or a search, that proposes candidates with no correctness guarantee. We study how to make such recovery trustworthy, in the concrete setting of recovering a runnable Scratch program from a recording of its execution. The recording shows what the program does but never its code; many programs produce the same video, so the source cannot be recovered, and the right target is a program that behaves the same as far as the camera can tell, made precise with a lens. The core is a two-tier validation oracle with a deliberate verdict asymmetry. A static checker proves lens-equivalence to a reference and issues a certificate that, granting the partial-order independence quotient adequate, never accepts a wrong program; a renderer can only refute or witness finite agreement, never certify. Around it, Vid2Prog reads each sprite's motion, visibility, and timing from the video and a known-asset manifest and synthesizes a candidate source-free; a closed loop renders and runs recovery again for ground truth. Under the exact lens the oracle makes no false accept on 246 labeled differing pairs, including an adversarial battery built to trap its concurrency quotient; on inputs outside the vocabulary and on real projects it abstains or refutes, accepting none we test. In-vocabulary recoveries reproduce their source frame for frame and 80% earn a static certificate, while whole real projects, mostly outside the vocabulary, recover at 14%, a vocabulary-bound rate the system never inflates with a wrong answer. A frontier vision-language model recovers none of the matched programs single-shot, which oracle-in-the-loop repair lifts only to a few while the structured pipeline recovers all, the gap a sound checker makes for an untrusted generator.

# BehaVerify: A Formal Verification Tool for Behavior Trees

- arXiv ID: `2611.22403v1`
- Authors: Serena S. Serbinowska, Ben Wooding, Diego Manzanas Lopez, Luke Nam, Anne M. Tumlin, Nicholas K. Potteiger, Hongchao Zhang, Taylor T. Johnson
- Published: 2026-11-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LO`, `cs.RO`
- Links: [abs](http://arxiv.org/abs/2611.22403v1) | [pdf](https://arxiv.org/pdf/2611.22403v1)

## Abstract

This paper presents BehaVerify, a verification toolbox for behavior trees (BTs) and Neuro-Symbolic BTs. BTs are a graphical language for planning and sequencing behaviors - similar to extended state machines - and are increasingly used in safety-critical domains. BehaVerify enables users to specify a BT using a Domain Specific Language (DSL) with formal syntax and semantics. This language further includes Linear Temporal Logic and Computation Tree Logic specifications. BehaVerify uses an efficient encoding into nuXmv, called fastforwarding, to quickly verify if a specification holds over the BT. Additionally, BehaVerify can generate implementations of the BT in Python and Haskell. Through Python, BehaVerify has been integrated with PyTrees and Robot Operating System (ROS) and has been deployed to several autonomous robotic systems, including for verifying runtime monitors. While prior works have developed the underlying theory, this manuscript focuses on the toolbox usage, functionality and implementation. BehaVerify is open source: https://github.com/verivital/behaverify

# Verifying the Rust Standard Library

- arXiv ID: `2606.17374v1`
- Authors: Byron Cook, Remi Delmas, Zyad Hassan, Bart Jacobs, Ranjit Jhala, Rahul Kumar, Felipe R. Monteiro, Thanh Nguyen, Rebecca Rumbul, Michael Tautschnig, Celina Val, Carolyn Zech
- Published: 2026-06-16
- Primary category: `cs.LO`
- Categories: `cs.LO`, `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.17374v1) | [pdf](https://arxiv.org/pdf/2606.17374v1)

## Abstract

Rust's type system prevents many classes of memory errors, yet its standard library relies heavily on unsafe code whose correctness is validated through testing, including dynamic checks under Miri, but lacks static verification. We present what is, to the best of our knowledge, the largest verification campaign reported for a software library: an open, crowdsourced effort that integrates complementary verification tools into the continuous integration of a verification repository forked from the Rust standard library. We analyze the campaign's effectiveness, discuss the practical value of machine-checked proofs for a subset of undefined behaviors (e.g., out-of-bounds access, null and dangling pointer dereferences, and use of uninitialized memory), and frame the remaining obstacles as open challenges for the formal-methods community.

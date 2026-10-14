# Progress in Benchmarking Generics for Mathematical Computation

- arXiv ID: `2607.26206v1`
- Authors: Daniel Pang, Stephen M. Watt
- Published: 2026-07-28
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.MS`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.26206v1) | [pdf](https://arxiv.org/pdf/2607.26206v1)

## Abstract

The original SciGMark benchmark adapted the SciMark numerical suite to measure the cost of generic programming in scientific computing. In the twenty years since, generics have become ordinary features of mainstream languages, but their implementation strategies have diversified. This paper reports SciGMark 1.5, a benchmark study of specialized and generic implementations in modern languages. The study has three aims. First, it examines the consequences of the wide variety of generic-realization strategies used in current widely used languages. Second, it extends the benchmark toward symbolic computation by adding finite-field linear algebra, finite-field FFT, and a naïve Gröbner basis computation. Third, it asks how the original floating-point scientific kernels behave in the new language settings. The measurements cover Rust, Java, Go, and TypeScript for the main suite, with additional C++ and Julia measurements for the Gröbner basis benchmark. The study also records representative output artifact sizes, since code generation and runtime packaging are part of the cost model of generic programming. The results confirm that the cost of generic programming is not inherent in abstraction itself, but depends strongly on when type information is resolved, how arithmetic values are represented, and whether the compiler or runtime can recover specific operations in the inner loops. Ahead-of-time monomorphization usually makes generic code close to specialized code in the numerical tests. Erased or objectbased generic arithmetic can introduce substantial overhead, especially in arithmetic- and allocation-intensive code. Runtime specialization occupies an intermediate position, offering flexibility and good steady-state performance when type inference and representation choices are favourable.

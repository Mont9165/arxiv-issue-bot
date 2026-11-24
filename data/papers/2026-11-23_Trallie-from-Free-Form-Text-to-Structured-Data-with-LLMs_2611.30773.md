# Trallie: from Free-Form Text to Structured Data with LLMs

- arXiv ID: `2611.30773v1`
- Authors: Vijayasri Iyer, Cristiano De Nobili, Mubashir Hussain Shah, Sébastien Bratières
- Published: 2026-11-23
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2611.30773v1) | [pdf](https://arxiv.org/pdf/2611.30773v1)

## Abstract

Trallie is an open-source framework that leverages large language models (LLMs) to perform information extraction (IE) from natural language sources with or without user guidance. Unlike conventional approaches that rely on extensive labeled datasets or domain-specific training, Trallie enables the conversion of unstructured data into structured formats with minimal or no representative examples. The framework is designed with three key objectives: (i) reducing manual annotation by harnessing prompt-based zero-shot and few-shot capabilities of modern LLMs, (ii) flexibly parsing diverse document formats (i.e., HTML, PDF, TXT, and JSON), and (iii) improving accessibility for non-expert users by automatically inducing schemas from document collections, which can then be refined for extraction. We evaluate Trallie with open-weight LLMs on FDA 510(k) documents and on movie and university websites from SWDE. It outperforms previously reported systems when the target attributes are provided for text extraction and is competitive when it must discover attributes for the schema automatically. The project is available at https://github.com/PiSchool/trallie

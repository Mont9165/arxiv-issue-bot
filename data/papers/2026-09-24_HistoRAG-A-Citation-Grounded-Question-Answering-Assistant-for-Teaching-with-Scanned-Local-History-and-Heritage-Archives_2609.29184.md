# HistoRAG: A Citation-Grounded Question Answering Assistant for Teaching with Scanned Local History and Heritage Archives

- arXiv ID: `2609.29184v1`
- Authors: Hongzhou Duan, Zikun Guo
- Published: 2026-09-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.29184v1) | [pdf](https://arxiv.org/pdf/2609.29184v1)

## Abstract

Teachers who prepare lessons on local history and cultural heritage work from material that is hard to use. The primary sources are scanned books without a text layer, and the supporting records are administrative catalogs released as spreadsheets. A general chatbot answers such questions fluently but without a verifiable source, which is the property a teacher needs most. This paper presents HistoRAG, a question answering assistant that answers from one regional collection and cites a volume and a page for every fact. HistoRAG transcribes each page with a vision language model and keeps a line level confidence from the token probabilities. It builds three stores from the same collection: a hybrid text index, a relational catalog database, and a knowledge graph extracted only from entity dense passages. A lightweight router sends each question to the stores it needs, so that counting questions reach the database and relational questions reach the graph. We build a benchmark of 516 questions over a collection of 36 scanned volumes and the heritage catalogs of the same region, covering statistical, factual, temporal, and multi-hop questions. HistoRAG answers more questions correctly than passage retrieval baselines and than a graph based retrieval system, at a far smaller cost per question. The assistant runs behind a chat interface, so a teacher can check any statement against the page it came from.

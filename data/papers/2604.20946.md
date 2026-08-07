# Common Foundations for Recursive Shape Languages

- arXiv ID: `2604.20946v1`
- Authors: Shqiponja Ahmetaj, Iovka Boneva, Jan Hidders, Maxime Jakubowski, Jose-Emilio Labra-Gayo, Wim Martens, Fabio Mogavero, Filip Murlak, Cem Okulmus, Ognjen Savković, Mantas Šimkus, Dominik Tomaszuk
- Published: 2026-04-22
- Primary category: `cs.LO`
- Categories: `cs.LO`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.20946v1) | [pdf](https://arxiv.org/pdf/2604.20946v1)

## Abstract

As schema languages for RDF data become more mature, we are seeing efforts to extend them with recursive semantics, applying diverse ideas from logic programming and description logics. While ShEx has an official recursive semantics based on greatest fixpoints (GFP), the discussion for SHACL is ongoing and seems to be converging towards least fixpoints (LFP). A practical study we perform shows that, indeed, ShEx validators implement GFP, whereas SHACL validators are more heterogeneous. This situation creates tension between ShEx and SHACL, as their semantic commitments appear to diverge, potentially undermining interoperability and predictability. We aim to clarify this design space by comparing the main semantic options in a principled yet accessible way, hoping to engage both theoreticians and practitioners, especially those involved in developing tools and standards. We present a unifying formal semantics that treats LFP, GFP, and supported model semantics (SMS), clarifying their relationships and highlighting a duality between LFP and GFP on stratified fragments. Next, we investigate to which extent the directions taken by SHACL and ShEx are compatible. We show that, although ShEx and SHACL seem to be going in different directions, they include large fragments with identical expressive power. Moreover, there is a strong correspondence between these fragments through the aforementioned principle of duality. Finally, we present a complete picture of the data and combined complexity of ShEx and SHACL validation under LFP, GFP, and SMS, showing that SMS comes at a higher computational cost under standard complexity-theoretic assumptions.

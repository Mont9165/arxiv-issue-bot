# From OA colors to observable access states: A commentary on the 2026 OpenAlex proposal

- arXiv ID: `2609.24730v1`
- Authors: Abdelghani Maddi
- Published: 2026-09-21
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.24730v1) | [pdf](https://arxiv.org/pdf/2609.24730v1)

## Abstract

The OpenAlex Colors Working Group proposes replacing the familiar Gold, Green, Hybrid, Bronze and Closed taxonomy with a work-level framework based on three dimensions: access, location and license. The proposal addresses genuine weaknesses in the legacy color system, particularly its dependence on journal-level characteristics, its difficulty in describing non-article outputs, and its conflation of access conditions with venue business models. This commentary supports that general direction but argues that the proposed labels should not become the primary data model. The central technical issue is that access, location and license are not best understood as three independent attributes of a work: scholarly works commonly have several versions or copies at different locations, and access status, license and version may differ from one location to another. The analysis therefore recommends treating the location/version observation as the atomic unit of OA metadata and deriving work-level labels, legacy colors and user-facing summaries from those observations. Particular attention is given to license semantics, version identification, the normative assumptions embedded in a ``best-available'' hierarchy, the coarse Publisher/Other Platform distinction, temporal change, provenance, compound works, and backward compatibility. Existing standards and infrastructure (including NISO/ALPSP Journal Article Versions, COAR controlled vocabularies, FAIR provenance principles, and OpenAlex's own current location objects) already provide many of the components needed for such an approach. The result would preserve the simplicity sought by the Working Group while making the underlying data model more extensible, auditable and suitable for funder compliance, bibliometric research and future changes in scholarly communication.

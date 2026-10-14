# Kale: A Transformation-Safe Spreadsheet System

- arXiv ID: `2608.26345v1`
- Authors: Michael Coblenz, Jacob Yim, Ajinkya Bokade, Mounika Padala, Julia Epshtein, Priyanka Bhatia, Piyush Chauhan, Simran Gill, Aniket Gupta, Grishma Gurbani, Vaibhav Khetan, Arushi Munjal, Jeffery Tung, Joanna Yang
- Published: 2026-08-26
- Primary category: `cs.HC`
- Categories: `cs.HC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.26345v1) | [pdf](https://arxiv.org/pdf/2608.26345v1)

## Abstract

Spreadsheet formulas can refer to rectangular ranges of arbitrary size. When a user changes the structure of a referenced table, the spreadsheet system updates the references to refer to a new range. Unfortunately, this new range may differ from the user's expectations, introducing bugs in spreadsheets. We describe a user study showing that standard reference semantics are error-prone, resulting in significant risk to users. We introduce Kale, a prototype system that eliminates the risk of inserting these kinds of bugs by restricting the kinds of references that can be expressed. We show that Kale can be used effectively by users to complete tasks that are error-prone in traditional spreadsheet systems. Finally, we describe a corpus study that evaluates the extent to which the reference restrictions in Kale might have implications on users.

(NED)
==========================
Definition
----------
NED also know as entity linking or entity resolution  is the task of linking mentions of entities in text to a given
knowledge base, such as Freebase or Wikipedia.

Proposed Approach 
-----------------
The proposed system accepts text as an input and text preprocessing is applied. The preprocessing includes, Part-Of-Speech tagging,
Named Entity Recognition,  ASCII folding filter(This filter converts alphabetic, numeric, and symbolic Unicode characters which are 
not in the Basic Latin Unicode block to their ASCII equivalents) and Shingle Token Filter (This token filter of type shingle that constructs shingles (token n-grams)
from a token stream. In other words, it creates combinations of tokens as a single token).   
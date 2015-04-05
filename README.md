BIBDCalc
========
A python library for BIBD-related (Balanced Incomplete Block Design) calculations.

Overview
--------
####BIBD definition:
Let V and B be sets and I &sube; V x B. A triplet (V, B, I) is a t - (v, k, &lambda;) design if the following holds:
* |V| = v.
* Every block b &isin; B is incident (in relation I) with exactly k vertices v &isin; V.
* Every t-subset T of V is incident with exactly &lambda; blocks b &isin; B.

####About this library:
This library provides routines for testing existence of BIBD-s with certain paramethers, 
as well as construction of some BIBD-s.

"""
This example shows construction of finite fields and vector spaces
with prime number of elements.
"""

import sys
sys.path.append("../")
from bibdcalc.utils import FVSpace
from bibdcalc.utils import FVSubSpace

if __name__ == "__main__":
    p = 3

    F = list(range(p))
    add_table = [[(x+y) % p for x in F] for y in F]
    mult_table = [[(x*y) % p for x in F] for y in F]

    v3 = FVSpace(add_table, mult_table, 3)
    print("Elements of Z_3^3:")
    print(set(v3.elements()))

    subspaces1d = set()
    subspaces2d = set()

    for a in v3.elements():
        for b in v3.elements():
            subspace = frozenset(FVSubSpace(v3, [a, b]).elements())
            if len(subspace) == p:
                subspaces1d.add(subspace)
            elif len(subspace) != 1:
                subspaces2d.add(subspace)

    print("1D subspaces [{}]:".format(len(subspaces1d)))
    for s in subspaces1d:
        print(s)

    print("2d subspaces [{}]:".format(len(subspaces2d)))
    for s in subspaces2d:
        print(s)

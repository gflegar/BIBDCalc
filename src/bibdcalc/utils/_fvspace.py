
import itertools as it
import functools as ft
import operator as op

class FVSpace(object):
    """A class representing finite vector space"""
    def __init__(self, add_table, mult_table, dim):
        self._add_table = add_table
        self._mult_table = mult_table
        self._fsize = len(add_table)
        self._dim = dim

    class Vector(object):
        def __init__(self, fvspace, elements):
            self._fvspace = fvspace
            self._elements = elements

        def __add__(self, other):
            add_table = self._fvspace._add_table
            elements = tuple(add_table[x][y] 
                             for x, y in zip(self._elements, other._elements))
            return FVSpace.Vector(self._fvspace, elements)

        def __rmul__(self, other):
            mult_table = self._fvspace._mult_table
            elements = tuple(mult_table[other][x] for x in self._elements)
            return FVSpace.Vector(self._fvspace, elements)

        def __repr__(self):
            return repr(self._elements)

        def __str__(self):
            return str(self._elements)

        def __hash__(self):
            return hash(self._elements)

        def __eq__(self, other):
            return self._elements == other._elements

    def elements(self):
        for elements in it.product(range(self._fsize), repeat=self._dim):
            yield FVSpace.Vector(self, elements)

    def __hash__(self):
        return hash(frozenset(self.elements()))

    def __eq__(self, other):
        return frozenset(self.elements()) == frozenset(other.elements())

    def __repr__(self):
        return repr(set(self.elements()))

    def _str__(self):
        return str(set(self.elements()))

class FVSubSpace(FVSpace):
    def __init__(self, fvspace, generators):
        super(FVSubSpace, self).__init__(
                fvspace._add_table, fvspace._mult_table, fvspace._dim)
        self._generators = generators

    def elements(self):
        for coefs in it.product(
                range(self._fsize), repeat=len(self._generators)):
            elements = ft.reduce(
                op.add, (c * v for c, v in zip(coefs, self._generators)))
            yield FVSpace.Vector(self, elements)


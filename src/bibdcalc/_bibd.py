
from . import _bibderrors
from . import _bibdparams
from . import utils

class BIBD(object):
    def __init__(self, blocks, bibd_params = None, t = None):
        self.blocks = blocks
        if bibd_params is None:
            bibd_params = BIBD.calculate_params(blocks, t)
        self.bibd_params = bibd_params

    @classmethod
    def calculate_params(cls, blocks, t):
        """TODO: implement this method"""
        pass

    @classmethod
    def create_projective_plane(cls, add_table, mult_table):
        n = len(add_table)
        f3 = utils.FVSpace(add_table, mult_table, 3)
        subspaces1d = set()
        subspaces2d = set()
        for a in f3.elements():
            for b in f3.elements():
                subspace = frozenset(utils.FVSubSpace(f3, [a, b]).elements())
                if len(subspace) == n:
                    subspaces1d.add(subspace)
                elif len(subspace) != 1:
                    subspaces2d.add(subspace)

        blocks = []
        for plane in subspaces2d:
            block = set()
            for index, line in enumerate(subspaces1d):
                if line <= plane:
                    block.add(index)
            blocks.append(block)

        return BIBD(blocks, _bibdparams.BIBDParams(2, n*n + n + 1, n + 1, 1))

    def get_incidency_matrix(self):
        matrix = []
        v = self.bibd_params.v
        for block in self.blocks:
            matrix_row = [0] * v
            for element in block:
                matrix_row[element] = 1
            matrix.append(''.join(str(x) for x in matrix_row))
        return matrix

    def __repr__(self):
        return repr(self.blocks)

    def __str__(self):
        return str(self.blocks)

    def remove_block(self):
        new_params = self.bibd_params.remove_block()
        first_block = self.blocks[0]
        new_blocks = []
        rename_counter = 0
        rename_map = {}
        for block in self.blocks[1:]:
            new_block = set()
            for vertex in block - first_block:
                if vertex not in rename_map:
                    rename_map[vertex] = rename_counter
                    rename_counter += 1
                new_block.add(rename_map[vertex])
            new_blocks.append(new_block)
        return BIBD(new_blocks, new_params)

    def complement(self):
        new_params = self.bibd_params.complement()
        vertices = set(range(self.bibd_params.v))
        new_blocks = [vertices - block for block in self.blocks]
        return BIBD(new_blocks, new_params)


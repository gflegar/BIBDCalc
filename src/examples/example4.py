"""
This example shows contruction of 2-(13, 4, 1) design.
"""

import sys
sys.path.append("../")
from bibdcalc import BIBD

if __name__ == "__main__":

    F = list(range(3))
    add_table = [[(x+y) % 3 for x in F] for y in F]
    mult_table = [[(x*y) % 3 for x in F] for y in F]

    design = BIBD.create_projective_plane(add_table, mult_table)

    print(design.bibd_params)
    for row in design.get_incidency_matrix():
        print(row)


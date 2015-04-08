"""
This example shows contruction of 2-(21, 5, 1) design.
"""

import sys
sys.path.append("../")
from bibdcalc import BIBD

add_table = [
    [0, 1, 2, 3],
    [1, 0, 3, 2],
    [2, 3, 0, 1],
    [3, 2, 1, 0]
]
mult_table = [
    [0, 0, 0, 0],
    [0, 1, 2, 3],
    [0, 2, 3, 1],
    [0, 3, 1, 2]
]

design = BIBD.create_projective_plane(add_table, mult_table)


if __name__ == "__main__":
    print(design.bibd_params)
    for row in design.get_incidency_matrix():
        print(row)


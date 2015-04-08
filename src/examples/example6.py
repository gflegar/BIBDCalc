"""
This example shows construction of some other designs from
2-(21. 5. 1) design contructed in example5.
"""

from example5 import *

#2-(16, 4, 1)
afine_plane = design.remove_block()

#2-(21, 16, 12)
d2 = design.complement()

#2-(16, 12, 11)
d3 = afine_plane.complement()

#2-(5, 4, 12)
d4 = d2.remove_block()

new_designs = [design, d2, afine_plane, d3, d4]

if __name__ == "__main__":
    for new_design in new_designs:
        print(new_design.bibd_params)
        for row in new_design.get_incidency_matrix():
            print(row)
        print("")


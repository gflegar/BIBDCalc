"""
This example finds diferent design parameters by applying various
operations on designs 5-(24, 8, 1) and 2-(27, 13, 6).
"""

import sys
sys.path.append("../")
from bibdcalc import BIBDParams
from bibdcalc import BIBDParamsError
from collections import deque

def findParameters(startingParams = None):
    if startingParams is None:
        startingParams = [BIBDParams(5, 24, 8, 1), BIBDParams(2, 27, 13, 6)]
    done = set(startingParams)
    frontier = deque((params, str(i+1))
                     for i, params in enumerate(startingParams))
    operations = [
            (BIBDParams.remove_block, 'b'),
            (BIBDParams.remove_vertex, 'v'),
            (BIBDParams.derive, 'd'),
            (BIBDParams.complement, 'c'),
            (BIBDParams.extend, 'e')
    ]

    while frontier:
        current, path = frontier.popleft()
        yield current, path
        for operation, code in operations:
            try:
                new = operation(current)
            except BIBDParamsError:
                continue
            if new.k < new.t or new.k >= new.v:
                continue
            if new not in done:
                done.add(new)
                frontier.append((new, path + code))

if __name__ == "__main__":
    for params, path in findParameters():
        print(params, path, sep="\t")



"""
This script tests validity of 2-(2015, k, lambda) designs for k > 2 with
diferent lambda.

Examples:

>>> from example1 import testValidity
>>> for params in testValidity(5):
...     print(params)
...
2-(2015,5,2)
2-(2015,20,2)
2-(2015,3,3)
2-(2015,39,3)
2-(2015,5,4)
2-(2015,20,4)

>>> len([p for p in testValidity(5)])
6


>>> len([p for p in testValidity(100)])
278

"""

import sys

sys.path.append("../")

from bibdcalc import BIBDParams

def testValidity(maxLambda = 2015):
    for lambda_ in range(1, maxLambda + 1):
        for k in range(3, 2015):
            p = BIBDParams(2, 2015, k, lambda_)
            if p.is_valid():
                yield p


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: {} maxLambda\n".format(sys.argv[0]))
        sys.exit(-1)
    counter = 0
    for params in testValidity(int(sys.argv[1])):
        if params.is_valid():
            print(params, end='\t' if counter != 3 else '\n')
            counter = (counter + 1) % 4


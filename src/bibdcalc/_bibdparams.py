
from . import _bibderrors
import math

class BIBDParams(object):
    """A class representing BIBD parameters"""

    def __init__(self, t, v, k, lambda_):
        """Initialize a new BIBDParams object"""
        self.t = t
        self.v = v
        self.k = k
        self.lambda_ = lambda_

    def __repr__(self):
        return ("BIBDParams({t}, {v}, {k}, {lambda})".
            format(**self.get_params()))

    def __str__(self):
        return ("{t}-({v},{k},{lambda})".
            format(**self.get_params()))

    def get_params(self):
        return {"t": self.t, "v": self.v, "k": self.k, "lambda":self.lambda_}

    def get_full_params(self):
        r, b = None, None
        for params in self.reduced_t():
            r, b = b, params.lambda_
        return {"t": self.t, "v": self.v, "b": b, "r": r, "k": self.k,
                "lambda": self.lambda_}

    def reduced_t(self):
        current = self
        while current.t > 0:
            yield current
            lambda_t, check = divmod((current.v-current.t+1) * current.lambda_,
                                     current.k-current.t+1)
            if check != 0:
                raise _bibderrors.BIBDParamsError("Invalid design parameters")
            else:
                current = BIBDParams(current.t - 1, current.v,
                                     current.k, lambda_t)
        yield current

    def ray_chavdhuri_wilson_test(self, params = None):
        if params is None:
            params = self.get_full_params()
        v, th, k, b = params['v'], params['t'] // 2, params['k'], params['b']
        return (v < k + th or
                b >= math.factorial(v) //
                     math.factorial(th) // math.factorial(v - th))


    __tests = [ray_chavdhuri_wilson_test]

    def is_valid(self):
        try:
            params = self.get_full_params()
        except _bibderrors.BIBDParamsError:
            return False
        return all(test(self, params) for test in BIBDParams.__tests)



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

    def __hash__(self):
        return (hash(self.t) * 2**28 + hash(self.v) * 2**16 +
                hash(self.k) * 2**8 + hash(self.lambda_))

    def __eq__(self, other):
        return (self.t == other.t and self.v == other.v and
                self.k == other.k and self.lambda_ == other.lambda_)

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

    def decrease_t(self, new_t = None):
        if new_t is None:
            new_t = self.t - 1
        if new_t > self.t or new_t < 0:
            raise _bibderrors.BIBDParamsError(
                    "Unable to decrease t parameter");
        for params in self.reduced_t():
            if params.t == new_t:
                return params

    def is_symetric(self):
        return self.v == self.get_full_params()['b']

    def remove_block(self):
        if self.t != 2 or not self.is_symetric():
            raise _bibderrors.BIBDParamsError(
                    "Base params must have t = 2 and design must be symetric")
        v, k, lambda_ = self.v, self.k, self.lambda_
        if v - k < 1 or k - lambda_ < 2:
            raise _bibderrors.BIBDParamsError(
                    "Invalid params for reduction")
        return BIBDParams(2, v - k, k - lambda_, lambda_)

    def remove_vertex(self):
        if self.t <= 2:
            raise _bibderrors.BIBDParamsError(
                    "Base params must have t > 2")
        for params in self.reduced_t():
            if params.t == self.t - 1:
                return BIBDParams(
                    self.t - 1, self.v - 1, self.k,
                    params.lambda_ - self.lambda_)

    def complement(self):
        if self.t != 2:
            raise _bibderrors.BIBDParamsError(
                    "Base params must have t = 2")
        params = self.get_full_params()
        v, b, r, k = params['v'], params['b'], params['r'], params['k']
        lambda_ = params['lambda']
        return BIBDParams(2, v, v - k, b - 2*r + lambda_)

    def derive(self):
        if self.t <= 2:
            raise _bibderrors.BIBDParamsError(
                    "Base params must have t > 2")
        return BIBDParams(self.t - 1, self.v - 1, self.k - 1, self.lambda_)

    def is_hadamard(self):
        return (self.t == 2 and self.v == 4 * self.lambda_ + 3 and
                self.k == 2 * self.lambda_ + 1)

    def extend(self):
        if not self.is_hadamard():
            raise _bibderrors.BIBDParamsError(
                    "Design params should be params for Hadamard design")
        return BIBDParams(3, self.v + 1, self.k + 1, self.lambda_)


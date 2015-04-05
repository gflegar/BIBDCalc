
class BIBDError(Exception):
    """A base class for exceptions returnd by bibdcalc library"""
    def __init__(self, what):
        self.what = what
    def __repr__(self):
        return repr(self.what)

class BIBDParamsError(BIBDError):
    pass


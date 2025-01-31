import numpy as np
import numba

@numba.jit(nopython=True)
def identity(x):
    """ A no-op link function.
    """
    return x
@numba.jit(nopython=True)
def _identity_inverse(x):
    return x
identity.inverse = _identity_inverse

@numba.jit(nopython=True)
def logit(x):
    """ A logit link function useful for going from probability units to log-odds units.
    """
    return np.log(x/(1-x))
@numba.jit(nopython=True)
def _logit_inverse(x):
    return 1/(1+np.exp(-x))
logit.inverse = _logit_inverse

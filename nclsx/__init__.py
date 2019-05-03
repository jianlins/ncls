from nclsx.src.ncls import NCLS64
from nclsx.src.ncls32 import NCLS32

import numpy as np


def NCLS(starts=None, ends=None, ids=None):
    if starts is None or ends is None or ids is None:
        test = np.array([1])
        if test.dtype == np.int32:
            return NCLS32()
        else:
            return NCLS64()
    if starts.dtype == np.int64:
        return NCLS64(starts, ends, ids)
    elif starts.dtype == np.int32:
        return NCLS32(starts, ends, ids)



from nclsx.version import __version__

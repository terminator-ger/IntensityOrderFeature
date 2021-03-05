import ctypes as ct
import numpy as np

from pyLIOP.bindings import load_library
from numpy.ctypeslib import ndpointer
from Image import imgCVShape, toByteImage

class LIOP:
    def __init__(self):
        self.lib = load_library()
        self.lib.detect.restype = ndpointer(dtype=ct.c_float,
                                            ndim=2)
        self.lib.detect.argtypes = (ct.c_int,
                                    ct.c_int,
                                    ndpointer(dtype=ct.c_uint8,
                                              ndim=2,
                                              flags="C_CONTIGUOUS"),
                                    ct.c_int,
                                    ndpointer(dtype=ct.c_float,
                                                ndim=2,
                                                flags="C_CONTIGUOUS")
        )
    
    def compute(self, img, keypoints):
        w,h = imgCVShape(img)
        l = len(keypoints)
        img = np.array(toByteImage(img), dtype=np.uint8)
        kp = np.array(keypoints, dtype=np.float)
        ptr_desc = self.lib.compute(w, h, img, l, kp)
        desc = np.ctypeslib.as_array(ct.cast(ptr_desc, 
                                    ct.c_float),
                                    shape=(l,))
        return desc
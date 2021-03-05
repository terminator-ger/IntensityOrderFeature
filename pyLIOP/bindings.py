import ctypes
import os
import sys
import random
import numpy as np


def load_library():

    root_dir = os.path.abspath(os.path.dirname(__file__))

    libnames = ['linux/libliop.so']
    libdir = 'lib'
    if sys.platform == 'win32':
        if sys.maxsize > 2 ** 32:
            libnames = ['win32/x64/liop.dll', 'win32/x64/libliop.dll']
        else:
            libnames = ['win32/x86/liop.dll', 'win32/x86/libliop.dll']
    elif sys.platform == 'darwin':
        libnames = ['darwin/libliop.dylib']

    while root_dir != None:
        for libname in libnames:
            try:
                lib = ctypes.cdll[os.path.join(root_dir, libdir, libname)]
                return lib
            except Exception as e:
                pass
        tmp = os.path.dirname(root_dir)
        if tmp == root_dir:
            root_dir = None
        else:
            root_dir = tmp

    # if we didn't find the library so far, try loading without
    # a full path as a last resort
    for libname in libnames:
        try:
            # print "Trying",libname
            lib = ctypes.cdll[libname]
            return lib
        except:
            pass

    return None

lib = load_library()
if lib == None:
    raise ImportError('Cannot load dynamic library. Did you compile the project?')

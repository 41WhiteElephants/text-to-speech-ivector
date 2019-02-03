"""numpy-kaldi i/o interface
"""
import logging
import struct
import numpy as np


def ark2dict(arkfile):  # bufferized version
    """Kaldi archive (ark) to dictionnary of numpy arrays (~npz)
    ..note: Only standard features files supported, and float (no doubles)
    """
    res = {}
    with open(arkfile) as fin:
        while True:
            #TODO: break if empty buffer here
            fname = ''
            c = fin.read(1)
            if c == '':  # EOF (EOFError not raised by read(empty))
                break
            while c != ' ':
                fname += c
                c = fin.read(1)
            logging.debug(fname)
            # end of fname
            fin.read(1)
            # data type
            assert fin.read(4) == 'BFM ', 'type not supported'
            # nrows type
            assert struct.unpack('b', fin.read(1))[0] == 4,  'type not supported'
            nrows = struct.unpack('i', fin.read(4))[0]
            # ncols type:
            assert struct.unpack('b', fin.read(1))[0] == 4,  'type not supported'
            ncols = struct.unpack('i', fin.read(4))[0]
            # data
            size = nrows * ncols * 4
            data = np.fromstring(fin.read(size), dtype=np.float32).reshape((nrows, ncols))
            res[fname] = data
    return res

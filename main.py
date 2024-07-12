#!/usr/bin/env python

import struct
import sys
import array
import collections

WAVE_FORMAT_PCM = 0x0001
def unpack(fmt, stream):
    return struct.unpack(fmt, stream.read(struct.calcsize(fmt)))

def read(path):
    with open(path, "rb") as f:
        ckID, = unpack("4s", f)
        assert ckID == b"RIFF"
        cksize0, = unpack("<I", f)
        WAVEID, = unpack("4s", f)
        assert WAVEID == b"WAVE"
        ckID, = unpack("4s", f)
        assert ckID == b"fmt "
        cksize, = unpack("<I", f)
        assert cksize == 16
        wFormatTag, = unpack("<H", f)
        if wFormatTag != WAVE_FORMAT_PCM:
            sys.stderr.write("main.py: error: only PCM Format is supported\n")
            sys.exit(1)
        nChannels, nSamplesPerSec, nAvgBytesPerSec, nBlockAlign, wBitsPerSample \
             = unpack("<HIIHH", f)
        if nChannels != 1:
            sys.stderr.write("main.py: error: only one channel is supported\n")
            sys.exit(1)
        ckID, = unpack("4s", f)
        assert ckID == b"data"
        cksize, = unpack("<I", f)
        M = nAvgBytesPerSec // nSamplesPerSec // nChannels
        Ns = cksize // nChannels // M # number of blocks
        assert nAvgBytesPerSec == nSamplesPerSec * M * nChannels
        assert nBlockAlign == M * nChannels
        assert 4 + 24 + (8 + M * nChannels * Ns) == cksize0
        a = array.array("h", f.read())
        return a

a = read("data/006c6dd6-d91e-419c-9836-c3f320da4f25.wav")
a = read(sys.argv[1])
for i, x in enumerate(a):
    print(i, x)

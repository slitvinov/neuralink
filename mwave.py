import struct
import sys
import array

WAVE_FORMAT_PCM = 0x0001


def unpack(fmt, stream):
    return struct.unpack(fmt, stream.read(struct.calcsize(fmt)))


def read_safe(path):
    with open(path, "rb") as f:
        ckID, = unpack("4s", f)
        assert ckID == b"RIFF"
        cksize0, = unpack("<I", f)
        WAVEID, = unpack("4s", f)
        assert WAVEID == b"WAVE"
        ckID, = unpack("4s", f)
        assert ckID == b"fmt "
        cksize1, = unpack("<I", f)
        assert cksize1 == 16
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
        Ns = cksize // nChannels // M
        assert nAvgBytesPerSec == nSamplesPerSec * M * nChannels
        assert nBlockAlign == M * nChannels
        assert 4 + 24 + (8 + M * nChannels * Ns) == cksize0
        a = array.array("h", f.read())
        assert len(a) == Ns
        assert a.itemsize == M
        return a


def read(path):
    with open(path, "rb") as f:
        f.seek(44)
        return array.array("h", f.read())

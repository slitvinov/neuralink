import struct


def unpack(fmt, stream):
    return struct.unpack(fmt, f.read(struct.calcsize(fmt)))


WAVE_FORMAT_PCM = 0x0001

path = "data/0052503c-2849-4f41-ab51-db382103690c.wav"
with open(path, "rb") as f:
    ckID, = unpack("4s", f)
    assert ckID == b"RIFF"
    cksize, = unpack("<I", f)
    WAVEID, = unpack("4s", f)
    assert WAVEID == b"WAVE"
    n = cksize - 4
    ckID, = unpack("4s", f)
    assert ckID == b"fmt "
    cksize, = unpack("<I", f)
    assert cksize == 16
    wFormatTag, = unpack("<H", f)
    if wFormatTag != WAVE_FORMAT_PCM:
        sys.stderr.write("main.py: error: only PCM Format is supported\n")
    nChannels, nSamplesPerSec, nAvgBytesPerSec, nBlockAlign, wBitsPerSample, cbSize, wValidBitsPerSample, dwChannelMask = unpack(
        "<HIIHHHHI", f)
    SubFormat = unpack("16c", f)
    nbytes = n - 48
    b = f.read(nbytes)
    print(nChannels, wBitsPerSample, nBlockAlign, cbSize, wValidBitsPerSample,
          dwChannelMask)

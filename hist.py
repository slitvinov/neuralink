#!/usr/bin/env python

import sys
import struct
import mwave
import itertools

s = set()
for path in sys.argv[1:]:
    a = mwave.read(path)
    s.update(a)

org = sorted(s)
cod = mwave.encode(org)
enc = mwave.decode(cod)
print(org == enc)

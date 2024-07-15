#!/usr/bin/env python

import sys
import struct
import mwave
import itertools

def min_max(fmt):
    for x in itertools.count():
        try:
            struct.pack(fmt, x)
        except struct.error:
            maxx = x - 1
            break
    for x in itertools.count(step=-1):
        try:
            struct.pack(fmt, x)
        except struct.error:
            minx = x + 1
            break
    return minx, maxx

u, v = min_max("<h")
p, q = -511, 512
s = set()
for path in sys.argv[1:]:
    a = mwave.read(path)
    s.update(a)
D = { }
for x in sorted(s):
    a = (x - u) * (q - p) / (v - u) + p
    a = int(round(a))
    if a in D:
        print(x, D[a], a)
    D[a] = x
    print(a, x)

#!/usr/bin/env python

import sys
import collections
import itertools
import mwave

a = mwave.read(sys.argv[1])
m, shift = max((sum((x + i) % 64 == 0 for x in a), i) for i in range(64))
for i, x in enumerate(a):
    x += shift
    if x % 64 != 0:
        y = (x // 64) * 64
        y0 = (x // 64) * 64 + 64
        if abs(y0 - x) < abs(y - x):
            y = y0
    else:
        y = x
    print(i, x - shift, y - shift, x - y)

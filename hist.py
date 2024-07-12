#!/usr/bin/env python

import sys
import collections
import itertools
import mwave

a = mwave.read(sys.argv[1])
c = sorted(collections.Counter(a))
c = collections.Counter(y - x for x, y in itertools.pairwise(c))
for k, v in sorted(c.items()):
    print(k, v)

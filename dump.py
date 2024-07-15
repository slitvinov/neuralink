#!/usr/bin/env python

import sys
import mwave

a = mwave.read(sys.argv[1])
for a in a:
    print(a)

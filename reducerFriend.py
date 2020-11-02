#!/usr/bin/env python
"""reducer.py"""

import sys

result = {}
for line in sys.stdin:
    #remove '\n'
    line = line.strip()
    key, value = line.split(" ")
    if key in result:
        result[key].append(int(value))
    else:
        # change value to list to use "append"
        result[key] = [int(value)]

for key,val in result.items():
    per1, per2 = key.split(",")
    a = [int(per1),int(per2)]
    tu = (a,val)
    print(tu)

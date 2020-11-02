#!/usr/bin/env python
"""mapper.py"""

import sys
result = {}
for line in sys.stdin:
    line = line.strip()
    if len(line)==0:
        continue
    key,vals = line.split(', ')# 坑一，这边是', ' 不是','
    val = vals.split(' ')
    result[key] = val
    if len(result)==1:
        continue
    else:
        for i in result[key]:
            for j in result:
                if i in result[j]:# 取交集的事情mapper在这边已经做了
                    if j<key:
                        print(j+","+key, i)
                    elif j>key:
                        print(key+","+j, i)




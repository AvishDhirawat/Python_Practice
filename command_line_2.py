#!/usr/bin/env python3

import sys

print(sys.argv)
sum_1 = 0
for i in range(1,len(sys.argv)):
    sys.argv[i] = int(sys.argv[i])
    sum_1 += sys.argv[i]
print(sum_1)

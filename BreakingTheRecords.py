#!/usr/bin/env python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_score = scores[0]
    max_count = 0
    min_score = scores[0]
    min_count = 0
    for i in range(1, len(scores)):
        if(scores[i] > max_score):
            max_score = scores[i]
            max_count += 1
        elif(scores[i] < min_score):
            min_score = scores[i]
            min_count += 1
        else:
            continue
    return max_count, min_count


n = int(input())
scores = list(map(int, input().rstrip().split()))
result = breakingRecords(scores)
print(result)

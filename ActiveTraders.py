#!/usr/bin/env python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    # Write your code here
    count_dict = {}
    n = len(customers)
    for name in customers:
        count_dict[name] = count_dict.get(name,0) + 1
    #print(count_dict)
    new_list = []
    for i in count_dict:
        if(count_dict.get(i)/n*100>=5):
            new_list.append(i)
    #print(new_list)
    new_list = sorted(new_list)
    #print(new_list)
    return new_list



customers_count = int(input().strip())

customers = []

for _ in range(customers_count):
    customers_item = input()
    customers.append(customers_item)

result = mostActive(customers)
print(result)

#!/usr/bin/env python3

from collections import Counter

x = int(input())
shoe_list = list(map(int, input().split()))
shoe_dict = Counter(shoe_list)

n = int(input())
cost= 0
for i in range(n):
    x,y = map(int,input().split())
    if(x in shoe_dict.keys() and shoe_dict[x] != 0):
        shoe_dict[x] = shoe_dict[x] - 1
        cost += y
print(cost)

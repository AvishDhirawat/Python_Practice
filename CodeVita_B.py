#!/usr/bin/env python3

from itertools import combinations

n = int(input("Enter the Number of Elements : "))
arr = list(map(int, input("Enter Elements : ").split()))
max_len = len(bin(max(arr)).replace("0b", ""))
combinations_all = sum([list(map(set, combinations(arr, i))) for i in range(1, len(arr) + 1)], [])
equi_count = 0


def toBinary(num):
    bin_num = bin(num).replace("0b", "")
    bin_num = bin_num.zfill(max_len)
    return bin_num


for i in combinations_all:
    element = ""
    for j in i:
        element += toBinary(j)
    if(element.count("1") == element.count("0")):
        equi_count += 1
print(toBinary(equi_count))

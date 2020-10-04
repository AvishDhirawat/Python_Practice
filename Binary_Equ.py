#!/usr/bin/env python3
import itertools

n = int(input("Enter the Number of Elements : "))
arr = list(map(int, input("Enter Elements : ").split()))
max_len = len(bin(max(arr)).replace("0b", ""))
equi_count = 0


def toBinary(num):
    bin_num = bin(num).replace("0b", "")
    bin_num = bin_num.zfill(max_len)
    return bin_num


for i in range(1, n+1):
    combinations_all = list(map(list, itertools.combinations(arr, i)))
    combinations_all = list(itertools.chain(*combinations_all))
    element = ""
    for j in combinations_all:
        element += toBinary(j)
    if(element.count("1") == element.count("0")):
        equi_count += 1
print(toBinary(equi_count))

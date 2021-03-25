#!/usr/bin/env python3

def shellSort(input_list):

    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i


            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp

        gap = gap//2

print("Enter the Unsorted List : ", end = "")
list = list(map(int,input().split()))

shellSort(list)
print("Sorted List : ", list)

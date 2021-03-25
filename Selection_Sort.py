#!/usr/bin/env python3

def selection_sort(input_list):

    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


print("Enter the Unsorted List : ", end = "")
list = list(map(int,input().split()))

selection_sort(list)
print("Sorted List : ", list)

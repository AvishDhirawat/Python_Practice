#!/usr/bin/env python3

def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i - 1
        nxt_element = InputList[i]

        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j + 1] = InputList[j]
            j = j - 1
        InputList[j + 1] = nxt_element

print("Enter Unsorted List : ", end = "")
list = list(map(int, input().split()))
insertion_sort(list)
print("Sorted List : ", list)

#!/usr/bin/env python3

def bubblesort(list):

    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp

print("Enter the Unsorted List : ", end = "")
list = list(map(int,input().split()))
bubblesort(list)
print("Sorted List : ", list)

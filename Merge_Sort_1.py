#!/usr/bin/env python3

def merge_sort(unsorted_list):
    if(len(unsorted_list)<=1):
        return unsorted_list

    mid = len(unsorted_list)//2
    left_list = unsorted_list[:mid]
    right_list = unsorted_list[mid:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return list(merge(left_list, right_list))

def merge(left, right):
    merge_list = []

    while(len(left)!= 0 and len(right)!=0):
        if(left[0] > right[0]):
            merge_list.append(right[0])
            right.remove(right[0])
        else:
            merge_list.append(left[0])
            left.remove(left[0])

        if(len(right) == 0):
            merge_list = merge_list + left
        else:
            merge_list = merge_list + right

        return merge_list

print("Enter the List to Sorted : ", end = "")
unsorted_list = list(map(int,input().split()))

print("Sorted List : ", merge_sort(unsorted_list))

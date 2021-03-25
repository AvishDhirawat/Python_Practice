#!/usr/bin/env python3

def binary_search(arr, start, end, element):
    if(start > end):
        return "Invalid Input"
    mid = (start + end)//2
    # print(mid, arr[mid])
    
    if(arr[mid] == element):
        return "Searched Element is at " + str(mid)
    if(arr[mid] < element):
        return binary_search(arr, mid+1, end, element)
    else:
        return binary_search(arr, start, mid-1, element)

print("Binary Search")
arr = list(map(int,input("Enter the Array : ").split()))
arr.sort()
start = 0
end = len(arr) - 1
element = int(input("Enter the Element to seach for : "))

result = binary_search(arr, start, end, element)
print(result)

#!/usr/bin/env python3

marks = list(map(int, input("Enter the array : ").split()))
n = int(input("Enter the Size : "))

print("Sum of initial marks elements :",sum(marks))

def min_marks(marks, n):
    matches = []
    sum = marks[0]
    for i in range(0,n):
        for j in range(i+1, n):
            if(marks[i] == marks[j]):
                matches.append(j)
    print("Matches :",matches)
    for i in range(1,n):
        if(i in matches):
            marks[i] = max(marks) + 1
        sum += marks[i]
    print("Marks after updating :",marks)
    return sum

result = min_marks(marks, n)
print("Result :",result)
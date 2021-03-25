n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

def ques(arr):
    i = 1
    flag = 0
    while(i):
        if(i not in arr):
            return i

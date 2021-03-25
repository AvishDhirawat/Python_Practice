def solve(A, B, C):
    count = 0
    i=0
    while(1):
        if(i==len(A)):
            break
        elif (A[i] not in B):
            A.pop(i)
        else:
            i = i+1
    if (B[0] in A):
        j = A.index(B[0])
        A = A[j:]
    else:
        A.insert(0, B[0])
        count += 1
    print(A)
    if (B[len(B) - 1] in A):
        j = A.index(B[len(B) - 1])
        A = A[:j + 1]
    else:
        A.insert(len(A), B[len(B) - 1])
        count += 1
    print(A)
    for i in range(len(B)-1):
        if (B[i] != A[i]):
            A.insert(i, B[i])
            count += 1
        if (A[i] not in B):
            A.remove(A[i])
        print(A)
    # i=0
    # while(len(A)!=len(B)):
    #     if(A[i]!=B[i]):
    #         A.pop(i)
    #     else:
    #         i+=1

    print("After Remove : ", A)
    print("Count : ",count)
    if(A==B):
        soln = C * count
        return soln
A = [5, 24, 10, 15, 20, 16, 1, 27, 28]
B = [29, 23, 19, 20, 30, 12, 21, 7]
C = 67
result = solve(A, B, C)
print("B : ",B)
print(result)
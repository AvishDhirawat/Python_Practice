arr1= [1, 3, 4, 5, 7]
arr2= [2, 3, 5, 6]

union = []
inter = []

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if(arr1[i]==arr2[j]):
            inter.append(arr1[i])
        else:
            union.append(arr1[i])
print("union : ", union)
print("inter : ", inter)

#!/usr/bin/env python3

from itertools import combinations

a = []
n = int(input())
list_row = []
for i in range(n):
    a.append([])
    row = int(input())
    list_row.append(row)
# a[i] = list(map(int, input("Enter a multiple value: ").split()))
    for j in range(row):
        el = int(input())
        a[i].append(el)


i = 1
s = 0
# print(a)
p = []
for row in a:
    # print(" row:{}".format(i))
    i = i + 1
    for ele in row:
        s = ele + s
        print(ele)
        p.append(ele)
s = int(s / n)
print(s)
p.sort()
print(p)
print(list_row)

# for i in range(n):
#   total=0
# for j in l:
#      right=l[0]
#     if(right==)


def combs(lst, n):
    return (c for k in range(1, n + 1) for c in combinations(lst, k))


combinations_all = sum([list(map(set, combinations(p, i))) for i in range(1, len(p) + 1)], [])
# print(combinations_all)
# print(type(combinations_all))
l1 = []
i = 0
a1 = []
for row in combinations_all:
    r = 0
    i = i + 1
    for ele in row:
        r = r + ele

        a1.append(ele)
    # print(r)
    if(r == s):
        l1.append(combinations_all[i-1])
a1 = list(dict.fromkeys(a1))
# print(a1)


# print(i)
# print(l1)
# print(list_row)
# print(" ")
final = []

for i in range(n+1):
    for j in range(len(l1)):

        if(list_row[i] == len(l1[j])):
            print(list(l1[j]))
            q = list(l1[j])
            final.append(q)
            l1.remove(l1[i])
            break



3
2
160
340
3
40
448
12
2
300
200



3
2
6
13
3
20
7
10
1
4

#!/usr/bin/env python3

import math

N = int(input())
wall_array = []
for i in range(N):
    wall_array.append(list(map(str, input().split())))


def melt_wall(wall_array, N):
    var_c = 0
    for i in range(N):
        for j in range(N):
            if wall_array[i][j] == 'D':
                var_c += 1
    sqrt_c = math.sqrt(var_c)
    floor_c = math.floor(sqrt_c)
    return floor_c


result = melt_wall(wall_array, N)
print(result, end="")

#!/usr/bin/emv python3

# n = 5
# inp_list = [1, 4, 5, 4, 5]
n = int(input("Enter Count of Marks : "))
inp_list = list(map(int, input("Enter the Marks : ").split()))

def minmarks(n, inp_list):

    count_dict = {}
    max_list = inp_list[0]

    for i in range(n):
        count_dict[inp_list[i]] = count_dict.get(inp_list[i], 0) + 1
        if(inp_list[i] > max_list):
            max_list = inp_list[i]

        elif(count_dict[inp_list[i]] > 1 & inp_list[i] <= max_list):
            inp_list[i] = max(inp_list) + 1

    # print(count_dict)
    # print(inp_list)
    return sum(inp_list)

results = minmarks(n, inp_list)
print(results)

#!/usr/bin/env python3

n,k = input().split()
s = input()
n = int(n)
k = int(k)
#n, k = 3, 3
#s = "abc"
words = []
for i in range(n):
    words.append(s[i])
#combinations = []
words1 = sorted(words)
def no_use():

    temp_list = []
    temp_list1 = []
    for j in range(n):
        for i in words:
            combinations.append(words1[j] + i)
    if(len(combinations[1])<=n):
        for i in range(len(combinations)):
            if(words[0] >= combinations[i][0]):
                temp_list.append(combinations[i][0])
    else:
        for l in words:
            for m in range(len(combinations)):
                if(len(combinations[m])<k):
                    combinations.append(combinations[m]+l)
    # print(combinations)
    # help(set)
        if(len(combinations[1])<=n):
            for i in range(len(combinations)):
                if(words[0] < combinations[i][0]):
                    temp_list1.append(combinations[i][0])
def lexo_func_1(n, k, words, words1):
    lexo = ""
    flag = 0
    words1.reverse()
    for i in range(0,n-1):
        if(words[i] <= words1[i] and words1[i+1] < max(words) and words[i+1] not in lexo):
            lexo+= words1[i+1]
        elif(words[i] == max(words) and flag == 0):
            lexo+= words[i]
            flag == 1
        else:
            lexo += words[i]
    while(len(lexo) != k):
        lexo+=min(words)
        

def lexo_func(n,k,words,words1):
    words1.reverse()
    lexo = ""
    flag = 0
    max_dict = dict()
    for i in range(n):
        max_num = 0
        word_list = []
        max_dict.setdefault(words[i], 0)
        for j in range(n):
            if(words[i] < words[j] and words[j] not in word_list):
                max_num +=1
                word_list.append(words[j])
        max_dict[words[i]] = max_dict[words[i]]+max_num
        #print(max_dict[words[i]])
    #print(max_dict)
    for i in words:
        if(max_dict[i] == 1):
            lexo+= max(words)
            flag = 1
        elif(max_dict[i] >1 and i not in lexo):
            lexo+= i
    while(len(lexo) != k):
        lexo+=min(words)
    return lexo
#print(combinations)
#s_set = set(combinations)
#print(temp_list)
#print(temp_list1)
lexo =  lexo_func(n, k, words, words1)
#print(max(words))
print(lexo)

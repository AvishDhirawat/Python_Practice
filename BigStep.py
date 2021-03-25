
def len_num(num):
    count = 0

    while(num!=0):
        num = num/10
        count+=1
    return count

inputs = [5, 10, 20, 40, 111, 150, 180]
n = len(inputs)
maxn = inputs[n-1]
max_len = len_num(maxn)
for i in range(n):
    num_len = len_num(inputs[i])
    if(inputs[i] < maxn and num_len == max_len):
        print(inputs[i])

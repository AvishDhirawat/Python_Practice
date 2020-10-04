size = int(input())
num_list = list(map(int, input().split()))
#size = num_list.pop(0)
def convert_to_bit(n):
    n = str(n)
    num_l = list()
    for i in range(len(n)):
        num_l.append(n[i])
    #print(num_list)
    large = int(max(num_l))
    small = int(min(num_l))
    bit_digit = large*11 + small*7
    bit_digit = str(bit_digit)
    #print(bit_digit)
    if(len(bit_digit) == 3):
        return bit_digit[1:]
    return bit_digit
bit_list = list()
for i in range(size):
    bit_list.append(str(convert_to_bit(num_list[i])))
def check_pair(bit_list):
    pair_list = list()
    pair = 0
    for i in range(size):
        k = i+1
        for j in range(k, size):
            if(bit_list[i] == bit_list[j] and i%2 == j%2):
                pair+=1
    #         print(bit_list[j][0])
            elif (bit_list[i][0] == bit_list[j][0] and i%2 == j%2):
                if(bit_list[i] not in pair_list):
                    pair_list.append(bit_list[i])
                    pair+=1
                if(bit_list[j] not in pair_list):
                    pair_list.append(bit_list[j])
                    pair+=1
    return pair-1
pair = check_pair(bit_list)
print(pair)

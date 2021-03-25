inp_list =[1, 2, 3, 1, 2, 3, 5, 2, 1, 3, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
count = {}
for i in range(len(inp_list)):
    if(i%5 == 0 and inp_list[i] == 1):
        count["Malaysia"] = count.get("Malaysia", 0)+1
    elif(i%5==1 and inp_list[i] == 1):
        count["Australia"] = count.get("Australia", 0)+1
    elif(i%5==2 and inp_list[i] == 1):
        count["Germany"] = count.get("Germany", 0)+1
    elif(i%5==3 and inp_list[i] == 1):
        count["Dubai"] = count.get("Dubai", 0)+1
    elif(i%5==4 and inp_list[i] == 1):
        count["France"] = count.get("France", 0)+1
    elif(inp_list[i] == 6):
        print("INVALID INPUT")
        exit(0)
    else:
        continue
print(count)
while(len(count)!=0):
    max_count = max(count, key = count.get)
    print(max_count)
    count.pop(max_count)
# count = sorted(count.keys())

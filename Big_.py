n = int(input())
sum = 0
for i in range(1, n//2 + 1):
    if(n%i == 0):
        # arr.append()
        sum += i
if(sum == n):
    print("It is perfect number")
print("sum = ", sum)

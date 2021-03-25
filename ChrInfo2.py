# Python Implementation of the above approach

# Function to find the minimum number
# character change required
import math as ma

n = int(input())
arr = []
for i in range(n):
    arr.append(input())

def change(s):

	# Finding the length of the string
	n = len(s)

	# To store the number of replacement operations
	cc = 0

	for i in range(n//2):

		# If the characters at location
		# i and n-i-1 are same then
		# no change is required
		if(s[i]== s[n-i-1]):
			continue

		# Counting one change operation
		cc+= 1

		# Changing the character with higher
		# ascii value with lower ascii value
		if(s[i]<s[n-i-1]):
			s[n-i-1]= s[i]
		else:
			s[i]= s[n-i-1]

	return cc
count=0
for i in range(n):
    result = change(list(arr[i]))
    flag = 0
    if(result == 0 and len(arr[i])%2==1):
        # for j in range(1, len(arr[i])):
        #     if(arr[i][j] != arr[i][0]):
        #         flag = 1
        #         break
        flag = 1
    if(result==1 or flag == 1 ):
        count+=1
print(count)

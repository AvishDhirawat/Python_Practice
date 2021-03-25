#!/usr/bin/env python3
# Python 3 code to check if
# the array is wave array

# Function to check if
# array is wave array
# arr : input array
# n : size of array
def isWaveArray(arr , n):

	result = True

	# Check the wave form
	# If arr[1] is greater than
	# left and right. Same pattern
	# will be followed by whole
	# elements, else reverse pattern
	# will be followed by array elements

	if (arr[1] > arr[0] and arr[1] > arr[2]):
		for i in range(1, n - 1, 2):

			if (arr[i] > arr[i - 1] and
				arr[i] > arr[i + 1]):
				result = True

			else :
				result = False
				break

		# Check for last element
		if (result == True and n % 2 == 0):
			if (arr[n - 1] <= arr[n - 2]) :
				result = False

	elif (arr[1] < arr[0] and
		arr[1] < arr[2]) :
		for i in range(1, n - 1, 2) :

			if (arr[i] < arr[i - 1] and
				arr[i] < arr[i + 1]):
				result = True

			else :
				result = False
				break

		# Check for last element
		if (result == True and n % 2 == 0) :
			if (arr[n - 1] >= arr[n - 2]) :
				result = False

	return result

def sortInWave(arr, n):

	# Traverse all even elements
    for i in range(0, n, 2):

		# If current even element is smaller than previous
		if (i> 0 and arr[i] < arr[i-1]):
			arr[i],arr[i-1] = arr[i-1],arr[i]

		# If current even element is smaller than next
		if (i < n-1 and arr[i] < arr[i+1]):
			arr[i],arr[i+1] = arr[i+1],arr[i]

# Driver Code
arr = [ 10, 5, 6, 3, 2, 20, 100, 80]
sortInWave(arr, len(arr))
print("Wave Sort : ")
for i in range(0,len(arr)):
    print arr[i],

n = len(arr)
#print("\nConclusion : ",end = "")
if (isWaveArray(arr, n)):
	print("\nTrue")
else:
	print("\nFalse")

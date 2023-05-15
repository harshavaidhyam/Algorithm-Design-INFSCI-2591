
def balancedArrMax(arr, n):

	total = 0
	maxsize = -1
	for i in range(0, n-1):
	
		total = -1 if(arr[i] == 0) else 1

		for j in range(i + 1, n):
		
			total = total + (-1) if (arr[j] == 0) else total + 1

			if (total == 0 and maxsize < j-i + 1):
				
				maxsize = j - i + 1
				startindex = i
	
	if (maxsize == -1):
		print("No balanced subset");
	else:
		print(startindex, "-", startindex + maxsize-1);

	return maxsize

#test case 1
arr = [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1]
size = len(arr)
balancedArrMax(arr, size)

#test case 2
# arr = [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0 ,0]
# size = len(arr)
# balancedArrMax(arr, size)

# #test case 3
# arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
# size = len(arr)
# balancedArrMax(arr, size)


# #test case 4
# arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# size = len(arr)
# balancedArrMax(arr, size)


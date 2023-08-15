
def binPack(weight, length, capacity):
	
	res = 0
	

	x = [0]*length
	
	for i in range(length):
	

		j = 0
		while( j < res):
			if (x[j] >= weight[i]):
				x[j] = x[j] - weight[i]
				break
			j+=1
			

		if (j == res):
			x[res] = capacity - weight[i]
			res= res+1
	return res
	
weight = [0.1, 0.26, 0.35, 0.4, 0.5, 0.6, 0.75, 0.99]
capacity = 1
length = len(weight)
print("Number of bins required : ",binPack(weight, length, capacity))

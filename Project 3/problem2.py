
def knapSackalgo(W, wt, val, n):
	K = [[0 for w in range(W + 1)]
			for i in range(n + 1)]
			

	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i - 1] <= w:
				K[i][w] = max(val[i - 1]
				+ K[i - 1][w - wt[i - 1]],
							K[i - 1][w])
			else:
				K[i][w] = K[i - 1][w]

	res = K[n][W]
	print(res)
	
	w = W
	for i in range(n, 0, -1):
		if res <= 0:
			break

		if res == K[i - 1][w]:
			continue
		else:


			print(wt[i - 1])
			

			res = res - val[i - 1]
			w = w - wt[i - 1]


val = [20, 30, 35, 12, 3]
wt = [2 ,5, 7, 3, 1]
W = 9
n = len(val)


print("Maximum profit along with their weights:")
knapSackalgo(W, wt, val, n)

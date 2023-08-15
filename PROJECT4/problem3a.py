
from typing import DefaultDict

INT_MAX = 2000000000
def findMinRoute(tsp):
	sum = 0
	counter = 0
	j = 0
	i = 0
	min = INT_MAX
	visitedRouteList = DefaultDict(int)


	visitedRouteList[0] = 1
	route = [0] * len(tsp)


	while i < len(tsp) and j < len(tsp[i]):


		if counter >= len(tsp[i]) - 1:
			break


		if j != i and (visitedRouteList[j] == 0):
			if tsp[i][j] < min:
				min = tsp[i][j]
				route[counter] = j + 1

		j += 1


		if j == len(tsp[i]):
			sum += min
			min = INT_MAX
			visitedRouteList[route[counter] - 1] = 1
			j = 0
			i = route[counter] - 1
			counter += 1


	i = route[counter - 1] - 1

	for j in range(len(tsp)):

		if (i != j) and tsp[i][j] < min:
			min = tsp[i][j]
			route[counter] = j + 1

	sum += min


	print("Minimum Cost is :", sum)


#test case 1:
# if __name__ == "__main__":

# 	# Input Matrix
# 	tsp = [[-1, 60, 100, 50, 90], [60, -1, 70, 40, 30], [100, 70, -1, 65,50], [50, 40, 65, -1,110]], [90, 30, 40, 110,-1]


# 	findMinRoute(tsp)


#test case 2:
if __name__ == "__main__":

	# Input Matrix
	tsp = [[-1, 10, 15, 20], [10, -1, 35, 25], [15, 35, -1, 30], [20, 25, 30, -1]]


	findMinRoute(tsp)





# x_coordinate = []
# y_coordinate = []

#findMinRoute(tsp)
#x_coordinate.append(tsp)
#y_coordinate.append(round(time.time() - start_time, 6))


# plt.plot(x_coordinate, y_coordinate, marker="o")
# plt.xlabel("Size")
# plt.ylabel("Time")
# plt.show()
def tsp_heuristics(G,s):
	visited = []
	src = s
	cost = 0
	while s not in visited:

		edges = G[s]
		min_weight = -1
		min_node = -1
		visited.append(s)
		for (i, j) in enumerate(edges):

			if (min_weight == -1) and (i not in visited):
				min_weight = j
				min_node = i

			elif (min_weight != -1) and (j < min_weight) and (i not in visited):
				min_weight = j
				min_node = i
		if min_node != -1:
			s = min_node
		if min_weight != -1:
			cost += min_weight
	cost += G[s][src]
	print("The total cost is:", cost)

#test case1
G = [[-1, 60, 100, 50, 90],[60, -1, 70, 40, 30 ],[100, 70, -1, 65, 55] ,[50, 40, 65, -1,110 ],[90, 30, 55, 110, -1]] 

#test case2
# G = [[-1, 10, 15, 20], [10, -1, 35, 25], [15, 35, -1, 30], [20, 25, 30, -1]]   

tsp_heuristics(G,0)





# x_coordinate = []
# y_coordinate = []

# for i in range(9):
# 	g.dijkstra(i)
#     x_coordinate.append(i)
#     y_coordinate.append(round(time.time() - start_time, 6))


# plt.plot(x_coordinate, y_coordinate, marker="o")
# plt.xlabel("Size")
# plt.ylabel("Time")
# plt.show()
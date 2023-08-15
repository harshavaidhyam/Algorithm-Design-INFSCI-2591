
import sys
from turtle import clear
import time
import matplotlib.pyplot as plt

start_time=time.time()

class Graph():
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def prntsol(self, dist):
		print("Vertex \tDistance from Source")
		for node in range(self.V):
			print(node, "\t", dist[node])


	def mindist(self, dist, sptSet):

		min = sys.maxsize

	
		for u in range(self.V):
			if dist[u] < min and sptSet[u] == False:
				min = dist[u]
				min_index = u

		return min_index


	def dijkstra(self, src):

		dist = [sys.maxsize] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):


			x = self.mindist(dist, sptSet)


			sptSet[x] = True


			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == False and \
						dist[y] > dist[x] + self.graph[x][y]:
					dist[y] = dist[x] + self.graph[x][y]

		self.prntsol(dist)


# Driver's code
if __name__ == "__main__":
	g = Graph(9)
	g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
			[4, 0, 8, 0, 0, 0, 0, 11, 0],
			[0, 8, 0, 7, 0, 4, 0, 0, 2],
			[0, 0, 7, 0, 9, 14, 0, 0, 0],
			[0, 0, 0, 9, 0, 10, 0, 0, 0],
			[0, 0, 4, 14, 10, 0, 2, 0, 0],
			[0, 0, 0, 0, 0, 2, 0, 1, 6],
			[8, 11, 0, 0, 0, 0, 1, 0, 7],
			[0, 0, 2, 0, 0, 0, 6, 7, 0]
			]
for i in range(9):
	g.dijkstra(i)

print("=%s seconds -" % (time.time() - start_time))


# #plotting of time complexity

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
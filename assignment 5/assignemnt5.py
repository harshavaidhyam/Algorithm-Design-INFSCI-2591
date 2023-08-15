import matplotlib.pyplot as plt
import time
import random


start_time=time.time()

v = 4
INF = 999

def floyd(G):
    dist = list(map(lambda j: list(map(lambda k: k, j)), G))

    for i in range(v):
        for j in range(v):
            for k in range(v):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
    sol(dist)

def sol(dist):
    for j in range(v):
        for k in range(v):
            if(dist[j][k] == INF):
                print("INF", end=" ")
            else:
                print(dist[j][k], end="  ")
        print(" ")

G = [[0, 5, INF, INF],
         [50, 0, 15, 5],
         [30, INF, 0, 15],
         [15, INF, 5, 0]]
floyd(G)

#plotting of time complexity

x_coordinate = []
y_coordinate = []

for k in range(1, 20000, 100):
     a = [random.randint(0, 200000) for i in range(k * 100)]
     floyd(G)
     print("Time taken: ", round(time.time() - start_time, 6))
     x_coordinate.append(k * 100)
     y_coordinate.append(round(time.time() - start_time, 6))   


plt.plot(x_coordinate, y_coordinate, marker="o")
plt.xlabel("Size")
plt.ylabel("Time")
plt.show()
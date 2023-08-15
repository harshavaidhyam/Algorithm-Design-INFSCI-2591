from collections import defaultdict
import time
import random
import matplotlib.pyplot as plt


start_time=time.time()
def generate(n):
  graph = dict()
  for i in range(1,n+1):
    vi = random.sample(range(1,n+1), random.randint(0,n))
    if i in vi:
      vi.remove(i)
    vi.sort()
    graph[i] = vi
  return graph

def graphSets(graph):
	

	if(len(graph) == 0):
		return []
	

	if(len(graph) == 1):
		return [list(graph.keys())[0]]
	

	currnt = list(graph.keys())[0]
	

	graph2 = dict(graph)
	

	del graph2[currnt]
	

	res1 = graphSets(graph2)
	



	for v in graph[currnt]:
		

		if(v in graph2):
			del graph2[v]
	

	res2 = [currnt] + graphSets(graph2)
	

	if(len(res1) > len(res2)):
		return res1
	return res2

def locate_clique(graph):
    
    
    cl =[]
    vertices = list(graph.keys())
    for ve in vertices:
      clique = []
      clique.append(ve)
      for v in vertices:
          if v in clique:
              continue
          isNext = True
          for u in clique:
              if u in graph[v]:
                  continue
              else:
                  isNext = False
                  break
          if isNext:
              clique.append(v)

      cl.append((len(clique),sorted(clique)))
    (cin, clique) = max(cl)
    return clique



# Test case 1:
# graph = dict([])

# graph[1] = []
# graph[2] = [3,5]
# graph[3] = [2,6]
# graph[4] = [5]
# graph[5] = [4,6]
# graph[6] = [5]
# graph[7] = [8,9]
# graph[8] = [7,9]
# graph[9] = [7,8]

# maximalIndependentSet = graphSets(graph)
# clique = locate_clique(graph)
# # Prints the Result
# print("largest independent set: ")
# for i in maximalIndependentSet:
# 	print( i, end =" ")
# print(" ")
# print("Max clique is: ", clique)

# Test case 2:
graph = dict([])

graph[1] = [4]
graph[2] = [3,5,6]
graph[3] = [2,5,6]
graph[4] = [7,8]
graph[5] = [2,3,6]
graph[6] = [2,3,5]
graph[7] = [4,8]
graph[8] = [4,7,9]
graph[9] = [8]

maximalIndependentSet = graphSets(graph)
clique = locate_clique(graph)
# Prints the Result
print("largest independent set: ")
for i in maximalIndependentSet:
	print( i, end =" ")
print(" ")
print("Max clique is: ", clique)



# #plotting of time complexity

# x_coordinate = []
# y_coordinate = []


# for i in maximalIndependentSet:
# 	    print( i, end =" ")
#     x_coordinate.append(i)
#     y_coordinate.append(round(time.time() - start_time, 6))

# plt.plot(x_coordinate, y_coordinate, marker="o")
# plt.xlabel("Size")
# plt.ylabel("Time")
# plt.show()


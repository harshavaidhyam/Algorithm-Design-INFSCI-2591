class Graph:
    def __init__(self, edge_list, num_of_nodes):

        self.adjacency_list = [[] for _ in range(num_of_nodes)]
 
        for (origin, dest) in edge_list:
            self.adjacency_list[origin].append(dest)
 
 
def print_graph(graph):
    for origin in range(len(graph.adjacency_list)):
        for dest in graph.adjacency_list[origin]:
            print(f'{origin} —> {dest} ', end='')
        print()
 
 
# if __name__ == '__main__':
#     # Set up an edge list and number of nodes
#     edge_list = [(0, 1), (1, 2), (2, 3), (0, 2), (3, 2), (4, 5), (5, 4)]
#     num_of_nodes = 6
 
#     graph = Graph(edge_list, num_of_nodes) 
#     print_graph(graph)

#TEST CASE 1
if __name__ == '__main__':
    edge_list = [(2, 3)]
    num_of_nodes = 7
 
    graph = Graph(edge_list, num_of_nodes) 
    print_graph(graph)
    print("Vertex 3 and 4 has the highest degree")

#TESTCASE 2
# if __name__ == '__main__':
#     edge_list = [(2, 3),(3,6), (6,2)]
#     num_of_nodes = 7
 
#     graph = Graph(edge_list, num_of_nodes) 
#     print_graph(graph)
#     print("Vertex 3, 4, 6 has the highest degree")

#TEST CASE 3
# if __name__ == '__main__':
#     edge_list = [(3,0), (3,2), (3,4)]
#     num_of_nodes = 7
 
#     graph = Graph(edge_list, num_of_nodes) 
#     print_graph(graph)
#     print("Vertex 4 has the highest degree")
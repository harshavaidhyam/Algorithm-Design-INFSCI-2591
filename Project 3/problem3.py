def isomorphic_check(x, map):
    if check(x,map):
        if x == n:
            print(map)
            return True
        for i in range(n):
            flag = 0
            for j in range(x):
                if map[j] == i:
                    flag = 1
            if flag == 1:
                continue
            map[x] = i
            if isomorphic_check(x+1, map):
                return True
        return False
    else:
        return False

def check(x, map):
    for i in range(x-1):
        if graph1[i][x-1] != graph2[map[i]][map[x-1]]:
            return False
    return True

#test case 1:

# n = 5
# graph1 = [[0,1,0,1,0],
#           [1,0,1,1,1],
#           [0,1,0,1,1],
#           [1,1,1,0,0],
#           [0,1,1,0,0]]

# graph2 = [[0,1,0,1,1],
#           [1,0,0,1,0],
#           [0,0,0,1,1],
#           [1,1,1,0,1],
#           [1,0,1,1,0]]

#test case 2:

n = 6
graph1 = [[0,1,1,0,1,0],
          [1,0,1,0,0,1],
          [1,1,0,1,0,0],
          [0,0,1,0,1,1],
          [1,0,0,1,0,1],
          [0,1,0,1,1,0]]

graph2 = [[0,1,0,1,1,0],
          [1,0,1,0,0,1],
          [0,1,0,1,0,1],
          [1,0,1,0,0,1],
          [1,0,0,1,0,1],
          [0,1,0,1,1,0]]


#test case 3:

# n = 7
# graph1 = [[0,1,0,1,1,0,0],
#           [1,0,1,0,1,0,0],
#           [0,1,0,1,0,1,0],
#           [1,0,1,0,0,0,1],
#           [1,1,0,0,0,1,0],
#           [0,0,1,0,1,0,1]
#           [0,0,0,1,1,1,0]]

# graph2 = [[0,1,0,1,0,0,1],
#           [1,0,1,0,1,0,0],
#           [0,1,0,1,0,1,0],
#           [1,0,1,0,0,0,1],
#           [0,1,0,0,0,1,1],
#           [0,0,1,0,1,0,1]
#           [0,0,0,1,1,1,0]]

map = [0 for i in range(n)]
temp = isomorphic_check(0, map)
if temp == True:
    print("isomorphic")
else:
    print("Non isomorphic")

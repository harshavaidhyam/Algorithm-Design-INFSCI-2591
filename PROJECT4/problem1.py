def cc_sort(arr):
  
  table = []
  count = []
  for a in arr:
    c1 = 0
    c2 = 0
    for i in range(len(arr)):
      if arr[i] < a:
        c2 += 1
    while(c2 in table):
      c2 += 1
    table.append(c2)
  print("Table for the counts:", table)
  new = [0 for x in range(len(arr))]
  for i in range(len(arr)):
    new[table[i]] = arr[i]
  print("Sorted array: ", new)


#test case 1:
print(" ")
print("test case 1:")
cc_sort([1, 4, 1, 2, 7, 5, 2])

#test case 2:
print(" ")
print("test case 2:")
cc_sort([5, 2, 9, 5, 2, 3, 5])


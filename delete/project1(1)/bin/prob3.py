import random
from sys import maxsize
import time
import matplotlib.pyplot as plt


start_time=time.time()

def maxSubArraySum(a, size):

	x = -maxsize - 1
	y = 0
	start = 0
	end = 0
	s = 0

	for i in range(0, size):

		y += a[i]

		if x < y:
			x = y
			start = s
			end = i

		if y < 0:
			y = 0
			s = i+1

	print("i is %d" % (start+1))
	print("j is %d" % (end+1))

#test case 1

# a = [-2, -5, 6, -2, -3, 1, 5, -6]
# maxSubArraySum(a, len(a))

# print("=%s seconds -" % (time.time() - start_time))

#test case 2: uncomment to run

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, -10, -100, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
maxSubArraySum(a, len(a))

print("=%s seconds -" % (time.time() - start_time))


#plotting of time complexity

x_coordinate = []
y_coordinate = []

for k in range(1, 2000, 100):
     a = [random.randint(0, 200000) for i in range(k * 100)]
    #  start = time.time()
     maxSubArraySum(a, len(a))
     print("Time taken: ", round(time.time() - start_time, 6))
     x_coordinate.append(k * 100)
     y_coordinate.append(round(time.time() - start_time, 6))   


plt.plot(x_coordinate, y_coordinate, marker="o")
plt.xlabel("Size")
plt.ylabel("Time")
plt.show()
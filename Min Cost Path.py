R = 3
C = 3
import sys

def minCost(cost, m, n):
	if (n < 0 or m < 0):
		return sys.maxsize
	elif (m == 0 and n == 0):
		return cost[m][n]
	else:
		return cost[m][n] + min( minCost(cost, m-1, n-1),
								minCost(cost, m-1, n),
								minCost(cost, m, n-1) )

def min(x, y, z):
	if (x < y):
		return x if (x < z) else z
	else:
		return y if (y < z) else z

cost= [ [1, 2, 3],
		[4, 8, 2],
		[1, 5, 3] ]
print(minCost(cost, 2, 2))

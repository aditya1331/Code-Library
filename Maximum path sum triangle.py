
def maxPathSum(tri, i, j, row, col):
	if(j == col ):
		return 0

	if(i == row-1 ):
		return tri[i][j]

	return tri[i][j] + max(maxPathSum(tri, i+1, j, row, col),
							maxPathSum(tri, i+1, j+1, row, col))

tri = [ [1, 0, 0],[4, 8, 0],[1, 5, 3] ]
print(maxPathSum(tri, 0, 0, 3, 3))

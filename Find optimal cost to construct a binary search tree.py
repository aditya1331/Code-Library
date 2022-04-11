import sys


# Find optimal cost to construct a binary search tree from keys
# `i` to `j`, where each key `k` occurs `freq[k]` number of times
def findOptimalCost(freq, i, j, level):
    # base case
    if j < i:
        return 0

    optimalCost = sys.maxsize

    # consider each key as a root and recursively find an optimal solution
    for k in range(i, j + 1):
        # recursively find the optimal cost of the left subtree
        leftOptimalCost = findOptimalCost(freq, i, k - 1, level + 1)

        # recursively find the optimal cost of the right subtree
        rightOptimalCost = findOptimalCost(freq, k + 1, j, level + 1)

        # current node's cost is `freq[k]×level`

        # update the optimal cost
        optimalCost = min(optimalCost, freq[k] * level + leftOptimalCost
                          + rightOptimalCost)

    # Return minimum value
    return optimalCost


if __name__ == '__main__':
    freq = [25, 10, 20]

    print('The optimal cost of constructing BST is',
          findOptimalCost(freq, 0, len(freq) - 1, 1))
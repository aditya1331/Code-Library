import sys


# Function to check if string `X[i…j]` is a palindrome or not
def isPalindrome(X, i, j):
    while i <= j:
        if X[i] != X[j]:
            return False
        i = i + 1
        j = j - 1

    return True


# Recursive function to find the minimum cuts needed in a string
# such that each partition is a palindrome
def findMinCuts(X, i, j):
    # base case: if starting index `i` and ending index `j` are equal,
    # or `X[i…j]` is already a palindrome.
    if i == j or isPalindrome(X, i, j):
        return 0

    # stores the minimum number of cuts needed to partition `X[i…j]`
    min = sys.maxsize

    # take the minimum over each possible position at which the
    # string can be cut

    '''
        (X[i]) | (X[i+1…j])
        (X[i…i+1]) | (X[i+2…j])
        (X[i…i+2]) | (X[i+3…j])
        …
        …
        (X[i…j-1]) | (X[j])
    '''

    for k in range(i, j):

        # recur to get minimum cuts required in `X[i…k]` and `X[k+1…j]`
        count = 1 + findMinCuts(X, i, k) + findMinCuts(X, k + 1, j)

        if count < min:
            min = count

    # return the minimum cuts required
    return min


def findMinimumCuts(X):
    # base case
    if not X:
        return 0

    return findMinCuts(X, 0, len(X) - 1)


if __name__ == '__main__':
    X = 'BABABCBADCD'
    print('The minimum cuts required are', findMinimumCuts(X))
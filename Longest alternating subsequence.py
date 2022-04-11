def findLongestSequence(A, start, end, flag):
    result = 0
    for i in range(start, end + 1):

        if flag and A[i - 1] < A[i]:
            result = max(result, 1 + findLongestSequence(A, i + 1, end, not flag))

        elif not flag and A[i - 1] > A[i]:
            result = max(result, 1 + findLongestSequence(A, i + 1, end, not flag))

        else:
            result = max(result, findLongestSequence(A, i + 1, end, flag))

    return result

def longestSequence(A):
    if not A:
        return 0

    return 1 + max(findLongestSequence(A, 1, len(A) - 1, True),
                   findLongestSequence(A, 1, len(A) - 1, False))

if __name__ == '__main__':
    A = [8, 9, 6, 4, 5, 7, 3, 2, 4]

    print('The length of the longest alternating subsequence is', longestSequence(A))

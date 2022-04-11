
def findMinAbsDiff(S, n, S1=0, S2=0):

    if n < 0:
        return abs(S1 - S2)

    inc = findMinAbsDiff(S, n - 1, S1 + S[n], S2)

    exc = findMinAbsDiff(S, n - 1, S1, S2 + S[n])

    return min(inc, exc)


if __name__ == '__main__':
    S = [10, 20, 15, 5, 25]

    print('The minimum difference is', findMinAbsDiff(S, len(S) - 1))
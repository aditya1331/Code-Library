def dist(X, m, Y, n):

    if m == 0:
        return n

    if n == 0:
        return m


    cost = 0 if (X[m - 1] == Y[n - 1]) else 1

    return min(dist(X, m - 1, Y, n) + 1,
               dist(X, m, Y, n - 1) + 1,
               dist(X, m - 1, Y, n - 1) + cost)


if __name__ == '__main__':
    X = 'kitten'
    Y = 'sitting'

    print('The Levenshtein distance is', dist(X, len(X), Y, len(Y)))
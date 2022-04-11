
def printCombinations(i, n, out, index):

    if n == 0:
        print(out[:index])

    for j in range(i, n + 1):
        out[index] = j

        printCombinations(j, n - j, out, index + 1)


if __name__ == '__main__':
    n = 5
    out = [None] * n

    printCombinations(1, n, out, 0)
def printLexicographicOrder(s, result=''):

    if len(result) == len(s):

        print(result, end=' ')
        return

    for c in s:
        printLexicographicOrder(s, result + c)


def findLexicographic(s):

    if not s:
        return

    c = sorted(list(s))

    printLexicographicOrder(c)


if __name__ == '__main__':
    s = 'ACB'
    findLexicographic(s)
import random
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(A, low, high, pivot):
    pIndex = low
    j = low
    while j < high:
        if A[j] < pivot:
            swap(A, pIndex, j)
            pIndex = pIndex + 1
        elif A[j] == pivot:
            swap(A, j, high)
            j = j - 1
        j = j + 1

    swap(A, pIndex, high)
    return pIndex


def findMatchingPairs(red, blue, low, high):
    if low >= high:
        return

    r = random.randint(low, high)
    chosenJug = red[r]
    pivot = partition(red, low, high, chosenJug)

    partition(blue, low, high, chosenJug)

    findMatchingPairs(red, blue, low, pivot - 1)
    findMatchingPairs(red, blue, pivot + 1, high)


if __name__ == '__main__':
    red = [6, 3, 2, 8, 7]
    blue = [8, 6, 7, 2, 3]

    findMatchingPairs(red, blue, 0, len(red) - 1)

    print('Red jugs:', red)
    print('Blue jugs:', blue)
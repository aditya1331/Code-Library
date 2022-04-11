
def findTriplet(A):
    A.sort()

    n = len(A)

    if n <= 2:
        print("No triplet exists. The array has less than 3 elements.")

    if A[n - 1] * A[n - 2] * A[n - 3] > A[0] * A[1] * A[n - 1]:
        print("Triplet is", (A[n - 1], A[n - 2], A[n - 3]))
    else:
        print("Triplet is", (A[0], A[1], A[n - 1]))


if __name__ == '__main__':
    A = [-4, 1, -8, 9, 6]
    findTriplet(A)
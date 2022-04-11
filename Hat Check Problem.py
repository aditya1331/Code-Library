# Recursive function to count the derangements of an n–element set
def derangements(n):
    # base case
    if n == 1 or n == 2:
        return n - 1

    # recur using the recurrence relation
    return (n - 1) * (derangements(n - 1) + derangements(n - 2))


if __name__ == '__main__':
    n = 4
    print(f'The total number of derangements of a {n}–element set is', derangements(n))


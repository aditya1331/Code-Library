
def divide(x, y):
    INF = 100000000000.0
    if y == 0:
        return INF

    left = 0.0
    right = INF

    precision = 0.001

    sign = 1
    if x * y < 0:
        sign = -1

    x = abs(x)
    y = abs(y)

    while True:
        mid = left + (right - left) / 2

        if abs(y * mid - x) <= precision:
            return mid * sign

        if y * mid < x:
            left = mid
        else:
            right = mid


if __name__ == '__main__':
    print(divide(22, 7))
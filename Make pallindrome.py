def LCS(s1,s2):
    n = len(s1)
    m = 0
    x = [0] * (n + 1)
    y = [0] * (n + 1)

    for i in range(n):
        for j in range(n):
            if s1[i] == s2[j]:
                y[j + 1] = 1 + x[j]
                if m < y[j + 1]:
                    m = y[j + 1]
            else:
                y[j + 1] = max(y[j], x[j + 1])
            x[j] = y[j]
            y[j] = 0
    return m


s= input()
print(len(s)-LCS(s, s))


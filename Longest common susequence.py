s1 = input()
s2 = input()
if (len(s1)==len(s2)):
    n = len(s1)
    st = []
    dp= [[0for i in range(n+1)] for j in range(n+1)]
    for i in range(n):
        for j in range(n):
            if s1[i] == s2[j]:
                st.append(i)
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    result = ''
    for i in st:
        result += s1[i]
    print(result)

else:
    print('Enter equal length string')

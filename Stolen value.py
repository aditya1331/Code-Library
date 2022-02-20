n = int(input())
ar = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    dp[i] = max(dp[i-1], dp[i-2]+ar[i])
print(dp[-1])
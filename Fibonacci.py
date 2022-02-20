
n= int(input())


def fib(n, memo=[0,1]):
    if len(memo)>n:
        return memo[n-1]
    if n<=2:
        return 1
    else:
        memo.append(fib(n-1, memo)+fib(n-2, memo))
        return memo[-1]






print(fib(n))

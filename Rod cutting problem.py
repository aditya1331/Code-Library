n = int(input('Enter the length of rob '))
result =[0 for i in range(n)]
for i in range(2, n):
    for j in range(i//2+1):
        result[i] = max(result[i], j*(i-j), j*result[i-j])
print(result[-1])
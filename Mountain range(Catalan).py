n = int(input())
catalan = [1, 1, 2]
pascal = [1, 2, 1]
temp = []
for ii in range(4, n+2, 2):
    temp = [1, ii]
    for i in range(ii//2-1):
        temp.append(pascal[i]+pascal[i+1]*2+pascal[i+2])
    s = temp[0:ii//2]
    s.reverse()
    temp += s
    pascal = temp
    catalan.append(pascal[len(pascal)//2]-pascal[len(pascal)//2-2])
print(catalan)




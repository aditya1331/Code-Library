def sort(a):
    a.sort(key = lambda x:(len(x), x))

    print(type(a))
    return a
a=[]
for i in range(int(input())):
    a.append(input())
a=sort(a)

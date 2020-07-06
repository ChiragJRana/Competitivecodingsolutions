from sys import stdin,stdout
for _ in range(int(input())):
    N = int(input())
    x = {}
    y = {}
    li = []
    for i in range(4*N - 1):
        li.append(list(map(int,stdin.readline().split())))
    for item in li:
        x[item[0]] = x.get(item[0],0) + 1
        y[item[1]] = y.get(item[1],0) + 1
    for item in x.keys():
        if x[item] % 2 != 0:
            xval = item
    for item in y.keys():
        if y[item] % 2 != 0:
            yval = item
    print(xval, yval)
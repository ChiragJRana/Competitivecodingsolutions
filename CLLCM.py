from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N=int(input())
    mylist = list(map(int, stdin.readline().split()))
    i = 0
    lag = 0
    p = max(mylist)
    if p%2 == 0:
        print('NO')
        continue
    for item in mylist:
        if p % item != 0:
            lag = 1

    if lag == 1:
        print('NO')
    else: print('YES')